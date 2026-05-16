# -*- coding: utf-8 -*-
from pathlib import Path

CSS = "/assets/css/site.css"
ORG = "https://github.com/AI-Guiders"

CARDS_EN = [
    ("🚀", "cascade-ide", "C#-first IDE, in-proc MCP, cockpit attention model. MIT.", ["IDE", "Agents"]),
    ("📝", "agent-notes-mcp", "Memory MCP 2.0, one TOML config. With kb-public.", ["MCP", "Memory"]),
    ("📖", "kb-public", "Public KB slice for agents (CC BY-SA).", ["Knowledge", "CC BY-SA"]),
    ("🔍", "RoslynMcp", "Roslyn diagnostics, code actions, rename.", ["C#", "Roslyn"]),
    ("🔧", "dotnet-debug-mcp", "DAP debugging for agents.", ["MCP", "Debug"]),
    ("📚", "agent-first-learn", "Course: designing with and for AI agents. MIT.", ["Course", "Agents"]),
]

CARDS_RU = [
    ("🚀", "cascade-ide", "IDE на C#, in-proc MCP, модель внимания кокпита. MIT.", ["IDE", "Агенты"]),
    ("📝", "agent-notes-mcp", "MCP памяти 2.0, один TOML. В паре с kb-public.", ["MCP", "Память"]),
    ("📖", "kb-public", "Публичный срез KB для агентов (CC BY-SA).", ["Knowledge", "CC BY-SA"]),
    ("🔍", "RoslynMcp", "Диагностики Roslyn, code actions, rename.", ["C#", "Roslyn"]),
    ("🔧", "dotnet-debug-mcp", "Отладка DAP для агентов.", ["MCP", "Debug"]),
    ("📚", "agent-first-learn", "Курс: проектирование с агентами и для агентов. MIT.", ["Курс", "Агенты"]),
]


def cards_html(cards):
    parts = []
    for icon, slug, desc, tags in cards:
        d = desc.replace("kb-public", f'<a href="{ORG}/kb-public">kb-public</a>')
        tag_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
        parts.append(
            "          <div class=\"project-card\">\n"
            "            <div class=\"card-header\">\n"
            f"              <motion class=\"card-icon\" aria-hidden=\"true\">{icon}</motion>\n"
            f"              <h3><a href=\"{ORG}/{slug}\">{slug}</a></h3>\n"
            "            </motion>\n"
            f"            <p class=\"desc\">{d}</p>\n"
            f"            <div class=\"tags\">{tag_html}</div>\n"
            "          </div>"
        )
    text = "\n".join(parts)
    return text.replace("motion", "div")


def page(lang, title, desc, nav_items, hero_label, h1, h1_accent, lead, about_title, about_text,
         stack_title, stack_sub, handbook_title, handbook_sub, handbook_items, footer_links, css_path, base):
    nav_lis = "\n".join(f'          <li><a href="{href}">{label}</a></li>' for href, label in nav_items)
    lang_en = 'aria-current="page"' if lang == "en" else ""
    lang_ru = 'aria-current="page"' if lang == "ru" else ""
    cards = cards_html(CARDS_EN if lang == "en" else CARDS_RU)
    hb = "\n".join(
        f'          <li><a href="{u}">{t}</a><span class="meta">{m}</span></li>'
        for u, t, m in handbook_items
    )
    fl = "\n".join(f'      <a href="{u}">{t}</a>' for u, t in footer_links)
    skip = "К содержанию" if lang == "ru" else "Skip to content"
    nav_aria = "Основная навигация" if lang == "ru" else "Main navigation"
    lang_aria = "Язык" if lang == "ru" else "Language"
    btn_org = "GitHub org"
    btn_stack = "Open stack"

    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="alternate" hreflang="en" href="/" />
  <link rel="alternate" hreflang="ru" href="/ru/" />
  <link rel="alternate" hreflang="x-default" href="/" />
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>&#x1F916;</text></svg>" />
  <link rel="stylesheet" href="{css_path}" />
