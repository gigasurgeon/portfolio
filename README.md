# Amit Kumar Singh — Portfolio

A dependency-free portfolio website. No build step, no npm install.

## Themes

Open **`themes.html`** first — it's a picker that previews every look. Each theme is a
full standalone page and each has its own built-in **light/dark toggle** (top-right). 

**Structural layouts** — genuinely different placement, components, and navigation:

| File | Layout | Structure |
|------|--------|-----------|
| `index-dossier.html` | **Dossier** | Fixed sidebar nav; ruled data rows; expandable systems ledger (no cards) |
| `index-magazine.html` | **Magazine** | Newspaper masthead; stat ticker; drop-cap columns; roman-numeral articles |
| `index-console.html` | **Console** | Interactive terminal; commands type themselves; ASCII tables & charts |

> Note: these three are standalone files — if you change content, edit them directly
> (generate_themes.py only syncs the Aurora-based palette variants below).

**Palette variants** — same structure as Aurora, different skin:

| File | Theme | Vibe |
|------|-------|------|
| `index.html` | **Aurora** | Space-black, purple→cyan→pink gradient, floating orbs (default) |
| `index-terminal.html` | **Terminal** | Phosphor-green monospace, hacker-console |
| `index-synthwave.html` | **Synthwave** | Neon magenta/cyan on indigo, heavy glow |
| `index-editorial.html` | **Editorial** | Warm ivory, elegant serif, light-first |
| `index-sakura.html` | **Sakura** | Artistic watercolor pastels, italic serif, petal-soft |
| `index-brutalist.html` | **Brutalist** | Artistic poster: stark white, massive type, hard shadows |
| `index-blueprint.html` | **Blueprint** | Drafting-table blue, chalk gridlines, dashed linework |
| `index-noir.html` | **Noir & Gold** | Luxe black + champagne gold, high-fashion serif |

Once you pick one, that's the file to deploy (rename it to `index.html` if needed).

The variants are generated from `index.html` by `generate_themes.py`. If you edit the
**content** of `index.html`, re-run `python3 generate_themes.py` to sync the others.

## Resume PDF

`Amit_Kumar_Singh_Resume.pdf` is compiled from `resume.tex` (the original LaTeX resume
template, with updated content + hyperlinked portfolio/LinkedIn). To update it, edit
`resume.tex` and recompile with [tectonic](https://tectonic-typesetting.github.io):

```bash
# one-time install if needed:  curl -fsSL https://drop-sh.fullyjustified.net | sh
tectonic resume.tex && mv resume.pdf Amit_Kumar_Singh_Resume.pdf
```

## Run it locally

**Option 1 — just open it**

Double-click `index.html`, or open it in your browser:

```bash
# macOS
open index.html
# Linux
xdg-open index.html
# Windows
start index.html
```

**Option 2 — local web server** (recommended; some browsers restrict fonts on `file://`)

```bash
# Python 3 (built in on most laptops)
python3 -m http.server 8000
```

Then visit **http://localhost:8000/themes.html** to pick a theme (or `http://localhost:8000/` for the default Aurora look).

```bash
# or with Node, if you prefer
npx serve .
```

## Edit it

Everything lives in `index.html` — HTML, CSS, and JS in one file. Search for the
section you want (e.g. `id="experience"`) and edit the text directly. Refresh the
browser to see changes.

## Deploy it (later)

Because it's a static file, you can host it free anywhere:

- **GitHub Pages** — push this folder to a repo, enable Pages on the branch.
- **Netlify / Vercel** — drag-and-drop the folder, or connect the repo.
- **Cloudflare Pages** — same, point it at this folder.
