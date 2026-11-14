import base64, html, json, pathlib, sys
from content import *

ROOT = pathlib.Path(__file__).parent
FA = ROOT / "node_modules/@fontsource-variable/archivo/files"
FS = ROOT / "node_modules/@fontsource-variable/source-serif-4/files"
LATIN = "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"
LATINEXT = "U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF"

def b64(p): return base64.b64encode(p.read_bytes()).decode()

def face(fam, path, rng, style="normal", wght="100 900", wdth=None):
    extra = f"font-stretch:{wdth};" if wdth else ""
    return (f"@font-face{{font-family:'{fam}';font-style:{style};font-display:swap;font-weight:{wght};{extra}"
            f"src:url(data:font/woff2;base64,{b64(path)}) format('woff2');unicode-range:{rng}}}")

FONTS = "".join([
    face("Archivo", FA/"archivo-latin-wdth-normal.woff2", LATIN, wdth="62% 125%"),
    face("Archivo", FA/"archivo-latin-ext-wdth-normal.woff2", LATINEXT, wdth="62% 125%"),
    face("Source Serif", FS/"source-serif-4-latin-wght-normal.woff2", LATIN, wght="200 900"),
    face("Source Serif", FS/"source-serif-4-latin-ext-wght-normal.woff2", LATINEXT, wght="200 900"),
    face("Source Serif", FS/"source-serif-4-latin-wght-italic.woff2", LATIN, style="italic", wght="200 900"),
])

e = html.escape
STATUS = {"live": "Live", "beta": "Public beta", "building": "In development", "client": "Client work"}
P = PERSON

def ext(href, text, cls=""):
    return f'<a class="{cls}" href="{e(href)}" target="_blank" rel="noopener">{e(text)}</a>'

def sdg_chip(n, note=None):
    name, col = SDG[n]
    t = f'<li class="sdg"><span class="sdg-n" style="background:{col}">{n}</span><span><b>Goal {n}: {e(name)}</b>'
    if note: t += f'<span class="sdg-note">{e(note)}</span>'
    return t + "</span></li>"

# ---------- hero route ----------
stops = "".join(
    f'<li class="stop s-{c["status"]}" style="--i:{i}"><a href="#case-{c["id"]}">'
    f'<span class="dot" aria-hidden="true"></span>'
    f'<span class="stop-name">{e(c["name"])}</span>'
    f'<span class="stop-kind">{e(c["kind"])}</span>'
    f'<span class="stop-status">{STATUS[c["status"]]}</span></a></li>'
    for i, c in enumerate(CASES))

# ---------- work list ----------
def work_row(c):
    visit = ""
    if c["links"]:
        t, h = c["links"][0]
        visit = ext(h, "Visit site" if c["status"] != "client" else "Consulting site", "btn btn-quiet")
    return (f'<li class="row"><div class="row-main"><h3><a href="#case-{c["id"]}">{e(c["name"])}</a></h3>'
            f'<p class="row-line">{e(c["line"])}</p></div>'
            f'<p class="row-kind">{e(c["kind"])}</p>'
            f'<p class="row-status"><span class="pill p-{c["status"]}">{STATUS[c["status"]]}</span></p>'
            f'<p class="row-act"><a class="btn" href="#case-{c["id"]}">Read case study</a>{visit}</p></li>')
work = "".join(work_row(c) for c in CASES)

more = "".join(
    f'<li><h3>{ext(u, n) if u else e(n)}</h3><p>{e(d)}</p><p class="more-status">{e(s)}</p></li>'
    for n, d, s, u in MORE)

exp = "".join(
    f'<li><p class="when">{e(w)}</p><div><h3>{e(r)}</h3><p class="org">{e(o)}, {e(where)}</p><p>{e(d)}</p></div></li>'
    for r, o, w, where, d in EXPERIENCE)
edu = "".join(f'<li><b>{e(a)}</b><span>{e(b)}{", " + e(c) if c else ""}</span></li>' for a, b, c in EDUCATION)
skills = "".join(f'<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>' for a, b in SKILLS)

# goals across the work
goal_map = {}
for c in CASES:
    for n, _ in c["sdgs"]:
        goal_map.setdefault(n, []).append(c)
