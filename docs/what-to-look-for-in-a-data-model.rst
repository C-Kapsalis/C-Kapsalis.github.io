:orphan:

What to look for in a data model
================================

*A review checklist for Power BI semantic models, written for the moment
before you trust the numbers.*

Most broken data models do not look broken. They open, they refresh, the
visuals render, and the numbers are plausible. The defects that matter most
are the ones that stay quiet: a filter that never reaches a table, a
measure pointing at a column someone renamed, a bookmark that restores
nothing. This checklist is what I look for when I review a model, grouped
by the layer where each problem lives. Each item says what to check and
why it matters, because a checklist you don't understand is one you stop
using.

Most of these checks are mechanical, which means a tool can do them. I
built three that do:
:doc:`tmdl-preflight <projects/tmdl-preflight>` for the model files,
:doc:`pbi-plot-styler <projects/pbi-plot-styler>` for the report layer,
and the self-check in :doc:`pbip-model-forge <projects/pbip-model-forge>`
for a model's design before it is built. The checklist comes first,
though. The tools are only the part of it that can be automated.

Structure and file integrity
----------------------------

These are the defects that stop a project from opening at all. They are
cheap to check and expensive to discover in front of a stakeholder.

1. **Every table is wired into the model, both ways.** A table file with no
   ``ref table`` line, or a ``ref table`` line naming a file that no longer
   exists, stops the project opening.
2. **Every table has a partition, even a table that only holds measures.**
   Power BI cannot map a table with no partition to a query.
3. **Lineage tags are unique, real identifiers.** Copy-pasting a table
   copies its tags, and the deployment target rejects the duplicates.
4. **Property lines sit where they belong.** A property such as
   ``isHidden`` that a script or a merge has dropped inside a DAX
   expression, or placed after an object's annotations, rejects the import.
5. **No description is left dangling.** A ``///`` description followed by a
   blank line is harmless until someone appends content after it, and then
   it is a parse error.
6. **Names are unique, ignoring case.** The engine treats ``Sales`` and
   ``sales`` as one name, and a measure cannot share a name with a column
   of its own table.

Relationships
-------------

Relationships are where a model stops being a set of tables and starts
answering questions. They are also where silent errors live.

7. **Every relationship endpoint exists.** Renames and merges leave
   relationships pointing at nothing.
8. **There is at most one active relationship between any two tables.** A
   second active path is ambiguous: Power BI either rejects it or quietly
   deactivates one, and you will not be told which.
9. **Every bidirectional, many-to-many, and auto-detected relationship has
   been chosen by a person.** Each one changes how filters flow without
   changing a single line of DAX. Auto-detected relationships in particular
   were never chosen by anyone.
10. **Dimensions can reach the facts they claim to filter.** Existence is
    not enough. A dimension with no active path to a fact returns the grand
    total on every row, which looks plausible rather than broken.

DAX
---

DAX is compiled lazily, when a visual asks for it. That means a model with
broken DAX imports cleanly and fails later, in someone else's hands.

11. **Every referenced table, column, and measure resolves.** A deleted
    table imports fine and then breaks every visual that touches it.
12. **Delimiters balance everywhere DAX lives**: measures, calculated
    columns, calculated tables, calculation items, and dynamic format
    strings. A broken format-string expression takes down every visual that
    uses its calculation group.
13. **No variable is declared twice in the same scope.** It is a classic
    merge artifact, and it only fails when the measure is evaluated.
14. **Every ratio is valid at the grain it is shown.** A ratio is only
    correct where both its numerator and its denominator are filtered.
    Counting customers from the customer table instead of from the sales
    fact gives every row of a breakdown the same denominator, and only the
    grand total comes out right. This one passes every structural check
    there is. :doc:`I wrote about a real example of it
    <democratizing-data-model-mock-ups>`.

Naming and documentation
------------------------

The field list is the interface most people actually use. It deserves the
same care as any other user interface.

15. **Every visible measure has a description, a format string, and a
    display folder.** These are the tooltip, the default rendering, and the
    organization a business user sees.
16. **Names follow one convention, and the convention agrees with the
    format.** If counts end in ``#`` and rates end in ``%``, a measure
    called ``Churn %`` formatted as a whole number is a bug you can catch by
    reading.
17. **Helpers are hidden and user-facing measures are visible**, and these
    are checked separately, so one mistake cannot hide another.
18. **Descriptions are written for users, not for the team.** A ticket
    number in a tooltip means nothing to a reader, and copied models
    multiply it.

Model settings, refresh, and partitions
---------------------------------------

19. **Calculation groups have implicit measures discouraged**, and every
    calculation item uses the measure it modifies. Otherwise deployment
    fails, or the item ignores the measure it was meant to change.
20. **Incremental refresh is placed correctly and actually folds its date
    range.** A misplaced policy rejects the model; a policy that does not
    filter on its range parameters reloads everything on every refresh.
21. **Calculated tables and field parameters have exact punctuation.** One
    missing or extra comma between rows, and the table silently loads no
    rows at all, after a refresh that reports no errors.
22. **Inline ``#table`` sources don't sit next to calculated tables.**
    Together they force a composite model that will not open.

The report layer
----------------

A model is only half of a Power BI project. The report on top of it has its
own ways of failing quietly.

23. **Every field a visual or bookmark binds still exists in its model.**
    Renaming a measure breaks visuals without an error. Count its
    references in the report files before deleting anything, and look in
    every place a name can hide: field bindings, query references, the
    formatting rules keyed to a measure, and the field-parameter selections
    that slicers and bookmarks store as text.
24. **Bookmarks pass import validation, not just JSON syntax.** An unknown
    key in a bookmark's options, or a number stored as a string, makes the
    service reject the whole report. Valid JSON is not the same as
    importable JSON.
25. **Bookmarks point at pages and visuals that exist**, and their scope is
    deliberate. A bookmark scoped to a list of visuals quietly ignores the
    rest of the page.
26. **Colors come from the theme, and automated formatting never overwrites
    manual formatting.** Theme colors survive a rebrand. A formatting tool
    that rebuilds settings it does not own will eventually delete someone's
    careful work.

The process around the model
----------------------------

27. **Gate on new problems and track old ones by identity.** A legacy model
    will not pass every check on day one. Record its known findings by what
    they are, not by how many there are, and fail only on new ones. A
    count that is allowed to stay flat can hide a new defect behind a fixed
    old one.
28. **Make every check prove it can fail.** A test that has never fired is
    indistinguishable from a test that cannot fire. Plant the defect, and
    watch the check catch it.

A checklist like this is the start of a review, not the end of one. The
mechanical items belong in CI, where they run on every change and nobody
has to remember them. That leaves the review for what only a person can
judge: whether the model answers the questions the business is actually
asking. :doc:`That is easiest when the model is text
<one-governed-model-kept-as-text>`.
