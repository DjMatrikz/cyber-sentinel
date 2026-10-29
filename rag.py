#!/usr/bin/env python3
"""
cyber-sentinel RAG — ask questions answered from your own security notes.

- Reads every .md file under ./notes (skips folders starting with . or _)
- Embeds them with nomic-embed-text into a local, persistent Chroma DB
- Retrieves the most relevant chunks for your question
- Answers with the cyber-sentinel model, grounded in those chunks

First run builds the index (one-time, takes a few minutes).
Later runs reuse it instantly.
"""

import os
import glob
import ollama
import chromadb

NOTES_DIR   = "notes"
DB_DIR      = "chroma_db"
COLLECTION  = "cybervault"
EMBED_MODEL = "nomic-embed-text"
CHAT_MODEL  = "security-ai"
CHUNK_SIZE  = 1200     # characters per chunk
CHUNK_OVER  = 150      # overlap so ideas aren't cut in half
TOP_K       = 5        # how many chunks to feed the model


def find_markdown(root):
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        # skip hidden/system folders like .obsidian and _maps-less dotfolders
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for f in filenames:
            if f.endswith(".md"):
                files.append(os.path.join(dirpath, f))
    return files


def chunk_text(text):
    chunks = []
    i = 0
    while i < len(text):
        chunks.append(text[i:i + CHUNK_SIZE])
        i += CHUNK_SIZE - CHUNK_OVER
    return chunks


def embed(text):
    return ollama.embeddings(model=EMBED_MODEL, prompt=text)["embedding"]


def build_or_load(client):
    existing = [c.name for c in client.list_collections()]
    if COLLECTION in existing:
        col = client.get_collection(COLLECTION)
        if col.count() > 0:
            print(f"Loaded existing index: {col.count()} chunks. Ready.\n")
            return col
        client.delete_collection(COLLECTION)

    col = client.create_collection(COLLECTION)
    files = find_markdown(NOTES_DIR)
    print(f"Indexing {len(files)} notes (one-time)...")
    cid = 0
    for n, path in enumerate(files, 1):
        try:
            text = open(path, encoding="utf-8", errors="ignore").read()
        except Exception:
            continue
        for chunk in chunk_text(text):
            if not chunk.strip():
                continue
            col.add(
                ids=[str(cid)],
                embeddings=[embed(chunk)],
                documents=[chunk],
                metadatas=[{"source": os.path.basename(path)}],
            )
            cid += 1
        if n % 50 == 0:
            print(f"  ...{n}/{len(files)} files")
    print(f"Done. {cid} chunks indexed.\n")
    return col


def ask(col, question):
    q_emb = embed(question)
    res = col.query(query_embeddings=[q_emb], n_results=TOP_K)
    docs = res["documents"][0]
    srcs = [m["source"] for m in res["metadatas"][0]]
    context = "\n\n---\n\n".join(docs)

    prompt = (
        "Use the following reference material from my security notes to answer.\n\n"
        f"=== REFERENCE ===\n{context}\n=== END REFERENCE ===\n\n"
        f"Question: {question}"
    )
    print("\ncyber-sentinel:\n")
    stream = ollama.chat(
        model=CHAT_MODEL,
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    for part in stream:
        print(part["message"]["content"], end="", flush=True)
    print("\n\n(sources: " + ", ".join(sorted(set(srcs))) + ")\n")


def main():
    if not os.path.isdir(NOTES_DIR):
        print(f"No '{NOTES_DIR}' folder found. Link your vault:  ln -s <path> notes")
        return
    client = chromadb.PersistentClient(path=DB_DIR)
    col = build_or_load(client)
    print("Ask a security question (or 'exit'):")
    while True:
        try:
            q = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if q.lower() in ("exit", "quit", "/bye", ""):
            break
        ask(col, q)


if __name__ == "__main__":
    main()