goals = ""
for n in sorted(goal_map):
    name, col = SDG[n]
    links = ", ".join(f'<a href="#case-{c["id"]}">{e(c["name"])}</a>' for c in goal_map[n])
    goals += (f'<li><span class="sdg-n big" style="background:{col}">{n}</span>'
              f'<div><h3>{e(name)}</h3><p>{links}</p></div></li>')

# ---------- case studies ----------
def case_html(i, c):
    prev = CASES[i - 1]; nxt = CASES[(i + 1) % len(CASES)]
    links = "".join(ext(h, t, "btn" if j == 0 else "btn btn-quiet") for j, (t, h) in enumerate(c["links"]))
    facts = "".join(f'<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>' for a, b in c["facts"])
    stack = "".join(f"<li>{e(s)}</li>" for s in c["stack"])
    secs = "".join(f'<section><h2>{e(h)}</h2>' + "".join(f"<p>{e(p)}</p>" for p in ps) + "</section>"
                   for h, ps in c["sections"])
    sdgs = "".join(sdg_chip(n, note) for n, note in c["sdgs"])
    return f'''<article class="case" id="case-{c["id"]}" hidden aria-labelledby="h-{c["id"]}">
  <header class="case-head s-{c["status"]}">
    <div class="wrap">
      <p class="crumb"><a href="#work">All work</a></p>
      <h1 id="h-{c["id"]}">{e(c["name"])}</h1>
      <p class="case-line">{e(c["line"])}</p>
      <p class="case-meta"><span class="pill p-{c["status"]}">{STATUS[c["status"]]}</span><span>{e(c["kind"])}</span></p>
      <p class="case-links">{links}<button class="btn btn-quiet copy" type="button" data-id="case-{c["id"]}">Copy link</button></p>
    </div>
  </header>
  <div class="wrap case-body">
    <div class="prose">{secs}
      <section class="goals-in-case"><h2>Global Goals this supports</h2>
      <p>The UN Sustainable Development Goals {e(c["name"])} contributes to. It supports these goals; it does not achieve them on its own.</p>
      <ul class="sdgs">{sdgs}</ul></section>
    </div>
    <aside class="facts">
      <dl>{facts}</dl>
      <h2>Built with</h2><ul class="tags">{stack}</ul>
    </aside>
  </div>
  <nav class="wrap pager" aria-label="More case studies">
    <a href="#case-{prev["id"]}"><span>Previous</span>{e(prev["name"])}</a>
    <a href="#case-{nxt["id"]}"><span>Next</span>{e(nxt["name"])}</a>
  </nav>
</article>'''
cases = "\n".join(case_html(i, c) for i, c in enumerate(CASES))

FAV = ("data:image/svg+xml," + "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23F4C20D'/%3E"
       "%3Crect y='22' width='64' height='5' fill='%231C2126'/%3E%3Crect y='37' width='64' height='5' fill='%231C2126'/%3E%3C/svg%3E")

desc = ("Daniel Njoku, software engineer in Lagos. Case studies and live links for Kashfinda, Danfo Code, "
        "Guardsbase, ToonMate, Attestana, Blue Watch Academy, Mantra Worlds and Odoo consulting work.")
ld = {"@context": "https://schema.org", "@type": "ProfilePage", "url": BASE,
      "mainEntity": {"@type": "Person", "name": P["name"], "jobTitle": "Software Engineer",
                     "address": {"@type": "PostalAddress", "addressLocality": "Lagos", "addressCountry": "NG"},
                     "email": "mailto:" + P["email"],
                     "sameAs": [P["linkedin"], P["x"], P["github"], P["odoo_site"]]}}

CSS = (ROOT / "style.css").read_text()
JS = (ROOT / "app.js").read_text()

