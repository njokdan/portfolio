"""Builds two outputs from content.py:
  site/index.html            single-file preview (hash routing, fonts inlined) for the Claude artifact
  dist/portfolio/...         multi-page static site for GitHub Pages, one real URL per case study
"""
import base64, html, json, pathlib, shutil
from content import *

ROOT = pathlib.Path(__file__).parent
FA = ROOT / "node_modules/@fontsource-variable/archivo/files"
FS = ROOT / "node_modules/@fontsource-variable/source-serif-4/files"
LATIN = "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"
LATINEXT = "U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF"
FONTFILES = [  # family, src file, out name, range, style, weight, stretch
    ("Archivo", FA/"archivo-latin-wdth-normal.woff2", "archivo-latin.woff2", LATIN, "normal", "100 900", "62% 125%"),
    ("Archivo", FA/"archivo-latin-ext-wdth-normal.woff2", "archivo-latin-ext.woff2", LATINEXT, "normal", "100 900", "62% 125%"),
    ("Source Serif", FS/"source-serif-4-latin-wght-normal.woff2", "serif-latin.woff2", LATIN, "normal", "200 900", None),
    ("Source Serif", FS/"source-serif-4-latin-ext-wght-normal.woff2", "serif-latin-ext.woff2", LATINEXT, "normal", "200 900", None),
    ("Source Serif", FS/"source-serif-4-latin-wght-italic.woff2", "serif-latin-italic.woff2", LATIN, "italic", "200 900", None),
]
def fontcss(inline):
    out = []
    for fam, src, name, rng, style, wght, wdth in FONTFILES:
        url = f"data:font/woff2;base64,{base64.b64encode(src.read_bytes()).decode()}" if inline else f"fonts/{name}"
        out.append(f"@font-face{{font-family:'{fam}';font-style:{style};font-display:swap;font-weight:{wght};"
                   + (f"font-stretch:{wdth};" if wdth else "") + f"src:url({url}) format('woff2');unicode-range:{rng}}}")
    return "".join(out)

e = html.escape
P = PERSON
SITE = "https://njokdan.github.io" + BASE_PATH
BP = BASE_PATH
STATUS = {"live": "Live", "beta": "Public beta", "building": "In development", "client": "Client work"}
CASE = {c["id"]: c for c in CASES}
for c in CASES: c.update(EXTRA[c["id"]])
FAV_SVG = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='14' fill='#F4C20D'/>"
           "<rect y='22' width='64' height='5' fill='#1C2126'/><rect y='37' width='64' height='5' fill='#1C2126'/></svg>")
FAV_URI = "data:image/svg+xml," + FAV_SVG.replace("<", "%3C").replace(">", "%3E").replace("#", "%23")
BUS = ('<svg class="bus-svg" viewBox="0 0 96 48" aria-hidden="true" focusable="false">'
       '<rect x="4" y="6" width="86" height="32" rx="7" fill="#F4C20D" stroke="#1C2126" stroke-width="3"/>'
       '<rect x="5.5" y="25" width="83" height="3.5" fill="#1C2126"/><rect x="5.5" y="31" width="83" height="3.5" fill="#1C2126"/>'
       '<rect x="12" y="11" width="14" height="10" rx="2" fill="#DCE6EC" stroke="#1C2126" stroke-width="2"/>'
       '<rect x="30" y="11" width="14" height="10" rx="2" fill="#DCE6EC" stroke="#1C2126" stroke-width="2"/>'
       '<rect x="48" y="11" width="14" height="10" rx="2" fill="#DCE6EC" stroke="#1C2126" stroke-width="2"/>'
       '<rect x="68" y="11" width="16" height="15" rx="2" fill="#DCE6EC" stroke="#1C2126" stroke-width="2"/>'
       '<circle cx="24" cy="39" r="6.5" fill="#1C2126"/><circle cx="24" cy="39" r="2.5" fill="#CBD0D3"/>'
       '<circle cx="72" cy="39" r="6.5" fill="#1C2126"/><circle cx="72" cy="39" r="2.5" fill="#CBD0D3"/></svg>')

