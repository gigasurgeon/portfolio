"""
Generates standalone themed variants of the portfolio from the base index.html.

Each theme is a full, self-contained HTML file that swaps the colour palette,
fonts, and a few decorative rules. Re-run this whenever index.html's content
changes so the variants stay in sync:  python3 generate_themes.py
"""

from pathlib import Path

HERE = Path(__file__).parent
BASE = (HERE / "index.html").read_text(encoding="utf-8")

FONT_LINK = '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />'

ROOT_BLOCK = """  :root {
    --bg: #06070d;
    --bg-2: #0b0d17;
    --panel: rgba(255, 255, 255, 0.03);
    --panel-border: rgba(255, 255, 255, 0.08);
    --text: #e7e9f3;
    --muted: #969ab5;
    --faint: #6a6f8c;
    --accent: #7c5cff;
    --accent-2: #22d3ee;
    --accent-3: #f472b6;
    --glow: rgba(124, 92, 255, 0.35);
    --max: 1080px;
    --orb-opacity: 0.5;
    --grid-line: rgba(255,255,255,0.025);
    --nav-bg: rgba(6, 7, 13, 0.55);
    --nav-bg-scrolled: rgba(6, 7, 13, 0.8);
  }

  [data-theme="light"] {
    --bg: #f4f5fb;
    --bg-2: #ffffff;
    --panel: rgba(10, 12, 30, 0.02);
    --panel-border: rgba(10, 12, 30, 0.1);
    --text: #14162b;
    --muted: #4c5170;
    --faint: #868bab;
    --accent: #6b46f0;
    --accent-2: #0891b2;
    --accent-3: #db2777;
    --glow: rgba(107, 70, 240, 0.25);
    --orb-opacity: 0.28;
    --grid-line: rgba(10,12,30,0.04);
    --nav-bg: rgba(244, 245, 251, 0.65);
    --nav-bg-scrolled: rgba(244, 245, 251, 0.85);
  }"""


def make_root(dark: dict, light: dict) -> str:
    def block(selector: str, v: dict) -> str:
        lines = "\n".join(f"    {k}: {val};" for k, val in v.items())
        return f"{selector} {{\n{lines}\n  }}"
    return "  " + block(":root", dark) + "\n\n  " + block('[data-theme="light"]', light)


# Shared, non-colour vars carried into every theme's :root.
COMMON = {"--max": "1080px"}


