# Christoforos Kapsalis - personal website

This repository contains the source for my personal website,
https://c-kapsalis.github.io/, built with Sphinx and Furo. GitHub Actions
builds and deploys the site from the main branch using
.github/workflows/docs.yml.

## Build locally

Install the packages listed in requirements.txt, then run:

    make html
    make serve

The built site is written to docs/_build/html/; the local server listens on
port 8000.

## Publish

Push to main or run the Deploy portfolio workflow manually. The workflow
builds the Sphinx documentation and deploys it to GitHub Pages.