def ext(href, text, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<a{c} href="{e(href)}" target="_blank" rel="noopener">{e(text)}</a>'

class Links:
    def __init__(s, single): s.single = single
    def case(s, cid): return f"#case-{cid}" if s.single else f"{BP}work/{cid}/"
    def home(s, anchor=""): return (f"#{anchor}" if anchor else "#top") if s.single else f"{BP}{'#' + anchor if anchor else ''}"

def sdg_chip(n, note=None):
    name, col = SDG[n]
    return (f'<li class="sdg"><span class="sdg-n" style="background:{col}">{n}</span><span><b>Goal {n}: {e(name)}</b>'
            + (f'<span class="sdg-note">{e(note)}</span>' if note else "") + "</span></li>")

def heading(h, name): return QUESTION_HEADINGS.get(h, h).format(name=name)

# ---------------- structured data ----------------
PERSON_ID = SITE + "#person"
def person_full():
    return {"@type": "Person", "@id": PERSON_ID, "name": P["name"], "url": SITE,
            "image": SITE + "og.png", "jobTitle": "Software Engineer",
            "description": FAQ[0][1], "email": "mailto:" + P["email"], "telephone": "+2348094451628",
            "address": {"@type": "PostalAddress", "addressLocality": "Lagos", "addressCountry": "NG"},
            "nationality": {"@type": "Country", "name": "Nigeria"},
            "worksFor": {"@type": "Organization", "name": "Infoassure Limited"},
            "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Institute of Management and Technology, Enugu"},
                         {"@type": "Organization", "name": "Udacity"}],
            "knowsAbout": ["Software engineering", "Full-stack web development", "Mobile app development", "React Native",
                           "Next.js", "Python", "TypeScript", "Microsoft Azure", "Cloud infrastructure", "DevOps",
                           "Cybersecurity", "Governance, risk and compliance", "Nigeria Data Protection Act",
                           "Odoo ERP", "Payroll systems", "Fintech", "Educational games", "Deepfake detection"],
            "sameAs": [P["linkedin"], P["x"], P["github"], P["odoo_site"]]}
PERSON_REF = {"@id": PERSON_ID, "@type": "Person", "name": P["name"], "url": SITE}

def ld_home():
    g = [{"@type": "WebSite", "@id": SITE + "#website", "url": SITE, "name": "Daniel Njoku", "inLanguage": "en",
          "publisher": {"@id": PERSON_ID}},
         {"@type": "ProfilePage", "@id": SITE + "#page", "url": SITE, "name": "Daniel Njoku, software engineer in Lagos, Nigeria",
          "isPartOf": {"@id": SITE + "#website"}, "mainEntity": {"@id": PERSON_ID},
          "dateModified": UPDATED, "primaryImageOfPage": SITE + "og.png", "inLanguage": "en"},
         person_full(),
         {"@type": "Organization", "name": "Mantra Worlds", "url": "https://mantraworlds.com", "founder": {"@id": PERSON_ID}},
         {"@type": "ItemList", "name": "Case studies by Daniel Njoku",
          "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{SITE}work/{c['id']}/", "name": c["name"]}
                              for i, c in enumerate(CASES)]},
         {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q,
                                              "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}]
    return {"@context": "https://schema.org", "@graph": g}

def ld_case(c):
    url = f"{SITE}work/{c['id']}/"
    live = c["links"][0][1] if c["links"] and c["status"] != "client" else None
    thing = {"@id": url + "#subject", "name": c["name"], "description": c["line"]}
    if c["schema"] == "SoftwareApplication":
        thing.update({"@type": "SoftwareApplication", "applicationCategory": c["cat"], "operatingSystem": c["os"],
                      "creator": {"@id": PERSON_ID}})
        if c["id"] == "danfo-code":
            thing.update({"isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "NGN"}})
    elif c["schema"] == "Organization":
        thing.update({"@type": "Organization", "founder": {"@id": PERSON_ID}})
    else:
        thing.update({"@type": "CreativeWork", "creator": {"@id": PERSON_ID}})
    if live: thing["url"] = live
    article = {"@type": "Article", "@id": url + "#article", "headline": c["title"].split(" | ")[0],
               "description": c["desc"], "author": PERSON_REF, "publisher": PERSON_REF,
               "datePublished": UPDATED, "dateModified": UPDATED, "image": f"{SITE}og/{c['id']}.png",
               "mainEntityOfPage": url, "about": {"@id": url + "#subject"}, "inLanguage": "en",
               "keywords": ", ".join(c["stack"])}
    crumbs = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Daniel Njoku", "item": SITE},
        {"@type": "ListItem", "position": 2, "name": "Work", "item": SITE + "#work"},
        {"@type": "ListItem", "position": 3, "name": c["name"], "item": url}]}
    return {"@context": "https://schema.org", "@graph": [article, thing, crumbs, PERSON_REF]}

def jsonld(obj): return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace("</", "<\\/") + "</script>"

# ---------------- page parts ----------------
HOME_TITLE = "Daniel Njoku, software engineer in Lagos, Nigeria"
HOME_DESC = ("Daniel Njoku is a Lagos software engineer building web, mobile, cloud and security products. "
             "Live links and case studies: Kashfinda, Danfo Code and more.")

def head(title, desc, url, img, ld, inline_css, extra=""):
    if inline_css is not None:
        css = f"<style>{inline_css}</style>"; icon = f'<link rel="icon" href="{FAV_URI}">'
    else:
        css = (f'<link rel="preload" href="{BP}assets/fonts/archivo-latin.woff2" as="font" type="font/woff2" crossorigin>'
               f'<link rel="stylesheet" href="{BP}assets/site.css">')
        icon = (f'<link rel="icon" href="{BP}favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="{BP}apple-touch-icon.png">'
                f'<link rel="manifest" href="{BP}site.webmanifest"><link rel="alternate" type="text/plain" title="LLM summary" href="{BP}llms.txt">')
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="author" content="Daniel Njoku">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#F4C20D">
{icon}
<meta property="og:site_name" content="Daniel Njoku">
<meta property="og:locale" content="en_NG">
<meta property="og:type" content="{'profile' if url == SITE else 'article'}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(title)}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@njokudanielo"><meta name="twitter:creator" content="@njokudanielo">
<meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(desc)}"><meta name="twitter:image" content="{img}">
{extra}{jsonld(ld)}
{css}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>'''

def topbar(L):
    avail = "Open to projects and remote roles" if OPEN_TO_ROLES else "Taking on new projects"
    return f'''<header class="top">
  <div class="wrap top-in">
    <a class="me" href="{L.home()}">Daniel Njoku</a>
    <span class="avail"><span aria-hidden="true"></span>{avail}</span>
    <nav aria-label="Main"><a href="{L.home('work')}">Work</a><a href="{L.home('services')}">Services</a><a href="{L.home('experience')}">Experience</a><a href="{L.home('faq')}">FAQ</a></nav>
    <a class="btn btn-small" href="{L.home('contact')}">Let's talk</a>
  </div>
