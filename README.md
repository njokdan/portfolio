# Daniel Njoku portfolio

Static, single-file site. No build step, no trackers, fonts embedded.

## Deploy to GitHub Pages at njokdan.github.io/portfolio/

1. Create a public repo named `portfolio` under njokdan.
2. Add `index.html`, `og.png` and `404.html` (copy of index.html) to the root.
3. Settings > Pages > Source: Deploy from a branch, `main`, folder `/ (root)`.
4. It goes live at https://njokdan.github.io/portfolio/ in a minute or two.
   Your Odoo site at njokdan.github.io is untouched.

Case studies have shareable links: #case-kashfinda, #case-danfo-code, #case-guardsbase,
#case-toonmate, #case-attestana, #case-blue-watch, #case-mantra-worlds, #case-payroll-audit.

## Editing
Content lives in content.py; run `python3 build.py` to regenerate index.html
(needs the two @fontsource-variable packages from npm for the embedded fonts).
