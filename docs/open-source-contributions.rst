Open-source contributions
=========================

**Diátaxis: documentation typo fix.** A small fix to the documentation of the
Diátaxis framework itself, the very framework I use to structure my own
documentation. Modest in size, but it took me through the project's
contribution workflow end to end and, more usefully, made me read the source
material closely.
`Pull request #164 <https://github.com/evildmp/diataxis-documentation-framework/pull/164>`_.

**Canonical robotics documentation: making labels carry meaning.**
Canonical's robotics documentation site is split into four kinds of content:
tutorials, how-to guides, explanations, and reference material. I made two
changes to it. The first rewrote the homepage's one-line description of each
content type so it was actually accurate. The second replaced a
set of internal links that silently break whenever a page gets renamed or
moved with stable, named references instead, and gave those names a
consistent scheme, since the project had only handed me a single example to
extend.

That naming scheme is the interesting part. A page that lists every tutorial
on a given topic gets a name ending in "learning-roadmap," because that is
what it is to a reader: an overview to plan a path from. The specific
tutorial it points to instead gets a name ending in "getting-started,"
because that is where someone actually begins doing the task. An
explanation page never needs that split — each one is a self-contained
discussion of a single topic, not a step in a sequence — so every
explanation gets the same ending instead: "topic-guide." A how-to guide got
no special ending at all: a label like
``how-tos-packaging-ros-2-shared-memory-in-snaps`` is just its folder,
subfolder, and page name, because each how-to guide is already a complete,
self-contained task with nothing left to tell apart. Knowing where a real
distinction existed, and where it didn't, mattered as much as inventing the
names themselves.
`Pull request #140 <https://github.com/canonical/robotics_documentation/pull/140>`_
and `pull request #142 <https://github.com/canonical/robotics_documentation/pull/142>`_.

*Next: more from the Open Documentation Academy, and open-source projects in
my own domain, such as* `PyMC-Marketing <https://www.pymc-marketing.io/>`__.
