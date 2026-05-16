# Writing (org site)

Markdown sources for **https://ai-guiders.github.io/writing/** (EN) and **/ru/writing/** (RU).

## Add an article

1. Create `en/your-slug.md` and `ru/your-slug.md` with the **same `slug`** in front matter.
2. Run from repo root:

```bash
dotnet script tools/build-writing.csx
```

3. Commit both `src/writing/**` and generated `docs/writing/**` (and `docs/ru/writing/**`).

## Front matter

```yaml
---
slug: your-slug
title: "Page title"
description: "One line for meta and index cards."
date_display: "May 2026"
order: 10
tags:
  - mcp
  - agents
---
```

- **order** — lower appears first on the index (higher numbers = newer on top if you use ascending sort — check build script; KDGIO uses higher order for newer items).
- **tags** — optional; generates tag pages under `writing/tag/`.

Body is standard Markdown (Markdig with advanced extensions).

## Nav

Generated pages use `articles.css` and org nav (About, Open stack, Writing, Handbook, GitHub). Landing pages: edit `tools/gen_pages.py` and run `python tools/gen_pages.py`.
