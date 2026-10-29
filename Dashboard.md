---
tags: [home, dashboard]
---

# 📊 Dashboard

Live queries over the vault. **Requires the Dataview community plugin**
(Settings → Community plugins → Browse → "Dataview" → Install → Enable).

## Technique counts by tactic
```dataview
TABLE length(rows) AS Techniques
FROM #attack
WHERE attack_id
FLATTEN tactics AS tactic
GROUP BY tactic
SORT length(rows) DESC
```

## All Windows credential-access techniques
```dataview
LIST
FROM #attack/tactic/credential-access AND #platform/windows
SORT file.name ASC
```

## Every Linux technique
```dataview
LIST
FROM #platform/linux
SORT file.name ASC
```

## Find a technique by ID or name
Change the search text below, then it lists matches:
```dataview
LIST
FROM #attack
WHERE contains(lower(file.name), "dumping")
```

## Random technique to study (daily learning)
```dataview
LIST
FROM #attack
WHERE attack_id
SORT file.mtime DESC
LIMIT 5
```