</head>
<body>
  <a href="#main" class="skip-link">{skip}</a>
  <nav aria-label="{nav_aria}">
    <div class="nav-inner">
      <div class="logo"><a href="{base}">AI<span>-</span>Guiders</a></div>
      <div class="nav-right">
        <ul>
{nav_lis}
        </ul>
        <ul class="nav-lang" aria-label="{lang_aria}">
          <li><a href="/" lang="en" {lang_en}>EN</a></li>
          <li class="nav-sep" aria-hidden="true">|</li>
          <li><a href="/ru/" lang="ru" {lang_ru}>RU</a></li>
        </ul>
      </motion>
    </motion>
  </nav>
  <main id="main">
    <section class="hero">
      <div class="container">
        <div class="hero-content">
          <div class="hero-label">{hero_label}</div>
          <h1>{h1}<br /><span class="accent">{h1_accent}</span></h1>
          <p class="lead">{lead}</p>
          <div class="hero-buttons">
            <a href="{ORG}" class="btn btn-primary">{btn_org}</a>
            <a href="#stack" class="btn btn-outline">{btn_stack}</a>
          </motion>
        </motion>
      </motion>
    </section>
    <section id="about">
      <div class="container">
        <h2 class="section-title">{about_title}</h2>
        <p class="section-subtitle">{about_text}</p>
      </motion>
    </section>
    <section id="stack">
      <div class="container">
        <h2 class="section-title">{stack_title}</h2>
        <p class="section-subtitle">{stack_sub}</p>
        <div class="card-grid">
{cards}
        </motion>
      </motion>
    </section>
    <section id="handbook">
      <div class="container">
        <h2 class="section-title">{handbook_title}</h2>
        <p class="section-subtitle">{handbook_sub}</p>
        <ul class="link-list">
{hb}
        </ul>
      </motion>
    </section>
  </main>
  <footer>
    <div class="links">
{fl}
    </motion>
    <p>AI-Guiders &copy; 2026</p>
  </footer>
</body>
</html>
"""
    return html.replace("motion", "div")


root = Path(__file__).parent / "docs"
(root / "ru").mkdir(parents=True, exist_ok=True)

en = page(
    "en",
    "AI-Guiders — Agent-first open stack for .NET",
    "Open tools for agent-first .NET work: Cascade IDE, MCP servers, shared libraries.",
    [("#about", "About"), ("#stack", "Open stack"), ("#handbook", "Handbook"), (ORG, "GitHub")],
    "Open source · .NET · MCP",
    "Agent-first tools",
    "you can verify",
    "We build an IDE, MCP servers, and shared libraries so humans and coding agents "
    "share the same ground truth — build, tests, git, Roslyn, and agent memory.",
    "What we do",
    "<strong>Parity</strong> — if an agent can do it via MCP, the IDE should not contradict it. "
    "<strong>Observable loop</strong> — one legible contour for editor, tools, and agent. "
    "Essays on <a href=\"https://karataevdmitry.github.io/\">Dmitry Karataev's site</a>; this is the org hub.",
    "Open stack",
    f"Full list: <a href=\"{ORG}\">github.com/AI-Guiders</a>",
    "Handbook & KB",
    "Org norms and agent knowledge.",
    [
        (f"{ORG}/handbook/wiki", "Handbook wiki", "Mission, values, boundaries (Russian)"),
        (f"{ORG}/kb-public", "kb-public", "Public KB for agents"),
        (f"{ORG}/handbook", "handbook repo", "Edit wiki/ folder, sync to GitHub Wiki"),
    ],
    [(ORG, "GitHub"), ("https://karataevdmitry.github.io/", "Writing (personal)")],
    CSS,
    "/",
)
ru = page(
    "ru",
    "AI-Guiders — open stack для agent-first .NET",
    "Открытые инструменты для agent-first .NET: Cascade IDE, MCP, общие библиотеки.",
    [("#about", "О нас"), ("#stack", "Open stack"), ("#handbook", "Handbook"), (ORG, "GitHub")],
    "Open source · .NET · MCP",
    "Инструменты для агентов",
    "которым можно доверять",
    "IDE, MCP-серверы и общие библиотеки — чтобы человек и coding agent смотрели "
    "на одну правду: сборка, тесты, git, Roslyn, память агента.",
    "Что делаем",
    "<strong>Паритет</strong> — если агент делает через MCP, IDE не должна противоречить. "
    "<strong>Наблюдаемый контур</strong> — редактор, инструменты и агент в одной картине. "
    "Тексты — на <a href=\"https://karataevdmitry.github.io/ru/\">сайте Дмитрия Каратаева</a>; здесь — хаб организации.",
    "Open stack",
    f"Полный список: <a href=\"{ORG}\">github.com/AI-Guiders</a>",
    "Handbook и KB",
    "Нормы организации и знания для агентов.",
    [
        (f"{ORG}/handbook/wiki", "Handbook wiki", "Миссия, ценности, границы (RU)"),
        (f"{ORG}/kb-public", "kb-public", "Публичный срез KB"),
        (f"{ORG}/handbook", "репозиторий handbook", "Правки в wiki/, синхрон с GitHub Wiki"),
    ],
    [(ORG, "GitHub"), ("https://karataevdmitry.github.io/ru/", "Тексты (личный сайт)")],
    "/assets/css/site.css",
    "/ru/",
)

(root / "index.html").write_text(en, encoding="utf-8", newline="\n")
(root / "ru" / "index.html").write_text(ru, encoding="utf-8", newline="\n")
print("ok")
