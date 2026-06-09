# kaggle-audit-node24-ci-guard

**Part of the MANIFOLD field computation system.**
**Copyright (c) 2026 Guinea Pig Trench LLC**

---

Kaggle audit kernel for the `node24-ci-guard` product. Analyzes file tree structure, template imports, and self-containedness of deployed TypeScript projects.

## What It Checks

| Check | Method | Purpose |
|-------|--------|---------|
| File tree | `rglob('*')` | Verifies expected structure |
| Hardcoded paths | regex `path.join` | Flags non-portable references |
| Unsafe file ops | regex `copyFileSync` | Flags side-effect imports |

## Deployment

```bash
python push_kernel.py
```

Push credentials are read from `~/.kaggle/kaggle.json`.

## Entity

| Field | Value |
|-------|-------|
| Copyright | Guinea Pig Trench LLC |
| R&D Entity | Guinea Pig Trench LLC (PA, #13674084) |
| Credit Facility | Truth Holds Enterprise (PA #7049023) |
