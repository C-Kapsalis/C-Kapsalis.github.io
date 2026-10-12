Open-source contributions
=========================

Most of this work came through Canonical's
`Open Documentation Academy <https://github.com/canonical/open-documentation-academy>`_,
where Canonical's technical authors mentor newcomers through real
documentation issues. I used it to learn and practise the craft on
production documentation, with an experienced author reviewing every change.

.. list-table::
   :header-rows: 1
   :widths: 30 45 25

   * - Project
     - Contribution
     - Status
   * - :ref:`Ulwazi <oss-ulwazi>`
     - Designed and built the theme's "Get help" section
     - Merged, October 2026
   * - :ref:`Launchpad manual <oss-launchpad>`
     - Reworked the "Register your project" guide
     - Merged, October 2026
   * - :ref:`Robotics documentation <oss-robotics>`
     - Homepage descriptions and a cross-reference naming scheme
     - Merged
   * - :ref:`Diátaxis <oss-diataxis>`
     - Documentation typo fix
     - Merged

Canonical Open Documentation Academy
------------------------------------

.. _oss-ulwazi:

Ulwazi: a "Get help" section that says what its links are
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Pull request #144 <https://github.com/canonical/ulwazi/pull/144>`_ ·
`Academy issue #356 <https://github.com/canonical/open-documentation-academy/issues/356>`_

Ulwazi is the new Sphinx theme for all of Canonical's documentation, built on
the Vanilla Framework. The task was to add a configurable panel of help links
(chat, forum, issue tracker) to every page. It looked like a styling task. I
treated it as a question of meaning: what *kind* of thing is this list, and
which component already says that?

My first instinct was to reuse the classes of the "On this page" list, since
it blended in perfectly. But those classes exist for in-page navigation, and
these links take the reader somewhere else entirely, so the markup would have
told a false story about them. I went through Vanilla's component catalogue
instead and ruled out candidates on semantic grounds. A contextual menu, for
example, hides its items until the reader opens it, which is wrong for links
that should always be visible. I built prototypes of the two real contenders
in three placements and discussed them with the theme's maintainer, a
Canonical technical author, until we agreed on a direction.

The final design makes "Get help" a section of the left-hand table of
contents itself. It is generated in Python, so its heading matches the theme's
own section captions instead of being a hand-made copy that could drift out of
step. A divider and a help icon set it apart, and the icon sits in its own
gutter so the heading stays aligned with the sections above it. The section is
off by default and switched on through a single ``conf.py`` setting.

The review also taught me discipline about scope. When my changes started to
override the maintainer's new styling for other sections, I removed them and
kept the pull request to the feature it was for.

.. _oss-launchpad:

Launchpad manual: checking the page against the product
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Pull request #591 <https://github.com/canonical/launchpad-manual/pull/591>`_ ·
`Academy issue #349 <https://github.com/canonical/open-documentation-academy/issues/349>`_

The task was to tidy the formatting of Launchpad's "Register your project"
guide and mark up its interface elements with ``:guilabel:``. Before touching
the markup, I registered a project myself and compared the page with what
Launchpad actually shows. The guide described an older, single-step flow with
fields that no longer exist, so I documented the current two-step process
rather than neatly formatting instructions that were wrong. I used
``:guilabel:`` only where the reader is directed to a control, not for every
mention of a field name, and kept Launchpad's own spelling ("Licences") inside
those labels. I also flagged openly that some of these edits went beyond
formatting, so the reviewer could judge them separately.

The review was a lesson in how-to writing. My reviewer, a Canonical technical
author, pushed me to cut overlapping steps, choose admonitions that match the
weight of their message, link only to pages closely related to the task, and
avoid UI positions ("the right-hand menu") that can change with the layout or
the device.

.. _oss-robotics:

Canonical robotics documentation: making labels carry meaning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Pull request #140 <https://github.com/canonical/robotics_documentation/pull/140>`_ ·
`Pull request #142 <https://github.com/canonical/robotics_documentation/pull/142>`_ ·
`Academy issue #358 <https://github.com/canonical/open-documentation-academy/issues/358>`_

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

.. _oss-diataxis:

Diátaxis: documentation typo fix
--------------------------------

`Pull request #164 <https://github.com/evildmp/diataxis-documentation-framework/pull/164>`_

A small fix to the documentation of the Diátaxis framework itself, the very
framework I use to structure my own documentation. Modest in size, but it
took me through the project's contribution workflow end to end and, more
usefully, made me read the source material closely.

Up next
-------

Documentation and internationalization contributions to
`Data Formulator <https://github.com/microsoft/data-formulator>`__,
`Flint <https://github.com/microsoft/flint-chart>`__, and
`JASP <https://jasp-stats.org/>`__.
