# How to Create the AI

Turn this vault into a local AI you can chat with - fully offline, running on your own machine. It reads your notes (RAG) before answering, so responses are grounded in this knowledge base.

Nothing leaves your computer. No API keys, no cloud.

## What you need
- [Ollama](https://ollama.com) (free) - runs local models
- Python 3.10+
- A machine with a GPU helps but isn't required (CPU works, just slower)
- This vault, open as a folder

## Step 1 - Install Ollama and pull a model
Install Ollama from ollama.com, then pull a model:
```bash
ollama pull llama3.1:8b
```
(Any chat model works - swap in whatever you like. ~8B models fit comfortably on 8 GB of VRAM.)

Also pull the embedding model the RAG uses:
```bash
ollama pull nomic-embed-text
```

## Step 2 - Create a custom model (persona)
Create a file named `Modelfile`:
```
FROM llama3.1:8b

SYSTEM """
You are a cybersecurity expert assistant: a senior penetration tester and SOC analyst.
Explain clearly, cite MITRE ATT&CK technique IDs when relevant, think step by step,
and remind users to stay authorized. Ground answers in the provided reference notes.
"""

PARAMETER temperature 0.6
PARAMETER num_ctx 8192
```
Build it:
```bash
ollama create security-ai -f Modelfile
```

## Step 3 - Set up the RAG
```bash
mkdir ai-project && cd ai-project
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install ollama chromadb
```

Link (or copy) your notes into a `notes` folder:
```bash
# macOS/Linux
ln -s "/path/to/CyberVault" notes
# Windows (PowerShell): copy the folder, or use a junction
```

Add the `rag.py` script (see the companion code / repo), then run:
```bash
python rag.py
```
The first run builds the index (one-time). Later runs load it instantly.

## Step 4 - Ask it
```
> How do I detect LSASS credential dumping on Windows?
> Explain a pass-the-hash attack and its MITRE technique ID.
> What nmap command finds all open ports with service versions?
```

## Keeping it current
Add notes to the vault, then re-index:
```bash
rm -rf chroma_db
python rag.py
```

## Notes
- Swap the `FROM` model for any Ollama model to trade speed vs quality.
- Add the OWASP and MITRE data (see the README) to your `notes` folder for deeper coverage.
- This is a study and authorized-testing aid - validate anything important against primary sources.
