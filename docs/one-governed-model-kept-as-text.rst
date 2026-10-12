:orphan:

One governed model, kept as text
================================

*Why a central data model needs a text format, and how TMDL turns modeling
best practice into something you can review, test, and transfer.*

Every organization that takes analytics seriously ends up with the same
problem. The first semantic model is built carefully. Then a second team
needs something similar, so the model is copied. Then a client, a region,
or a product line needs its own version, and it is copied again. A year
later there are a dozen models that all started from the same idea and no
longer agree on what "revenue" means.

The usual response is governance by meeting: a review board, a naming
document, a shared drive of "approved" files. It rarely holds, and the
reason is not discipline. When a model is stored as an opaque binary file,
there is nothing to govern. You cannot see what changed between two
versions, so you cannot review a change. You cannot compare two models, so
you cannot say how far one has drifted from the other. And you cannot apply
an improvement from one model to another except by redoing it by hand.

A central, governed model only works if the model is text.

What changes when the model is text
-----------------------------------

Power BI's project format, PBIP, saves a semantic model as a folder of
plain-text TMDL files: one file per table, plus files for relationships,
shared expressions, and model settings. A measure is a few readable lines.
A relationship is a short block that names the two columns it joins.

That sounds like a storage detail. It is actually a change in what is
possible:

- **A change becomes a diff.** Adding a measure, renaming a column, or
  changing a relationship shows up as a few lines in a pull request that a
  person can read and approve.
- **Best practice becomes a test.** "Every visible measure has a
  description" stops being a sentence in a style guide and becomes a check
  that runs on every commit. The
  :doc:`checklist in my previous post <what-to-look-for-in-a-data-model>`
  is mostly this kind of rule.
- **A model becomes comparable.** Two models in text can be compared
  object by object: which measures are missing, which expressions differ,
  which relationships point somewhere else.
- **A structure becomes transferable.** A modeling pattern that works,
  such as a calendar table done right, a set of standard measures, or a
  dimension with its keys and hierarchies, is text that can be applied to
  another model on purpose, instead of rebuilt from memory.

TMDL is good at this in a way earlier formats were not. Its files are
small, line-oriented, and indented like code, so diffs stay readable. Each
object carries a stable lineage tag, so a tool can tell a renamed object
from a new one. And because it is the format Power BI itself reads and
writes, there is no export step that can fall out of date.

The template and its derivatives
--------------------------------

Text makes a specific architecture practical: one **template** model that
holds the canonical core, and a fleet of **derivative** models built from
it, one per client, team, or region. The template is not a superset of
everything any derivative has ever needed. It is the part every derivative
must carry: the shared tables, the agreed definitions, the measures that
mean the same thing everywhere.

Derivatives are allowed to extend it. A client can add its own measures and
tables, and those extras are not drift. What a derivative may not do is let
the shared core decay. When the template improves, the improvement should
reach every derivative. When a derivative's copy of a shared measure
diverges, someone should find out.

That is where best practice gets distilled. Each improvement made once, in
the template, and reviewed as a diff, becomes the standard every model is
measured against. Over time the template becomes the organization's
modeling knowledge in executable form. This is the problem I built
:doc:`tmdl-drift-doctor <projects/tmdl-drift-doctor>` to solve.

What it takes to make transfer safe
-----------------------------------

Moving structure from a template into a fleet sounds simple: add what is
missing, fix what differs. In practice, every naive version of that
breaks something. These are the mechanisms that make it safe.

**Absence is not a reason to delete.** If a derivative has a measure the
template lacks, that is usually the derivative's own work. The only objects
that can be removed automatically are the ones that provably *used to be*
in the template and were deliberately retired. That needs a ledger: a
permanent record of every retirement, with the date and the reason, so the
tool can tell "never had it" from "removed it on purpose".

**A deletion must not strand what depends on it.** Retiring a column is
safe in the template and dangerous in a derivative whose own measures still
read it. A safe tool checks what depends on an object before removing it,
and when a derivative's own work is in the way, it stops and hands the
decision to a person instead of leaving a model that will not open.

**Intentional difference has to be written down.** Some derivatives are
meant to differ: a client with a different definition of an active
customer, a region with its own data source. If that intent lives in
someone's head, every sync is a risk. If it lives in a reviewed file, with
a reason, an owner, and a date, the tool can respect it, and anyone can see
why it exists. A suppressed difference should still be printed every time,
so it never becomes invisible.

**A name lives in more places than you think.** Renaming a measure touches
its declaration, every DAX expression that references it, any text that
compares against its name, the labels people see, and every report visual
bound to it. Most of those fail silently when they are missed. A rename is
only finished when the count of old references, model and report together,
reaches zero.

**Debt may shrink, but it must not grow.** A fleet rarely starts clean. A
ratchet records how much drift each model carries today and fails only when
that number goes up. The floor only ever moves down. Some things should
never be allowed at any level: a retired object that reappears after a
careless merge is a resurrection, and it should fail loudly rather than
show up as a number that went up by one.

**Counts are not correctness.** A green dashboard of drift counts can hide
a fix that was silently reverted, for example by a merge that resolved a
conflict the wrong way. Keeping a record of every fix that was applied,
and re-checking that each one is still there, catches what counting never
will.

**What the rules cannot decide goes in a queue.** Automation should
proceed where the rules are certain and stop where they are not. Everything
it stops on belongs in one short list, owned by a person. And anything that
keeps coming back to that list is a rule that has not been written yet.

Why this matters beyond Power BI
--------------------------------

None of these ideas is specific to Power BI. They are what software
engineering learned about source code: version control, review, tests,
dependency checks, and the habit of encoding a lesson as a check so it
never has to be learned twice. The semantic layer is where a business's
definitions live, so it deserves the same treatment as its code. A text
format is what makes that possible.

It is also what makes the next step possible. Once modeling knowledge lives
in a governed template and a set of executable rules, it can be handed to
people who are not data engineers, and to tools that build models for them.
:doc:`That is the subject of my next post
<democratizing-data-model-mock-ups>`.