</header>'''

def home_body(L):
    stops = "".join(
        f'<li class="stop s-{c["status"]}" style="--i:{i}"><a href="{L.case(c["id"])}">'
        f'<span class="dot" aria-hidden="true"></span><span class="stop-name">{e(c["name"])}</span>'
        f'<span class="stop-kind">{e(c["kind"])}</span><span class="stop-status">{STATUS[c["status"]]}</span></a></li>'
        for i, c in enumerate(CASES))
    proof = "".join(f'<li><b>{e(n)}</b><span>{e(t)}</span></li>' for n, t in PROOF)
    def row(c):
        visit = ext(c["links"][0][1], "Visit site" if c["status"] != "client" else "Consulting site", "btn btn-quiet") if c["links"] else ""
        return (f'<li class="row"><div class="row-main"><h3><a href="{L.case(c["id"])}">{e(c["name"])}</a></h3>'
                f'<p class="row-line">{e(c["line"])}</p></div><p class="row-kind">{e(c["kind"])}</p>'
                f'<p class="row-status"><span class="pill p-{c["status"]}">{STATUS[c["status"]]}</span></p>'
                f'<p class="row-act"><a class="btn" href="{L.case(c["id"])}" aria-label="Read case study: {e(c["name"])}">Read case study</a>{visit}</p></li>')
    work = "".join(row(c) for c in CASES)
    why = "".join(f'<li><h3>{e(h)}</h3><p>{e(t)}</p><a href="{L.case(cid)}">See {e(CASE[cid]["name"])}</a></li>' for h, t, cid in WHY)
    serv = "".join(f'<li><h3>{e(h)}</h3><p>{e(t)}</p>'
                   + (f'<a href="{L.case(cid)}">Example: {e(CASE[cid]["name"])}</a>' if cid else ext(P["odoo_site"], "Odoo consulting site"))
                   + "</li>" for h, t, cid in SERVICES)
    proc = "".join(f'<li><span class="step" aria-hidden="true">{i+1}</span><div><h3>{e(h)}</h3><p>{e(t)}</p></div></li>' for i, (h, t) in enumerate(PROCESS))
    more = "".join(f'<li><h3>{ext(u, n) if u else e(n)}</h3><p>{e(d)}</p><p class="more-status">{e(s)}</p></li>' for n, d, s, u in MORE)
    exp = "".join(f'<li><p class="when">{e(w)}</p><div><h3>{e(r)}</h3><p class="org">{e(o)}, {e(wh)}</p><p>{e(d)}</p></div></li>'
                  for r, o, w, wh, d in EXPERIENCE)
    edu = "".join(f'<li><b>{e(a)}</b><span>{e(b)}{", " + e(c) if c else ""}</span></li>' for a, b, c in EDUCATION)
    skills = "".join(f'<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>' for a, b in SKILLS)
    gm = {}
    for c in CASES:
        for n, _ in c["sdgs"]: gm.setdefault(n, []).append(c)
    goals = "".join(f'<li><span class="sdg-n big" style="background:{SDG[n][1]}">{n}</span><div><h3>{e(SDG[n][0])}</h3><p>'
                    + ", ".join(f'<a href="{L.case(c["id"])}">{e(c["name"])}</a>' for c in gm[n]) + "</p></div></li>" for n in sorted(gm))
    faq = "".join(f'<div class="faq-item"><h3>{e(q)}</h3><p>{e(a)}</p></div>' for q, a in FAQ)
    return f'''<div id="home">
  <section class="hero" id="top" aria-labelledby="hero-h">
    <div class="wrap">
      <p class="hello">{e(HERO["hello"])}</p>
      <h1 id="hero-h">{e(HERO["h1"])}</h1>
      <p class="intro">{e(HERO["intro"])}</p>
      <p class="hero-cta"><a class="btn btn-ink" href="{L.home('contact')}">Start a project</a><a class="btn btn-quiet" href="{L.home('work')}">See my work</a></p>
    </div>
    <div class="route-wrap">
      <div class="wrap">
        <p class="route-hint">{e(HERO["route_hint"])}</p>
        <div class="route-track"><div class="bus" aria-hidden="true">{BUS}</div><ul class="route" aria-label="Products I built">{stops}</ul></div>
      </div>
    </div>
  </section>

  <section class="proof-band" aria-label="At a glance">
    <div class="wrap"><ul class="proof">{proof}</ul></div>
  </section>

  <section class="work" id="work" aria-labelledby="work-h">
    <div class="wrap">
      <h2 id="work-h" class="sec">Things I've built and shipped</h2>
      <p class="sec-sub">Each one links to the live product where there is one, and to a case study that explains the problem, the build and where it stands.</p>
      <ul class="rows">{work}</ul>
    </div>
  </section>

  <section class="why" aria-labelledby="why-h">
    <div class="wrap">
      <h2 id="why-h" class="sec">Why people work with me</h2>
      <ul class="why-list">{why}</ul>
    </div>
  </section>

  <section class="services" id="services" aria-labelledby="serv-h">
    <div class="wrap serv-grid">
      <div>
        <h2 id="serv-h" class="sec">How I can help</h2>
        <ul class="serv-list">{serv}</ul>
      </div>
      <div class="process">
        <h2 class="sec">How we'd work together</h2>
        <ol class="proc-list">{proc}</ol>
        <p><a class="btn btn-ink" href="{L.home('contact')}">Book the free call</a></p>
      </div>
    </div>
  </section>

  <section class="more" id="more" aria-labelledby="more-h">
    <div class="wrap">
      <h2 id="more-h" class="sec">Also on my workbench</h2>
      <p class="sec-sub">Smaller builds, research and client work. Links appear where there's something public to open.</p>
      <ul class="more-grid">{more}</ul>
    </div>
  </section>

  <section class="exp" id="experience" aria-labelledby="exp-h">
    <div class="wrap exp-grid">
      <div>
        <h2 id="exp-h" class="sec">Where I've worked</h2>
        <ol class="timeline">{exp}</ol>
        <p class="earlier">{e(EARLIER)}</p>
      </div>
      <div>
        <h2 class="sec">What I work with</h2>
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

  <section class="faq" id="faq" aria-labelledby="faq-h">
    <div class="wrap">
      <h2 id="faq-h" class="sec">Questions people ask</h2>
      <div class="faq-list">{faq}</div>
    </div>
  </section>
