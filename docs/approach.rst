How I think about documentation
===============================

My work has always sat between data and marketing, but underneath both there is
a single motive: helping people do their best with the tools they already have.
Documentation is the most direct expression of that motive I have found, which
is why it became the center of my practice long before it was ever part of a
job title.

What documentation is for
-------------------------------------------------------------

Good documentation does three jobs at once, for three different audiences.

It helps the people who use a tool actually reach the goals the tool exists to
serve, the obvious job, and the one everything else rests on. It shows people
on the outside what the tool can do and what it is worth, so they can judge
whether it belongs in their stack and how it compares to the alternatives. A
second, less visible job: it grounds the team that built the tool. Documentation is the
record of the ground they have conquered, a chance to step back and see what
they have made, and an anchor that holds the team to the direction it agreed
on, rather than letting it drift toward every new approach a fast-moving AI
landscape throws up.

Losing sight of any one of these is how documentation quietly fails. Writing
only for today's users leaves the tool invisible to the people who might adopt
it; writing only to sell it leaves everyday users stranded.

Start from the reader, not the feature
-------------------------------------------------------------

I write with a *user-pull* approach: I start from who the reader is and what
they are trying to do, not from the feature I happen to want to describe. That
instinct comes from marketing, where you learn quickly that nobody cares about
your product on its own terms.

The sharpest lesson I have had here came from a client I had built a Power BI
data model and a set of reports for, to help their marketing team track its
digital-marketing performance. One of their marketing managers asked a question
that revealed they were not struggling with the reports at all. They were
missing the underlying fundamentals of their own field that my documentation
silently assumed.
Documentation is meant to answer the questions its audience is most likely to
ask, but there can be no questions when there is no underlying knowledge to
spark them. So part of the job is to supply that knowledge, through glossaries
and explanatory pieces that get the reader's mind going, before the rest of the
documentation can land.

Diátaxis is where I start
-------------------------------------------------------------

I structure documentation with Diátaxis: tutorials, how-to guides, reference,
and explanation. I did not know it had a name when I began; I arrived at
something like it by instinct, and finding the framework gave that instinct a
spine.

I have used all four modes in earnest. Documenting a marketing-analytics product
for people who had never touched Power BI and were, frankly, afraid of it, I
wrote **tutorials** that taught by doing: a blank report template with
selectors, walking the reader through what a metric, a dimension and a bookmark
actually are, on demo data. I wrote **how-to guides** for the real tasks each
discipline faced, including branching ones: for email marketers, a guide that
checks deliverability against benchmarks, then sends you down one path if your
open rates are healthy and another if your lists need fixing first. I wrote
**reference** that differed by reader, because the metrics an SEO specialist
cares about are not the ones an email marketer does. And I wrote **explanation**,
a piece on the funnel view, and why measuring it builds accountability into a
team's marketing practice.

But structure follows complexity
-------------------------------------------------------------

Diátaxis is an excellent start, not a straitjacket. How much of it you need is
set by the complexity of the tool *from the user's point of view*. A small
command-line tool with a handful of options does not need explanatory essays and
a wall of how-to guides; it needs a short tutorial and a tight reference. A
genuinely complex system, a library like `PyMC-Marketing
<https://www.pymc-marketing.io/>`__, which brings Bayesian
modeling to marketers, needs all four modes, plus the theory behind them, plus
video tutorials, masterclasses and courses to bring people in. The framework
tells you which kinds of documentation exist; the tool's difficulty, as the user
experiences it, tells you how far to take each one.

One definition, in one place
-------------------------------------------------------------

The hardest problem I keep meeting is serving genuinely different readers from
one body of truth. The usual advice, split the docs by role, is not enough,
because people from different departments still have to reach shared decisions.
If each audience quietly drifts toward its own definition of a term, the gap
between them widens instead of closing.

The clearest case I have hit is CAC. Marketing reads it as a campaign-efficiency
signal, so it accepts the current level as a baseline and strives to drive it
down; finance reads it as a unit-economics input, so it wants the number as low
as possible from the start. Neither reading is wrong, but if the two are not
anchored to one governed definition they arrive at the same meeting with
different numbers bearing the same name, and the tool gets blamed for the
disagreement. The answer, for concepts this heavyweight, is less a documentation
trick than a governance one: the definition has to stand as a corporate-level,
agreed-upon standard, settled once for the whole organization, not a number any
single team gets to argue its way to. In practice I keep each such definition in
exactly one place and have every audience-specific page link back to it rather
than restate it, so a reader's path can diverge in register but never in
substance.

Markup is part of the meaning
-------------------------------------------------------------

What a reader sees is only half of a page. The other half is what the markup
says each element *is*: a link that moves you within the page or one that
takes you somewhere else, a word that names a button or one that is just
prose. Readers notice that half without knowing it, and so do screen readers,
search, and the tooling that has to maintain the docs later. When the markup
tells the truth, the page holds together. When it borrows whatever happens to
look right, it quietly lies.

That is how I approached a "Get help" section for
:ref:`Ulwazi <oss-ulwazi>`, Canonical's documentation theme. The obvious move
was to copy the styling of the "On this page" list next to it, but those
links navigate within the page and these leave it. So I chose components for
what they mean, not how they look, and built the section so its heading
*is* the theme's own section caption rather than a copy of it. The same rule
applies at the level of a single word. In the
:ref:`Launchpad manual <oss-launchpad>` I marked up an interface label only
where the reader is being sent to that control, not every time a field is
mentioned. And in the :ref:`robotics documentation <oss-robotics>`, I gave
cross-reference labels endings that say what role the page plays for a reader,
and no ending where there was no distinction to make.

A page is a set of claims about the product
-------------------------------------------------------------

Every instruction in a how-to guide is a claim: this field exists, this
button is here, this step comes next. Products move on and the claims go
stale without anyone noticing, so before I edit a page I check it against the
real thing. Asked only to reformat Launchpad's project-registration guide, I
registered a project first and found the guide described a flow that no
longer existed. Formatting it neatly would have made wrong instructions look
more trustworthy. Instead I documented the current flow and told the
reviewer plainly which of my edits went beyond the brief. Mentorship from
Canonical's technical authors through the Open Documentation Academy
sharpened the other side of this. Keep each change to its stated purpose.
Don't describe the interface in ways that will break when it changes, such as
"the menu on the right". And give each admonition the weight its message
actually carries.

Documentation is a product
-------------------------------------------------------------

Once I have a first draft across all the structures, I do not think I have
finished; I think I have a prototype. From there I treat documentation the way
I would treat any product being put into the world: publish it, get it in front
of real users, gather feedback, and iterate. Open source makes this unusually
easy, because the community is embedded in the software itself, so feedback
arrives organically rather than having to be extracted.

That, in the end, is what I want documentation to do: not merely support a tool,
but make people fall in love with it and use it to the fullest. That is the job
I am trying to learn to do properly.
