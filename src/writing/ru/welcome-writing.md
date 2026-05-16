---
slug: welcome-writing
title: "Тексты на AI-Guiders"
description: "Орг-эссе и заметки к релизам — здесь; личный блог остаётся на сайте автора."
date_display: "май 2026"
order: 1
tags:
  - meta
  - agents
---

Здесь — **площадка текстов организации** AI-Guiders: направление продуктов, заметки к open stack и то, что логично держать рядом с репозиториями, а не только в README и ADR.

## Что публикуем здесь

- **Голос организации** — паритет, наблюдаемый контур, решения по MCP и IDE, на которые можно сослаться из handbook или GitHub.
- **Ссылки наружу** — личное и экспериментальное остаётся на личном сайте, здесь даём контекст и ссылку.

Полный архив эссе — на [сайте Дмитрия Каратаева](https://karataevdmitry.github.io/ru/writing/) (RU) и [EN](https://karataevdmitry.github.io/writing/). Пример перекрёстной ссылки: [Agent Notes MCP 2.0](https://karataevdmitry.github.io/writing/agent-notes-mcp-2-one-config.html).

## Как опубликовать

Пара файлов `src/writing/en/*.md` и `src/writing/ru/*.md`, затем из корня репозитория: `dotnet script tools/build-writing.csx`. Подробности — `src/writing/README.md`.