</div>'''

def case_article(i, c, L, single):
    prev = CASES[i - 1]; nxt = CASES[(i + 1) % len(CASES)]
    links = "".join(ext(h, t, "btn" if j == 0 else "btn btn-quiet") for j, (t, h) in enumerate(c["links"]))
    facts = "".join(f'<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>' for a, b in c["facts"])
    stack = "".join(f"<li>{e(s)}</li>" for s in c["stack"])
    secs = "".join(f'<section><h2>{e(heading(h, c["name"]))}</h2>' + "".join(f"<p>{e(p)}</p>" for p in ps) + "</section>"
                   for h, ps in c["sections"])
    sdgs = "".join(sdg_chip(n, note) for n, note in c["sdgs"])
    attrs = f'id="case-{c["id"]}" hidden' if single else f'id="case-{c["id"]}"'
    crumb = (f'<nav class="crumb" aria-label="Breadcrumb"><ol><li><a href="{L.home()}">Home</a></li>'
             f'<li><a href="{L.home("work")}">Work</a></li><li aria-current="page">{e(c["name"])}</li></ol></nav>')
    mail = f"mailto:{P['email']}?subject={e(c['name'])}%20enquiry"
    return f'''<article class="case" {attrs} aria-labelledby="h-{c["id"]}">
  <header class="case-head s-{c["status"]}">
    <div class="wrap">
      {crumb}
      <h1 id="h-{c["id"]}">{e(c["name"])}</h1>
      <p class="case-line">{e(c["line"])}</p>
      <p class="case-meta"><span class="pill p-{c["status"]}">{STATUS[c["status"]]}</span><span>{e(c["kind"])}</span><span>Updated <time datetime="{UPDATED}">{UPDATED_HUMAN}</time></span></p>
      <p class="case-links">{links}<button class="btn btn-quiet copy" type="button" data-id="{c["id"]}">Copy link</button></p>
    </div>
  </header>
  <div class="wrap case-body">
    <div class="prose">
      <section class="tldr" aria-label="Summary"><h2>In short</h2><p>{e(c["tldr"])}</p></section>
      {secs}
      <section class="goals-in-case"><h2>Global Goals {e(c["name"])} supports</h2>
      <p>The UN Sustainable Development Goals this work contributes to. It supports these goals; it does not achieve them on its own.</p>
      <ul class="sdgs">{sdgs}</ul></section>
      <aside class="case-cta" aria-label="Work with me">
        <h2>{e(c["cta"])}</h2>
        <p>I'd love to hear what you're building. Tell me the problem and I'll reply within one working day.</p>
        <p class="contact-cta">{ext(mail, "Email me about it", "btn btn-ink")}{ext(P["wa_link"], "Chat on WhatsApp", "btn btn-quiet-ink")}</p>
      </aside>
    </div>
    <aside class="facts" aria-label="Key facts">
      <h2>Key facts</h2>
      <dl>{facts}</dl>
      <h2>Built with</h2><ul class="tags">{stack}</ul>
    </aside>
  </div>
  <nav class="wrap pager" aria-label="More case studies">
    <a href="{L.case(prev["id"])}"><span>Previous</span>{e(prev["name"])}</a>
    <a href="{L.case(nxt["id"])}"><span>Next</span>{e(nxt["name"])}</a>
  </nav>
