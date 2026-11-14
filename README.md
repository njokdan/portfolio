# Daniel Njoku portfolio: deploy guide

A static site with one real, indexable page per case study. No build step needed to host it.

## Put it live at https://njokdan.github.io/portfolio/

1. Create a **public** GitHub repo named `portfolio` under `njokdan`.
2. Upload everything in this folder to the repo root (keep the `work/`, `og/` and `assets/` folders).
3. Repo Settings > Pages > Source: "Deploy from a branch", branch `main`, folder `/ (root)`.
4. Wait a minute or two, then open https://njokdan.github.io/portfolio/.

## Tell search engines and AI assistants (one-time, in your njokdan.github.io repo)

Your root `robots.txt` already allows Google, Bing and the AI crawlers. Add this line under the existing Sitemap line:

    Sitemap: https://njokdan.github.io/portfolio/sitemap.xml

Optionally add the portfolio to the root `llms.txt`:

    - [Portfolio and case studies](https://njokdan.github.io/portfolio/llms.txt)

Then in Google Search Console (same njokdan.github.io property), submit `https://njokdan.github.io/portfolio/sitemap.xml`
and use URL Inspection > Request indexing on the home page. In Bing Webmaster Tools, import from Search Console
(this also feeds Copilot and ChatGPT search, which use Bing's index).

## What's in here

- `index.html` home; `work/<name>/index.html` eight case studies, each with its own title, description, canonical URL,
  share image and structured data
- `sitemap.xml`, `llms.txt`, `llms-full.txt` (full text for AI assistants), `site.webmanifest`, icons, `404.html`
- `assets/` CSS, a small script, and self-hosted fonts (no third-party requests, no trackers)

## Moving to your own domain later

Set `BASE_PATH = "/"` in `source/content.py`, run `python3 build.py`, add a `CNAME` file with the domain, and update the
URLs in Search Console.