page = f'''<!DOCTYPE html>
<html lang="en-NG">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Daniel Njoku, software engineer in Lagos</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{BASE}">
<meta name="theme-color" content="#F4C20D">
<link rel="icon" href="{FAV}">
<meta property="og:type" content="profile">
<meta property="og:title" content="Daniel Njoku, software engineer in Lagos">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{BASE}">
<meta property="og:image" content="{BASE}og.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@njokudanielo">
<meta name="twitter:image" content="{BASE}og.png">
<script type="application/ld+json">{json.dumps(ld)}</script>
<style>{FONTS}{CSS}</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <div class="wrap top-in">
    <a class="me" href="#top">Daniel Njoku</a>
    <nav aria-label="Main"><a href="#work">Work</a><a href="#more">More projects</a><a href="#experience">Experience</a><a href="#contact">Contact</a></nav>
    {ext(P["calendly"], "Book a call", "btn btn-small")}
  </div>
</header>
<main id="main">
<div id="home">
  <section class="hero" id="top">
    <div class="wrap">
      <p class="hello">Software engineer in Lagos, Nigeria</p>
      <h1>I build and ship products for fintech, security and learning.</h1>
      <p class="intro">Live platforms on web and mobile, a learning games studio, and almost four years running Azure workloads in production. Each stop below is a product I built. Pick one to see what it does, how I built it and where it stands today.</p>
    </div>
    <div class="route-wrap">
      <div class="wrap"><ul class="route">{stops}</ul></div>
    </div>
  </section>

  <section class="work" id="work" aria-labelledby="work-h">
    <div class="wrap">
      <h2 id="work-h" class="sec">Selected work</h2>
      <ul class="rows">{work}</ul>
    </div>
  </section>

  <section class="more" id="more" aria-labelledby="more-h">
    <div class="wrap">
      <h2 id="more-h" class="sec">More projects</h2>
      <p class="sec-sub">Smaller builds, research and client work. Links appear where there is something public to open.</p>
      <ul class="more-grid">{more}</ul>
    </div>
  </section>

  <section class="exp" id="experience" aria-labelledby="exp-h">
    <div class="wrap exp-grid">
      <div>
        <h2 id="exp-h" class="sec">Experience</h2>
        <ol class="timeline">{exp}</ol>
        <p class="earlier">{e(EARLIER)}</p>
      </div>
      <div>
        <h2 class="sec">Skills</h2>
        <dl class="skills">{skills}</dl>
        <h2 class="sec">Education</h2>
        <ul class="edu">{edu}</ul>
      </div>
    </div>
  </section>

  <section class="goals" id="goals" aria-labelledby="goals-h">
    <div class="wrap">
      <h2 id="goals-h" class="sec">Global Goals in this work</h2>
      <p class="sec-sub">The UN Sustainable Development Goals my products support, and which products support each one. Supporting a goal is not the same as achieving it; each case study explains the link.</p>
      <ul class="goal-list">{goals}</ul>
    </div>
  </section>
</div>

{cases}

<section class="contact" id="contact" aria-labelledby="contact-h">
  <div class="wrap contact-in">
    <div>
      <h2 id="contact-h">Have a product to build or fix?</h2>
      <p>I take on full-stack builds, mobile apps, cloud and security work, and Odoo ERP projects. Tell me what you need and I will reply within one working day.</p>
      <p class="contact-cta">{ext("mailto:" + P["email"], "Email me", "btn btn-ink")}{ext(P["calendly"], "Book a 30-minute call", "btn btn-quiet-ink")}</p>
    </div>
    <dl class="reach">
      <div><dt>Email</dt><dd>{ext("mailto:" + P["email"], P["email"])}</dd></div>
      <div><dt>WhatsApp</dt><dd>{ext(P["wa_link"], P["whatsapp"])}</dd></div>
      <div><dt>LinkedIn</dt><dd>{ext(P["linkedin"], "daniel-njoku")}</dd></div>
      <div><dt>GitHub</dt><dd>{ext(P["github"], "njokdan")}</dd></div>
      <div><dt>X</dt><dd>{ext(P["x"], "@njokudanielo")}</dd></div>
      <div><dt>Odoo consulting</dt><dd>{ext(P["odoo_site"], "njokdan.github.io")}</dd></div>
    </dl>
  </div>
</section>
</main>
<footer class="foot"><div class="wrap"><p>Daniel Njoku, Lagos, Nigeria. Every product on this page links to the live site where one exists; figures are as built, not projected.</p></div></footer>
<div class="toast" role="status" aria-live="polite"></div>
<script>{JS}</script>
</body>
</html>'''

out = ROOT / "site" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(page)
print(out, len(page) // 1024, "KB")