</article>'''

def contact(L):
    roles = (" Hiring for a remote role? I'm open to the right full-time position too." if OPEN_TO_ROLES else "")
    return f'''<section class="contact" id="contact" aria-labelledby="contact-h">
  <div class="wrap contact-in">
    <div>
      <h2 id="contact-h">Got a problem worth solving? Let's build it.</h2>
      <p>New product, a rescue job, a mobile app, cloud and security work, or Odoo ERP. Tell me what you need and I'll reply within one working day.{roles}</p>
      <p class="contact-cta">{ext("mailto:" + P["email"] + "?subject=Project%20enquiry", "Email me", "btn btn-ink")}{ext(P["calendly"], "Book a free 30-minute call", "btn btn-quiet-ink")}</p>
    </div>
    <dl class="reach">
      <div><dt>Email</dt><dd>{ext("mailto:" + P["email"], P["email"])}</dd></div>
      <div><dt>WhatsApp</dt><dd>{ext(P["wa_link"], P["whatsapp"])}</dd></div>
      <div><dt>LinkedIn</dt><dd>{ext(P["linkedin"], "Daniel Njoku")}</dd></div>
      <div><dt>GitHub</dt><dd>{ext(P["github"], "njokdan")}</dd></div>
      <div><dt>X</dt><dd>{ext(P["x"], "@njokudanielo")}</dd></div>
      <div><dt>Odoo consulting</dt><dd>{ext(P["odoo_site"], "njokdan.github.io")}</dd></div>
    </dl>
  </div>
