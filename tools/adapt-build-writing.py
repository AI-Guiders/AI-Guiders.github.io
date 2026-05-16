# -*- coding: utf-8 -*-
"""One-off: adapt KDGIO build-writing.csx for AI-Guiders.github.io."""
from pathlib import Path

SRC = Path(r"d:\Experiments\Personal Cursor Folder\KarataevDmitry.github.io\tools\build-writing.csx")
DST = Path(__file__).resolve().parent / "build-writing.csx"

t = SRC.read_text(encoding="utf-8")

replacements = [
    ("https://karataevdmitry.github.io", "https://ai-guiders.github.io"),
    ("Dmitry Karataev", "AI-Guiders"),
    ("Дмитрий Каратаев", "AI-Guiders"),
    ("D<span>.</span>Karataev", "AI<span>-</span>Guiders"),
    ("Д<span>.</span>Каратаев", "AI<span>-</span>Guiders"),
    ("https://github.com/KarataevDmitry", "https://github.com/AI-Guiders"),
    ("&#x1F4BB;", "&#x1F916;"),
    (
        'new NavLabels("Skip to content", "Main navigation", "Language", "About", "Projects", "Writing", "Experience", "Docs", "All writing", "Email", "Telegram", "GitHub", "All tags")',
        'new NavLabels("Skip to content", "Main navigation", "Language", "About", "Open stack", "Writing", "Handbook", "GitHub", "All writing", "Email", "Telegram", "GitHub", "All tags")',
    ),
    (
        'new NavLabels("К содержанию", "Основная навигация", "Язык", "О себе", "Проекты", "Тексты", "Опыт", "Документы", "Все тексты", "Email", "Telegram", "GitHub", "Все теги")',
        'new NavLabels("К содержанию", "Основная навигация", "Язык", "О нас", "Open stack", "Тексты", "Handbook", "GitHub", "Все тексты", "Email", "Telegram", "GitHub", "Все теги")',
    ),
]

for a, b in replacements:
    t = t.replace(a, b)

nav_line_replacements = [
    ('{home}#projects', '{home}#stack'),
    ('{home}#experience', 'https://github.com/AI-Guiders/handbook/wiki'),
    ('{home}#documents', 'https://github.com/AI-Guiders'),
]
for old, new in nav_line_replacements:
    t = t.replace(old, new)

# Footer: drop personal email/telegram lines (org site)
for line in [
    '    sb.AppendLine($"        <a href=\\"mailto:dkarataev1990@gmail.com\\">{labels.Email}</a>");',
    '    sb.AppendLine($"        <a href=\\"https://t.me/karataev_dmitry\\">{labels.Telegram}</a>");',
]:
    t = t.replace(line + "\n", "")

DST.write_text(t, encoding="utf-8", newline="\n")
print("wrote", DST)
