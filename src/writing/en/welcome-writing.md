---
slug: welcome-writing
title: "Writing on AI-Guiders"
description: "Org essays and release notes live here; deeper personal posts stay on the author site."
date_display: "May 2026"
order: 1
tags:
  - meta
  - agents
---

This section is the **org writing surface** for AI-Guiders: product direction, open-stack notes, and material that belongs next to the repositories — not only in READMEs or ADRs.

## What goes here

- **Org voice** — parity, observable loops, MCP and IDE decisions we want to cite from the handbook or GitHub.
- **Pointers** — when a topic is personal or experimental, we link out instead of duplicating.

Long-form essays and the full archive remain on [Dmitry Karataev's site](https://karataevdmitry.github.io/writing/) (EN) and [RU](https://karataevdmitry.github.io/ru/writing/). Example cross-post: [Agent Notes MCP 2.0](https://karataevdmitry.github.io/writing/agent-notes-mcp-2-one-config.html).

## How to publish

Add paired `src/writing/en/*.md` and `src/writing/ru/*.md`, then run `dotnet script tools/build-writing.csx` from the repo root. See `src/writing/README.md`.
