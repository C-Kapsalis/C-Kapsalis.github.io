
pbip-model-forge
================

*Prototype a Power BI data model in chat, with real data loaded, then hand
the diagram to your data engineers as a spec.*

For the domain experts who are given the fewest data resources of anyone.

The mission comes first
-----------------------

Most of my tools start from a defect and work outward. This one starts from a
conviction about the moment we are in. In the AI age, the asset that keeps its
value is **domain expertise**, the person who actually understands the
business, its customers, and what moves the numbers. And yet the teams that
hold that expertise (marketing, finance, operations, sales) are routinely
handed the *fewest* data resources and the least data-engineering support.
Their sharpest questions sit in a backlog; their insight never reaches a model.

pbip-model-forge is built to close that gap. It lets a domain expert spec and
stand up a *real* data model themselves, in plain conversation, capturing the
tables, relationships, and measures their questions actually need, so they can
extract insight, justify their priorities, and express their value to
stakeholders in concrete terms, no longer blocked on scarce data resources to
prove the point. I built the tool end to end, two Claude Code skills, a
byte-exact entered-data encoder, and a validating builder, and I lead with
that mission here because it is the reason the project exists.

What it does
------------

You say *"create a sample data model for a hospital,"* or for subscription
analytics, or a delivery fleet. Claude invents plausible tables, columns, and
sample data, and the repo turns that into a **real, openable PBIP**: a Power BI
semantic model with the sample data *physically loaded*, plus a blank report,
validated so that Power BI Desktop will actually open it. Because the data is
really there, relationships resolve, measures compute, and the diagram view is
populated. The model is not a drawing of a model; it is one.

The skill workflow
------------------

This is a **Claude Code skill-based product**, and the skill instructions are
where much of the writing lives, the same move as an earlier project of mine,
where the prose *is* the software rather than describing it. Two skills split
the work along a clean seam:

- **create-sample-model** drives the first pass: domain description in, a spec
  dict assembled, a full PBIP written to disk (``build_pbip(spec, out_dir)``
  produces the ``.pbip`` plus its ``.SemanticModel`` and a blank ``.Report``).
- **validate-and-expand** owns the iteration loop. "Add a promotions
  dimension," "add a margin measure," "make it monthly," and the model
  regenerates from the single spec and re-validates, so it stays openable as it
  grows rather than drifting into a state Desktop rejects.

The will-it-open engineering
----------------------------

A hand-authored PBIP is unforgiving: get one of about nine structural details
wrong and Power BI Desktop simply **refuses to open the project**, often with
an opaque error like *"Sequence contains no elements"* or *"A composite model
cannot be used with entity based query sources."* Each of those was hit for
real and is now encoded into the builder, and written up in a *will-it-open
playbook*, an artifact checklist that walks every file and every check in
turn, so the knowledge is documented, not buried in code.

The single trickiest part is loading real data with no external source: Power
BI stores manually entered data as a compressed **raw-DEFLATE + base64 blob**
that must be byte-identical to what Desktop writes. The repo's encoder is
verified byte for byte against a model proven to open, with a worked example in
its own encoding guide and a test that locks it to Power BI's golden byte
layout. Validation is not self-attested: every generated model is gated by
:doc:`tmdl-preflight <tmdl-preflight>`, and nothing is called "openable" until
``tmdl-preflight check`` reports **0 errors**.

Openable is not the same as correct
-----------------------------------

Passing tmdl-preflight proves a model will open. It says nothing about
whether the numbers are right, and a mock-up that opens with wrong numbers
is worse than one that doesn't open, because people believe it. Version
1.1.0 encodes the modeling knowledge that closes that gap, so generated
models are *born compliant*.

The clearest example was in the project's own hospital model. Its "average
billed per patient" counted patients from the Patients table instead of
from the encounters themselves. Department filters never reach the Patients
table, so every department divided its revenue by all six patients:
Cardiology showed $18,300 when the right answer was $36,600. The model
opened, preflight passed, and only the grand total was correct. The fix was
one line, but the lesson became a rule: a ratio is only valid at a grain
where its numerator and denominator are both filtered.

That rule is one of 22 in a new ``pbip-forge check`` command, which judges
the spec, sample rows included, before any file is written:

- **Keys and integrity:** every dimension has one unique, non-null key;
  every fact row's foreign key exists in its dimension (with an "Unknown"
  member suggested instead of a null); keys on both ends share a type and a
  name.
- **Star-schema shape:** every fact has an active link to the calendar,
  every dimension filters at least one fact, no bidirectional filters, one
  active path between any two tables, no cycles.
- **DAX and grain:** every table, column, and measure a measure references
  exists; every fact is actually read by a measure; ratios respect grain.
- **The hand-off surface:** every visible measure has a format string, a
  real description, a display folder, and a name whose suffix agrees with
  its format (``Patients #``, ``No-Show %``).

Two strictness profiles keep the bar honest: ``mockup`` lets a stakeholder
iterate freely, ``handoff`` is what the data team receives. Builds are now
also deterministic: every internal identifier is derived from the object's
path, so rebuilding an unchanged spec produces identical files and a git
diff shows only real model changes. Both Claude Code skills gate on the
check first and on tmdl-preflight second.

The deliverable is a spec, not a report
----------------------------------------

The generated report is intentionally **blank**, ``.platform`` plus
``definition.pbir``, no pages, no visuals, because the value is the model:
tables, types, keys, relationships, and measures, the thing a data engineer
actually needs. Every build now also writes a hand-off pack: a
machine-readable manifest of tables, keys, relationships and measure
dependencies, and a generated ``SPEC.md`` with the data dictionary and a
star-schema diagram. Because both are generated from the spec, they can
never drift from the model they describe. Give it to your data engineers to build the
warehouse to exactly that shape, or hand it to a data-engineering skill and
have the pipeline generated the same way. The domain expert defines *what the
business needs to measure*; the plumbing follows.

Project links
-------------

- `pbip-model-forge repository on GitHub
  <https://github.com/c-kapsalis/pbip-model-forge>`_: the two Claude Code
  skills, the byte-exact entered-data encoder, the builder, the
  ``pbip-forge check`` self-check, and the `1.1.0 release
  <https://github.com/C-Kapsalis/pbip-model-forge/releases/tag/v1.1.0>`_.
- `Check rule catalog
  <https://pbip-model-forge-documentation.readthedocs.io/en/latest/reference/check-rules.html>`_:
  every rule, its severity in each profile, why it exists, and how to fix it.
- `Documentation site
  <https://pbip-model-forge-documentation.readthedocs.io/en/latest/index.html>`_:
  the published docs, on Read the Docs.

*Python 3.9 or later, standard library only to build a model; 59 passing
tests; requires the tmdl-preflight validator, installed separately from
GitHub; MIT license.*