THEMES = {
    "terminal": {
        "label": "Terminal",
        "blurb": "Monospace, phosphor-green, hacker-console aesthetic.",
        "default_light": False,
        "fonts": {
            "link": '<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet" />',
            "'Space Grotesk'": "'JetBrains Mono'",
            "'Inter'": "'IBM Plex Mono'",
        },
        "dark": {
            "--bg": "#050806", "--bg-2": "#081109",
            "--panel": "rgba(0, 255, 156, 0.04)", "--panel-border": "rgba(0, 255, 156, 0.18)",
            "--text": "#c9f9de", "--muted": "#6fbf91", "--faint": "#3d7a56",
            "--accent": "#00ff9c", "--accent-2": "#37e0c0", "--accent-3": "#a6ff00",
            "--glow": "rgba(0, 255, 156, 0.3)", **COMMON,
            "--orb-opacity": "0.25", "--grid-line": "rgba(0,255,156,0.05)",
            "--nav-bg": "rgba(5, 8, 6, 0.6)", "--nav-bg-scrolled": "rgba(5, 8, 6, 0.85)",
        },
        "light": {
            "--bg": "#eafff4", "--bg-2": "#ffffff",
            "--panel": "rgba(4, 60, 40, 0.03)", "--panel-border": "rgba(4, 90, 60, 0.18)",
            "--text": "#043824", "--muted": "#2f6b4d", "--faint": "#6fa588",
            "--accent": "#009e63", "--accent-2": "#0e8f7a", "--accent-3": "#3f8f00",
            "--glow": "rgba(0, 158, 99, 0.2)",
            "--orb-opacity": "0.18", "--grid-line": "rgba(4,90,60,0.05)",
            "--nav-bg": "rgba(234, 255, 244, 0.7)", "--nav-bg-scrolled": "rgba(234, 255, 244, 0.9)",
        },
        "extra_css": """
  /* Terminal theme: crisp, boxy edges */
  .btn, .stat, .skill-cat, .proj, .fcard, .about-card, .theme-toggle,
  .tag, .proj .stack span, .fbody .stack span { border-radius: 4px !important; }
  .fmedia { background: #050806; }
  h1, h2, h3 { letter-spacing: -0.01em; }""",
    },

    "synthwave": {
        "label": "Synthwave",
        "blurb": "Neon magenta + cyan on deep indigo, heavy glow.",
        "default_light": False,
        "fonts": {
            "link": '<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />',
            "'Space Grotesk'": "'Chakra Petch'",
        },
        "dark": {
            "--bg": "#120428", "--bg-2": "#1a0a38",
            "--panel": "rgba(255, 47, 185, 0.05)", "--panel-border": "rgba(45, 226, 230, 0.2)",
            "--text": "#f5e9ff", "--muted": "#b39ccf", "--faint": "#7c6a9c",
            "--accent": "#ff2fb9", "--accent-2": "#2de2e6", "--accent-3": "#ff9e2c",
            "--glow": "rgba(255, 47, 185, 0.45)", **COMMON,
            "--orb-opacity": "0.6", "--grid-line": "rgba(45,226,230,0.06)",
            "--nav-bg": "rgba(18, 4, 40, 0.6)", "--nav-bg-scrolled": "rgba(18, 4, 40, 0.85)",
        },
        "light": {
            "--bg": "#fdf0fb", "--bg-2": "#ffffff",
            "--panel": "rgba(214, 31, 145, 0.04)", "--panel-border": "rgba(214, 31, 145, 0.16)",
            "--text": "#3a0b30", "--muted": "#7a3767", "--faint": "#b07fa0",
            "--accent": "#d61f8c", "--accent-2": "#0b9aa0", "--accent-3": "#d97706",
            "--glow": "rgba(214, 31, 145, 0.3)",
            "--orb-opacity": "0.3", "--grid-line": "rgba(214,31,145,0.05)",
            "--nav-bg": "rgba(253, 240, 251, 0.7)", "--nav-bg-scrolled": "rgba(253, 240, 251, 0.9)",
        },
        "extra_css": """
  /* Synthwave theme: amped-up glow */
  .hero h1 .grad, .contact h2 .grad { filter: drop-shadow(0 0 22px var(--glow)); }
  .stat:hover, .skill-cat:hover, .proj:hover, .fcard:hover { box-shadow: 0 12px 44px var(--glow); }
  .orb { filter: blur(80px); }
  .fmedia { background: #120428; }""",
    },

    "editorial": {
        "label": "Editorial",
        "blurb": "Light-first, warm ivory, elegant serif display type.",
        "default_light": True,
        "fonts": {
            "link": '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />',
            "'Space Grotesk'": "'Fraunces'",
        },
        # For editorial, ":root" holds the LIGHT palette (default), and
        # [data-theme="light"] holds the DARK one — because default_light flips
        # the attribute. Simpler: keep semantics, set <html data-theme> below.
        "dark": {
            "--bg": "#14110c", "--bg-2": "#1d1913",
            "--panel": "rgba(255, 248, 235, 0.04)", "--panel-border": "rgba(255, 248, 235, 0.12)",
            "--text": "#f3ece0", "--muted": "#b8ac98", "--faint": "#7f7565",
            "--accent": "#c2724a", "--accent-2": "#6ba58f", "--accent-3": "#c4607a",
            "--glow": "rgba(194, 114, 74, 0.3)", **COMMON,
            "--orb-opacity": "0.3", "--grid-line": "rgba(255,248,235,0.03)",
            "--nav-bg": "rgba(20, 17, 12, 0.6)", "--nav-bg-scrolled": "rgba(20, 17, 12, 0.85)",
        },
        "light": {
            "--bg": "#faf7f1", "--bg-2": "#ffffff",
            "--panel": "rgba(40, 30, 20, 0.025)", "--panel-border": "rgba(40, 30, 20, 0.12)",
            "--text": "#20180f", "--muted": "#5c5344", "--faint": "#9a8f7d",
            "--accent": "#b45309", "--accent-2": "#0f766e", "--accent-3": "#a83a54",
            "--glow": "rgba(180, 83, 9, 0.18)",
            "--orb-opacity": "0.16", "--grid-line": "rgba(40,30,20,0.035)",
            "--nav-bg": "rgba(250, 247, 241, 0.75)", "--nav-bg-scrolled": "rgba(250, 247, 241, 0.92)",
        },
        "extra_css": """
  /* Editorial theme: refined serif display, softer motion */
  h1, h2.section-title, .contact h2, .job .role, .fbody h3, .proj h3 { font-weight: 600; }
  .hero h1 { letter-spacing: -0.02em; }
  .fmedia { background: #14110c; }""",
    },

    "sakura": {
        "label": "Sakura",
        "blurb": "Artistic watercolor pastels — cherry blossom pink, plum ink, soft paper.",
        "default_light": True,
        "fonts": {
            "link": '<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Nunito+Sans:wght@400;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />',
            "'Space Grotesk'": "'DM Serif Display'",
            "'Inter'": "'Nunito Sans'",
        },
        "dark": {
            "--bg": "#221521", "--bg-2": "#2b1b29",
            "--panel": "rgba(255, 214, 235, 0.05)", "--panel-border": "rgba(255, 214, 235, 0.16)",
            "--text": "#f7e6f0", "--muted": "#c3a2b6", "--faint": "#8a6d7e",
            "--accent": "#f47fb4", "--accent-2": "#9d8fe0", "--accent-3": "#f4b47f",
            "--glow": "rgba(244, 127, 180, 0.3)", **COMMON,
            "--orb-opacity": "0.35", "--grid-line": "rgba(255,214,235,0.04)",
            "--nav-bg": "rgba(34, 21, 33, 0.6)", "--nav-bg-scrolled": "rgba(34, 21, 33, 0.85)",
        },
        "light": {
            "--bg": "#fdf5f7", "--bg-2": "#ffffff",
            "--panel": "rgba(150, 60, 110, 0.03)", "--panel-border": "rgba(150, 60, 110, 0.14)",
            "--text": "#3d1f33", "--muted": "#7c5069", "--faint": "#b58ea2",
            "--accent": "#d4517f", "--accent-2": "#7c6bc9", "--accent-3": "#d4894f",
            "--glow": "rgba(212, 81, 127, 0.2)",
            "--orb-opacity": "0.3", "--grid-line": "rgba(150,60,110,0.045)",
            "--nav-bg": "rgba(253, 245, 247, 0.72)", "--nav-bg-scrolled": "rgba(253, 245, 247, 0.92)",
        },
        "extra_css": """
  /* Sakura theme: watercolor softness — italic serif accents, petal-round corners */
  .stat, .skill-cat, .proj, .fcard, .about-card, .quote { border-radius: 26px; }
  .hero h1 .grad { font-style: italic; }
  .eyebrow { letter-spacing: 0.26em; }
  .orb { filter: blur(110px); }
  .fmedia { background: #221521; }""",
    },

    "brutalist": {
        "label": "Brutalist",
        "blurb": "Artistic poster style — stark paper white, massive black type, hard shadows.",
        "default_light": True,
        "fonts": {
            "link": '<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Archivo:wght@400;500;600&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet" />',
            "'Space Grotesk'": "'Archivo Black'",
            "'Inter'": "'Archivo'",
            "'JetBrains Mono'": "'Space Mono'",
        },
        "dark": {
            "--bg": "#111111", "--bg-2": "#181818",
            "--panel": "rgba(255, 255, 255, 0.03)", "--panel-border": "#3a3a3a",
            "--text": "#f4f1ea", "--muted": "#b5b0a4", "--faint": "#7d786d",
            "--accent": "#ffd400", "--accent-2": "#ff4d00", "--accent-3": "#00c2ff",
            "--glow": "rgba(255, 212, 0, 0.25)", **COMMON,
            "--orb-opacity": "0.14", "--grid-line": "rgba(255,255,255,0.05)",
            "--nav-bg": "rgba(17, 17, 17, 0.7)", "--nav-bg-scrolled": "rgba(17, 17, 17, 0.92)",
        },
        "light": {
            "--bg": "#f4f1ea", "--bg-2": "#ffffff",
            "--panel": "rgba(17, 17, 17, 0.02)", "--panel-border": "#111111",
            "--text": "#111111", "--muted": "#44403a", "--faint": "#8a857b",
            "--accent": "#e0b000", "--accent-2": "#e04400", "--accent-3": "#0077b6",
            "--glow": "rgba(224, 176, 0, 0.3)",
            "--orb-opacity": "0.12", "--grid-line": "rgba(17,17,17,0.07)",
            "--nav-bg": "rgba(244, 241, 234, 0.8)", "--nav-bg-scrolled": "rgba(244, 241, 234, 0.95)",
        },
        "extra_css": """
  /* Brutalist theme: zero radius, thick borders, hard offset shadows */
  .btn, .stat, .skill-cat, .proj, .fcard, .about-card, .theme-toggle, .quote,
  .tag, .proj .stack span, .fbody .stack span, .hero .status { border-radius: 0 !important; }
  .stat, .skill-cat, .proj, .fcard, .about-card, .quote { border-width: 2px; }
  .stat:hover, .skill-cat:hover, .proj:hover, .fcard:hover {
    transform: translate(-3px, -3px); box-shadow: 6px 6px 0 var(--panel-border);
  }
  .btn.primary { background: var(--accent); color: #111; box-shadow: 4px 4px 0 var(--text); }
  .btn.primary:hover { transform: translate(-2px, -2px); box-shadow: 6px 6px 0 var(--text); }
  .btn.ghost { border: 2px solid var(--panel-border); }
  h1, h2.section-title, .contact h2 { text-transform: uppercase; letter-spacing: -0.01em; }
  .hero h1 { font-size: clamp(2.4rem, 7vw, 4.6rem); line-height: 1.05; }
  .hero h1 .grad { background: none; -webkit-text-fill-color: currentColor; color: var(--accent-2); }
  .contact h2 .grad { background: none; -webkit-text-fill-color: currentColor; color: var(--accent-2); }
  .proj:hover::after { opacity: 0; }
  .fmedia { background: #111111; }""",
    },

    "blueprint": {
        "label": "Blueprint",
        "blurb": "Artistic-technical — drafting-table blue, chalk lines, dashed borders.",
        "default_light": False,
        "fonts": {
            "link": '<link href="https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet" />',
            "'Space Grotesk'": "'Josefin Sans'",
            "'Inter'": "'IBM Plex Sans'",
            "'JetBrains Mono'": "'IBM Plex Mono'",
        },
        "dark": {
            "--bg": "#0a2447", "--bg-2": "#0d2c55",
            "--panel": "rgba(214, 232, 255, 0.04)", "--panel-border": "rgba(214, 232, 255, 0.28)",
            "--text": "#eaf3ff", "--muted": "#a8c4e5", "--faint": "#6d8db3",
            "--accent": "#ffffff", "--accent-2": "#7fd4ff", "--accent-3": "#ffd166",
            "--glow": "rgba(127, 212, 255, 0.25)", **COMMON,
            "--orb-opacity": "0.18", "--grid-line": "rgba(214,232,255,0.09)",
            "--nav-bg": "rgba(10, 36, 71, 0.65)", "--nav-bg-scrolled": "rgba(10, 36, 71, 0.9)",
        },
        "light": {
            "--bg": "#eef4fb", "--bg-2": "#ffffff",
            "--panel": "rgba(16, 58, 110, 0.03)", "--panel-border": "rgba(16, 58, 110, 0.3)",
            "--text": "#0f2b4f", "--muted": "#3f608a", "--faint": "#7f99bb",
            "--accent": "#0f4c92", "--accent-2": "#0779a8", "--accent-3": "#b07d1e",
            "--glow": "rgba(15, 76, 146, 0.18)",
            "--orb-opacity": "0.12", "--grid-line": "rgba(16,58,110,0.1)",
            "--nav-bg": "rgba(238, 244, 251, 0.75)", "--nav-bg-scrolled": "rgba(238, 244, 251, 0.94)",
        },
        "extra_css": """
  /* Blueprint theme: drafting-table linework */
  .stat, .skill-cat, .proj, .fcard, .about-card, .quote { border-style: dashed; border-radius: 6px; }
  .grid-overlay { mask-image: none; opacity: 0.9; }
  .hero h1 .grad, .contact h2 .grad { background: none; -webkit-text-fill-color: currentColor; color: var(--accent-2); text-decoration: underline; text-decoration-style: dashed; text-decoration-thickness: 2px; text-underline-offset: 8px; }
  .timeline::before { background: var(--panel-border); }
  .job::before { border-style: dashed; }
  .fmedia { background: #0a2447; }""",
    },

    "noir": {
        "label": "Noir & Gold",
        "blurb": "Luxe black and champagne gold, high-fashion serif.",
        "default_light": False,
        "fonts": {
            "link": '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />',
            "'Space Grotesk'": "'Playfair Display'",
        },
        "dark": {
            "--bg": "#0b0a08", "--bg-2": "#12100c",
            "--panel": "rgba(212, 180, 116, 0.04)", "--panel-border": "rgba(212, 180, 116, 0.18)",
            "--text": "#f2ead9", "--muted": "#b3a78d", "--faint": "#78705d",
            "--accent": "#d4b474", "--accent-2": "#e8d9b0", "--accent-3": "#a67c52",
            "--glow": "rgba(212, 180, 116, 0.25)", **COMMON,
            "--orb-opacity": "0.22", "--grid-line": "rgba(212,180,116,0.045)",
            "--nav-bg": "rgba(11, 10, 8, 0.65)", "--nav-bg-scrolled": "rgba(11, 10, 8, 0.9)",
        },
        "light": {
            "--bg": "#f8f4ec", "--bg-2": "#ffffff",
            "--panel": "rgba(60, 48, 24, 0.03)", "--panel-border": "rgba(60, 48, 24, 0.14)",
            "--text": "#2a2416", "--muted": "#6b5f45", "--faint": "#a4977c",
            "--accent": "#9a7830", "--accent-2": "#7a6a3f", "--accent-3": "#8a5a2e",
            "--glow": "rgba(154, 120, 48, 0.18)",
            "--orb-opacity": "0.14", "--grid-line": "rgba(60,48,24,0.05)",
            "--nav-bg": "rgba(248, 244, 236, 0.75)", "--nav-bg-scrolled": "rgba(248, 244, 236, 0.94)",
        },
        "extra_css": """
  /* Noir & Gold theme: hairline luxury */
  .stat, .skill-cat, .proj, .fcard, .about-card, .quote { border-radius: 10px; }
  h1, h2.section-title, .contact h2 { font-weight: 600; }
  .hero h1 .grad, .contact h2 .grad {
    background: linear-gradient(115deg, #d4b474, #f0e2bb 55%, #a67c52);
    -webkit-background-clip: text; background-clip: text; color: transparent;
  }
  .eyebrow { color: var(--accent); letter-spacing: 0.3em; }
  .eyebrow::before { background: var(--accent); }
  .fmedia { background: #0b0a08; }""",
    },
}


