:orphan:

From business idea to data model, without the queue
===================================================

*How I built modeling knowledge into pbip-model-forge, so the people with
the questions can design the model that answers them.*

Ask anyone who has waited for a dashboard where the time went, and it is
rarely in the building. It is in the translation. A stakeholder describes
the questions they want answered. An analyst sketches some tables on a
slide. The data team interprets the slide, builds pipelines, and stands up a
model. Then comes the first demo, and only then does anyone discover that
the grain was wrong, a dimension was missing, or "patients" meant something
different to each person in the room.

Weeks pass before anyone sees a number they can check. And the people with
the deepest understanding of the business (marketing, operations, finance,
clinical teams) are usually the ones with the least access to data
engineering. Their best questions sit in a backlog.

That gap between business ideation and data-team delivery is one of the
biggest bottlenecks in getting insight out of data. It is the bottleneck I
built :doc:`pbip-model-forge <projects/pbip-model-forge>` to shorten.

Let the person with the question go first
-----------------------------------------

The idea is simple: move the *design* step to the stakeholder, and make the
hand-off artifact something the data team can open, inspect, and build
from.

With pbip-model-forge, a domain expert describes their domain in one
sentence, for example *"create a sample data model for a veterinary
clinic"*, in a Claude Code session. Claude designs a star schema: a fact
table of visits, dimensions for patients, veterinarians and services, a
calendar, and a set of measures. The repository turns that design into a
real Power BI project, with believable sample rows physically loaded.

It is not a drawing of a model. It opens in Power BI Desktop, the
relationships resolve, and the measures compute. The stakeholder can drag
fields into a matrix and argue about real numbers instead of boxes on a
slide. Then they can grow it in conversation: *"add pet insurance
providers and measures for how much of each visit insurance covers"*. The
model is rebuilt from its specification and checked again, so it stays
valid as it grows.

Why a tool, and not a template
------------------------------

Two things normally stop a business user from doing this alone.

The first is that a Power BI project is unforgiving to write. There are
about nine structural details that, if wrong, make Desktop refuse to open
the project, often with an error that names nothing useful. I hit each of
them, and each is now handled by the builder rather than left to the
person or the language model. The trickiest is loading real data with no
external source, which means producing a compressed block of bytes that
must match exactly what Desktop itself writes.

The second is subtler, and it is the reason the latest release exists.

Openable is not the same as correct
-----------------------------------

Every model the tool generates is gated by
:doc:`tmdl-preflight <projects/tmdl-preflight>`, which proves it will open.
For a while I treated that as the finish line. Then I found a bug in the
project's own hospital example.

The model had a measure for the average amount billed per patient. It
divided billed revenue by a count of patients, and it counted those
patients from the Patients table. The trouble is that a department filter
reaches the encounters fact, but never reaches the Patients table. So in a
matrix broken down by department, every row divided its revenue by *all*
the hospital's patients. Cardiology showed an average of $18,300 per
patient. The right answer, counting only the patients Cardiology actually
saw, was $36,600.

The model opened. Preflight passed. The grand total was correct, which is
exactly why nobody would notice. Only the rows were wrong, and the rows
are what people make decisions from.

The fix was one line: count patients from the encounters, not from the
dimension. The lesson was bigger. A mock-up that opens with wrong numbers
is worse than one that doesn't open, because people believe it. If I
wanted business users to design their own models, the tool had to carry
the modeling knowledge they don't have time to learn, and apply it every
time.

Building the knowledge in
-------------------------

Version 1.1.0 of pbip-model-forge is the result. I took what I know about
what makes a model trustworthy, much of it written down in
:doc:`my checklist for reviewing data models
<what-to-look-for-in-a-data-model>`, and encoded it in three places.

**In the instructions Claude follows.** The skills that drive the tool now
teach the conventions a good modeler applies without thinking: count
entities from the fact's foreign key, never from the dimension; give every
dimension an "Unknown" member instead of leaving foreign keys empty; name a
foreign key exactly like the key it points to; follow one naming pattern
for measures (``Visits #``, ``No-Show %``, ``Avg Cost per Visit``) and
describe every measure in a sentence.

**In the builder's defaults.** Keys and foreign keys are hidden, because
users never need them. Raw fact columns are hidden, because users should
use measures. Measures land in display folders. The calendar comes with the
columns people actually drill by, and its date range is inferred from the
data, so it cannot quietly fall behind. And every internal identifier is
now derived from the object it belongs to, so rebuilding an unchanged
design produces identical files. That makes every change reviewable as a
diff, which is :doc:`what lets a model be governed at all
<one-governed-model-kept-as-text>`.

**In a gate that runs before anything is written.** A new
``pbip-forge check`` command applies 22 modeling rules to the design,
sample rows included. It checks that keys are unique, that every foreign
key value exists in its dimension, that every fact is linked to the
calendar, that every dimension filters at least one fact, that no filter
flows both ways, that every DAX reference resolves, that every fact is
actually used, and that every ratio respects the grain it is shown at. It
would have caught the hospital bug the first time the model was built. Two
profiles keep the bar honest: a lenient one while a stakeholder is
exploring, and a strict one for what gets handed to the data team.

What the data team receives
---------------------------

The deliverable is deliberately not a report. The generated report is
blank, because the value is the model. What the data team receives is:

- a Power BI project that opens and passes both gates;
- a star schema, with the grain of each fact stated in its description;
- typed keys and relationships, including inactive ones for secondary
  dates;
- measures that state the business definitions in DAX;
- sample rows that pin down intent, such as "self-pay is a member, not a
  missing value";
- and a generated hand-off pack: a machine-readable manifest of every
  table, key, relationship and measure dependency, and a specification
  document with a data dictionary and an entity-relationship diagram.

A data engineer can build the warehouse to exactly that shape, or hand the
specification to a pipeline generator. Either way, the conversation starts
from a model everyone has already seen working, not from a slide.

The point
---------

The asset that keeps its value in the age of AI is domain expertise: the
person who knows the business, its customers, and what moves the numbers.
Tools like this one should not replace data teams. They should let domain
experts arrive at the data team with a design that is already correct, so
the data team's time goes into building it well instead of discovering
what was meant.

That only works if the tool knows what a good model looks like. Teaching
it was the most interesting part of the project, and it is the same work I
care about in documentation: taking knowledge that lives in experts' heads
and putting it where the people who need it will actually meet it.
