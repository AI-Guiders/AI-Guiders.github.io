# Site source is in `docs/` (GitHub Pages). Open https://ai-guiders.github.io/ — not this README.
# AI-Guiders.github.io

Organization site (GitHub Pages): **Settings → Pages → branch `main`, folder `/docs`**.

Live: **https://ai-guiders.github.io/** (after Pages enable).

## Layout

| Path | Content |
|------|---------|
| `docs/index.html` | English landing |
| `docs/ru/index.html` | Russian landing |
| `docs/assets/css/site.css` | Landing styles |
| `docs/assets/css/articles.css` | Writing section styles |
| `docs/writing/`, `docs/ru/writing/` | Generated articles (from `src/writing/`) |
| `src/writing/{en,ru}/*.md` | Markdown sources |
| `tools/build-writing.csx` | Build writing + Atom + tag pages |
| `tools/gen_pages.py` | Regenerate EN/RU landings |

Landings: `python tools/gen_pages.py`. Writing: `dotnet script tools/build-writing.csx` (needs [dotnet-script](https://github.com/dotnet-script/dotnet-script)).

## Related

- [GitHub org profile](https://github.com/AI-Guiders) — `AI-Guiders/.github/profile/README.md`
- [Handbook wiki](https://github.com/AI-Guiders/handbook/wiki) (RU)
- [Personal writing archive](https://karataevdmitry.github.io/writing/) — long-form EN/RU essays