</section>'''

def footer(L):
    return (f'<footer class="foot"><div class="wrap foot-in"><p>Daniel Njoku, software engineer in Lagos, Nigeria. '
            f'Figures on this site are as built, not projected. Last updated <time datetime="{UPDATED}">{UPDATED_HUMAN}</time>.</p>'
            + ("" if L.single else f'<p><a href="{BP}llms.txt">llms.txt</a><a href="{BP}sitemap.xml">Sitemap</a></p>')
            + '</div></footer><div class="toast" role="status" aria-live="polite"></div>')

CSS = (ROOT / "style.css").read_text()
JS = (ROOT / "app.js").read_text()

# ---------------- single-file preview ----------------
def build_single():
    L = Links(True)
    cases = "\n".join(case_article(i, c, L, True) for i, c in enumerate(CASES))
    page = (head(HOME_TITLE, HOME_DESC, SITE, SITE + "og.png", ld_home(), fontcss(True) + CSS)
            + topbar(L) + f'<main id="main">{home_body(L)}\n{cases}\n{contact(L)}</main>' + footer(L)
            + f'<script>window.PF={{single:true,site:"{SITE}"}};{JS}</script></body></html>')
    out = ROOT / "site/index.html"; out.parent.mkdir(exist_ok=True); out.write_text(page)
    return out

# ---------------- multi-page deploy ----------------
def build_multi():
    L = Links(False)
    D = ROOT / "dist" / BP.strip("/")
    if D.exists(): shutil.rmtree(D)
    (D / "assets/fonts").mkdir(parents=True)
    for _, src, name, *_ in FONTFILES: shutil.copy(src, D / "assets/fonts" / name)
    (D / "assets/site.css").write_text(fontcss(False) + CSS)
    (D / "assets/app.js").write_text(JS)
    script = f'<script>window.PF={{single:false,site:"{SITE}"}};</script><script src="{BP}assets/app.js" defer></script>'
    pages = {"": head(HOME_TITLE, HOME_DESC, SITE, SITE + "og.png", ld_home(), None)
                 + topbar(L) + f'<main id="main">{home_body(L)}{contact(L)}</main>' + footer(L) + script + "</body></html>"}
    for i, c in enumerate(CASES):
        url = f"{SITE}work/{c['id']}/"
        pages[f"work/{c['id']}/"] = (head(c["title"], c["desc"], url, f"{SITE}og/{c['id']}.png", ld_case(c), None)
                                     + topbar(L) + f'<main id="main">{case_article(i, c, L, False)}{contact(L)}</main>'
                                     + footer(L) + script + "</body></html>")
    for path, html_ in pages.items():
        p = D / path / "index.html"; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(html_)
    # 404
    nf = (head("Page not found | Daniel Njoku", "This page doesn't exist. Head back to Daniel Njoku's portfolio.", SITE, SITE + "og.png",
               {"@context": "https://schema.org", "@type": "WebPage", "name": "Not found"}, None,
               extra='<meta name="robots" content="noindex">\n')
          + topbar(L) + f'<main id="main" class="nf"><div class="wrap"><h1>Wrong stop.</h1><p>That page isn\'t on this route. '
          f'Try the <a href="{BP}">home page</a> or one of the case studies.</p><ul>'
          + "".join(f'<li><a href="{L.case(c["id"])}">{e(c["name"])}</a></li>' for c in CASES)
          + "</ul></div></main>" + footer(L) + "</body></html>")
    (D / "404.html").write_text(nf)
    (D / "favicon.svg").write_text(FAV_SVG)
    (D / "site.webmanifest").write_text(json.dumps({"name": "Daniel Njoku", "short_name": "Daniel Njoku", "start_url": BP,
        "scope": BP, "display": "browser", "background_color": "#F3F4F1", "theme_color": "#F4C20D",
        "icons": [{"src": BP + "favicon.svg", "sizes": "any", "type": "image/svg+xml"},
                  {"src": BP + "apple-touch-icon.png", "sizes": "180x180", "type": "image/png"},
                  {"src": BP + "icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=2))
    # sitemap
    urls = [(SITE, SITE + "og.png", "1.0")] + [(f"{SITE}work/{c['id']}/", f"{SITE}og/{c['id']}.png", "0.8") for c in CASES]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
    for u, img, pr in urls:
        sm.append(f"  <url><loc>{u}</loc><lastmod>{UPDATED}</lastmod><changefreq>monthly</changefreq><priority>{pr}</priority>"
                  f"<image:image><image:loc>{img}</image:loc></image:image></url>")
    sm.append("</urlset>")
    (D / "sitemap.xml").write_text("\n".join(sm) + "\n")
    # llms.txt (llmstxt.org format) and llms-full.txt
    ll = [f"# Daniel Njoku", "", f"> {FAQ[0][1]}", "",
          f"Location: Lagos, Nigeria. Contact: {P['email']}, WhatsApp {P['whatsapp']}. Last updated {UPDATED}.", "",
          "## Case studies", ""]
    ll += [f"- [{c['name']}]({SITE}work/{c['id']}/): {c['tldr']}" for c in CASES]
    ll += ["", "## Live products", ""]
    ll += [f"- [{c['name']}]({c['links'][0][1]}): {STATUS[c['status']]}" for c in CASES if c["links"] and c["status"] in ("live", "beta")]
    ll += ["", "## Profiles", "", f"- [LinkedIn]({P['linkedin']})", f"- [GitHub]({P['github']})", f"- [X]({P['x']})",
           f"- [Odoo consulting]({P['odoo_site']})", "", "## Optional", "", f"- [Full text of every case study]({SITE}llms-full.txt)", ""]
    (D / "llms.txt").write_text("\n".join(ll))
    full = [f"# Daniel Njoku, software engineer in Lagos, Nigeria", "", f"Last updated {UPDATED}. Canonical: {SITE}", "",
            HERO["h1"], "", HERO["intro"], "", "## Frequently asked questions", ""]
    for q, a in FAQ: full += [f"### {q}", "", a, ""]
    full += ["## Experience", ""] + [f"- {r}, {o} ({w}, {wh}): {d}" for r, o, w, wh, d in EXPERIENCE] + [f"- {EARLIER}", ""]
    full += ["## Skills", ""] + [f"- {a}: {b}" for a, b in SKILLS] + [""]
    full += ["## Education", ""] + [f"- {a}, {b}{', ' + c if c else ''}" for a, b, c in EDUCATION] + [""]
    for c in CASES:
        full += [f"## {c['name']}: {c['kind']}", "", f"URL: {SITE}work/{c['id']}/", f"Status: {STATUS[c['status']]}"]
        full += [f"Link: {h}" for _, h in c["links"]]
        full += ["", c["tldr"], ""] + [f"- {a}: {b}" for a, b in c["facts"]] + [f"- Built with: {', '.join(c['stack'])}", ""]
        for h, ps in c["sections"]: full += [f"### {heading(h, c['name'])}", ""] + sum([[p, ""] for p in ps], [])
        full += ["### UN Sustainable Development Goals supported", ""] + [f"- Goal {n} ({SDG[n][0]}): {note}" for n, note in c["sdgs"]] + [""]
    full += ["## More projects", ""] + [f"- {n} ({s}): {d}" for n, d, s, u in MORE] + [""]
    (D / "llms-full.txt").write_text("\n".join(full))
    (D / "README.md").write_text((ROOT / "README.deploy.md").read_text())
    G = ROOT / "generated"
    if G.exists(): shutil.copytree(G, D, dirs_exist_ok=True)
    return D, pages

if __name__ == "__main__":
    s = build_single(); D, pages = build_multi()
    print(s, s.stat().st_size // 1024, "KB;", D, len(pages), "pages")
    for c in CASES:
        assert len(c["title"]) <= 60, (c["title"], len(c["title"]))
        assert 110 <= len(c["desc"]) <= 160, (c["id"], len(c["desc"]))
    assert len(HOME_TITLE) <= 60 and len(HOME_DESC) <= 160, (len(HOME_TITLE), len(HOME_DESC))
    print("meta lengths ok")
