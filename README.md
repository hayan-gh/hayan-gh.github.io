# Hayan Aljabr

Personal site for Hayan Aljabr, a software engineer in Damascus. It is a static site: HTML, CSS, and a small script for the light/dark control. No build step.

## Run locally

From this directory:

```bash
python3 -m http.server 8741
```

Open [http://127.0.0.1:8741](http://127.0.0.1:8741).

## CV

`cv/Hayan_Aljabr_CV_EN.pdf` is the file behind the Download CV button. Regenerate it with:

```bash
python3 scripts/build_cv_pdf.py
```

That script needs [fpdf2](https://pypi.org/project/fpdf2/). The public PDF does not include a phone number.

## Deploy to GitHub Pages

The workflow in `.github/workflows/pages.yml` publishes the repository root to GitHub Pages on every push to `main`.

1. In the repository on GitHub, open **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to **GitHub Actions**.
3. Push to `main`. The **Deploy to GitHub Pages** workflow publishes the site.

The site will be at `https://<user>.github.io/<repository>/`. If the site is served from a project subpath rather than the domain root, links in this repo are relative, so pages, the stylesheet, and the CV still resolve.

## Fonts

Space Grotesk, Inter, JetBrains Mono, and Noto Serif are used for the Latin text on the site and are under the SIL Open Font License, Version 1.1. See `assets/fonts/OFL.txt`.
