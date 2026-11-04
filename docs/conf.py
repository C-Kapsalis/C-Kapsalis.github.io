"""Sphinx configuration for the technical-writing portfolio."""

project = "Christoforos Kapsalis"
author = "Christoforos Kapsalis"
copyright = "2026, Christoforos Kapsalis"

extensions = ["sphinx_sitemap"]

templates_path = ["_templates"]
html_static_path = ["_static"]
# Served from the site root: Search Console verification and robots.txt.
html_extra_path = ["_extra"]

# The site is the GitHub Pages user site, served from the domain root.
html_baseurl = "https://c-kapsalis.github.io/"
sitemap_url_scheme = "{link}"
html_js_files = ["new-tab.js"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Furo: a clean, modern, responsive theme that reads well on mobile.
html_theme = "furo"
html_title = "Christoforos Kapsalis"

html_theme_options = {
    "sidebar_hide_name": False,
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/c-kapsalis",
            "html": "",
            "class": "fa-brands fa-github",
        },
    ],
}

# So dead internal links fail the build rather than shipping broken.
nitpicky = False


# The site used to live at /writing-portfolio/. Keep those links working by
# writing a redirect page for every document under that old prefix.
OLD_PREFIX = "writing-portfolio"


def _write_old_url_redirects(app, exception):
    import shutil
    from pathlib import Path

    if exception or app.builder.name != "html":
        return
    out = Path(app.outdir)
    old = out / OLD_PREFIX
    for docname in app.env.found_docs:
        target = html_baseurl + app.builder.get_target_uri(docname)
        stub = old / f"{docname}.html"
        stub.parent.mkdir(parents=True, exist_ok=True)
        stub.write_text(
            "<!doctype html><meta charset=\"utf-8\">"
            f"<link rel=\"canonical\" href=\"{target}\">"
            f"<meta http-equiv=\"refresh\" content=\"0; url={target}\">"
            f"<title>Moved</title><a href=\"{target}\">{target}</a>\n",
            encoding="utf-8",
        )
    # Downloads (the CV PDF) are copied, since a file cannot redirect itself.
    if (out / "_downloads").is_dir():
        shutil.copytree(out / "_downloads", old / "_downloads", dirs_exist_ok=True)


# Google Search Console ownership (HTML tag method), on every page.
GOOGLE_SITE_VERIFICATION = "vw_0BeUanpg7IqBop3_lYu5jjRJ4iEb770lZWUv5XIY"


def _add_site_verification(app, pagename, templatename, context, doctree):
    context["metatags"] = context.get("metatags", "") + (
        f'\n<meta name="google-site-verification" '
        f'content="{GOOGLE_SITE_VERIFICATION}" />'
    )


# Google Analytics 4 (gtag.js), in the <head> of every page.
GA4_MEASUREMENT_ID = "G-YP0MFY3YTG"


def _add_ga4(app, pagename, templatename, context, doctree):
    context["metatags"] = context.get("metatags", "") + f"""
<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_MEASUREMENT_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA4_MEASUREMENT_ID}');
</script>"""


def setup(app):
    app.connect("html-page-context", _add_site_verification)
    app.connect("html-page-context", _add_ga4)
    app.connect("build-finished", _write_old_url_redirects)
