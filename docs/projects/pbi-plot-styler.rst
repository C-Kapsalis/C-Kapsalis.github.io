
pbi-plot-styler
===============

**A Power BI reporting template you can argue for, with a formatter that
enforces it, documented end to end.** pbi-plot-styler is a small open-source
Python CLI that makes Power BI combo charts presentation-ready: it reads the
measures a semantic model declares in its *field-parameter* tables and
deterministically rebuilds every chart's line color, data labels and
data-label backgrounds, so that any metric anyone adds to the model comes out
styled for a deck with one command. I built the tool and its documentation
together. Its central claim, that per-measure formatting in Power BI is a
derived artifact that should be regenerated from the model and never
maintained by hand, is argued in prose as deliberately as it is enforced in
code.

The documentation is deliberately lean and deliberately Diátaxis-shaped, one
document per reader need rather than one per feature:

- **A README that evangelizes rather than lists.** Most CLI READMEs open
  with installation; this one opens with a failure mode, the twenty-page
  report where every page is the same chart with a different measure, and
  argues for a pattern: declare your dimensions and measures in three field
  parameters, drive one combo-chart page from slicers and bookmarks, and let
  a tool own the formatting. The CLI is positioned as the last mile of a
  template, not as the product.
- **One tutorial** (*Getting started*) that walks a fictional
  specialty-coffee roastery from an empty model to styled charts: the three
  field-parameter tables as ready-to-paste TMDL, the combo-chart page, a
  dry-run diff, the apply, and the idempotent re-run that proves the tool
  safe to habituate.
- **One reference page** for the CLI: every argument, option, and config key
  with its default; the exact JSON properties the tool rewrites, plus the
  guarantee that everything else in the file is preserved byte for byte down
  to line endings and the end-of-file convention; the exit codes, including
  the dry-run drift code that turns the style guide into a CI check; and why
  formatting must be enforced by regeneration rather than discipline, folded
  in as reference sections (CI usage, brand palettes, the one Power BI quirk
  that makes a shared measure catalog worth naming) rather than spun into
  standalone pages a three-flag tool does not need.

The project doubles as a demonstration of a documentation belief of mine:
that a tool with a strong opinion deserves documentation sized to its
surface, not to a template. Two documents and a README cover the whole
tool; nothing is written twice, and nothing is split into its own page
just because a bigger project would have split it.

What 1.1.0 added
----------------

Version 1.1.0 fixed the tool's most important promise and added a second job.

- **It only touches what it owns.** Earlier versions rebuilt every chart's
  formatting arrays from scratch, so a hand-picked column color or a hidden
  legend series disappeared on the next run. The styler now rewrites only the
  per-measure entries it is responsible for and keeps everything else byte
  for byte. Colors are also tied to each measure's position in the field
  parameter, so adding a metric no longer repaints the others, and they can
  come from the report theme instead of hard-coded hex values.
- **It checks the report, not just the styling.** A new read-only ``check``
  command finds the defects that let a report save cleanly and then fail:
  visuals and bookmarks bound to measures that no longer exist, bookmark
  options that the Power BI service rejects on import, bookmarks pointing at
  missing pages or visuals, and overlapping field-parameter slots. Each
  finding has a stable id, so the reference can say exactly what each one
  means and how to fix it, and a baseline lets a team adopt the check on a
  report that already has known findings.

The documentation grew with it, but in place: the new command and every
check id went into the one CLI reference page and the tutorial, rather than
into new pages a two-command tool does not need.

Project links
-------------

- `pbi-plot-styler repository on GitHub
  <https://github.com/c-kapsalis/pbi-plot-styler>`_: source code, release
  notes, and the `v1.1.0 release
  <https://github.com/C-Kapsalis/pbi-plot-styler/releases/tag/v1.1.0>`_.
- `Documentation site
  <https://pbi-plot-styler-documentation.readthedocs.io/en/latest/>`_:
  the published docs, on Read the Docs.

The documentation lives in its own repository and is published on Read
the Docs; this page introduces the project, not the docs themselves.

*Python ≥ 3.10; 93 passing tests; MIT license.*