def build(name: str, cfg: dict) -> str:
    html = BASE

    # The base (Aurora) defaults to light; normalize back to dark-first so each
    # variant's own default_light flag decides, below.
    html = html.replace('<html lang="en" data-theme="light">', '<html lang="en">')
    html = html.replace(
        '<button class="theme-toggle" id="themeToggle" aria-label="Toggle light/dark theme" title="Toggle theme">☀️</button>',
        '<button class="theme-toggle" id="themeToggle" aria-label="Toggle light/dark theme" title="Toggle theme">🌙</button>',
    )

    # Fonts: swap the stylesheet link and family tokens.
    html = html.replace(FONT_LINK, cfg["fonts"]["link"])
    for old, new in cfg["fonts"].items():
        if old == "link":
            continue
        html = html.replace(old, new)

    # Palette blocks.
    html = html.replace(ROOT_BLOCK, make_root(cfg["dark"], cfg["light"]))

    # Namespace the persisted theme key so variant files don't clobber each other.
    key = f"theme-{name}"
    html = html.replace("localStorage.getItem('theme')", f"localStorage.getItem('{key}')")
    html = html.replace("localStorage.setItem('theme', next)", f"localStorage.setItem('{key}', next)")

    # Extra per-theme decorative CSS, injected right before </style>.
    html = html.replace("</style>", cfg["extra_css"] + "\n</style>")

    # Light-first themes: default the document to the light palette.
    if cfg["default_light"]:
        html = html.replace('<html lang="en">', '<html lang="en" data-theme="light">')
        html = html.replace(
            '<button class="theme-toggle" id="themeToggle" aria-label="Toggle light/dark theme" title="Toggle theme">🌙</button>',
            '<button class="theme-toggle" id="themeToggle" aria-label="Toggle light/dark theme" title="Toggle theme">☀️</button>',
        )

    # A small badge so it's obvious which theme file you're viewing.
    html = html.replace(
        '<title>Amit Kumar Singh — AI/ML Engineer</title>',
        f'<title>Amit Kumar Singh — AI/ML Engineer ({cfg["label"]} theme)</title>',
    )
    return html


for name, cfg in THEMES.items():
    out = HERE / f"index-{name}.html"
    out.write_text(build(name, cfg), encoding="utf-8")
    print(f"wrote {out.name}")

print("done")
