
Cohortica
=============

**A free, open-source interview-prep site for marketing roles, and a
content-architecture problem disguised as a web app.** Cohortica organizes 59
practitioner playbooks across 12 disciplines (email marketing, paid search,
SEO, paid and organic social, paid media, web and customer analytics,
attribution and experiments, competitive research, GEO and LLM traffic, and
product management), each one condensing a topic into the question it
answers, the framework a practitioner actually uses, the metrics that matter
and their traps, and three to five realistic interview questions with the
reasoning a strong candidate would use. Two deterministic diagnostics, a
funnel engine and a brand strategy engine, sit on top and train the same
diagnostic thinking a case interview tests for. No AI, no backend, no
accounts, no tracking; the whole thing is static and runs client-side.

Why I built it
-------------------------------------------------------------

I chose to study marketing at Syracuse University's Whitman School of
Management because of its emphasis on product management and marketing
analytics, the two disciplines that frame Cohortica's playbooks. That
training changed how I saw my own work. Looking at documentation as a
product manager would, I realized how far technical communication still had
to go in the companies I had worked for: it was treated as an afterthought
to shipping, not as part of what was shipped.

That realization is why I am joining Canonical: to learn from the teams that
set the standards in this field, and to make the case that documentation is
a product feature. Open source makes software available; documentation is
what makes that availability usable. For an open-source data solution, the
readers are different teams: data engineers, data-platform operators, data
analysts and scientists, and compliance teams. Each one has to adopt the
software, use it in the way that gets the most value from it, troubleshoot
it, and extend or adjust it to fit their own stack. Serving all of them does
not mean writing separate descriptions of the same product. It means giving
each team its own path through one governed body of knowledge. Cohortica is
a small, self-contained exercise in exactly that: one fixed structure,
written once, that readers from twelve disciplines can each find their way
through.

Why this is a documentation project, not just a product
-------------------------------------------------------------

The interesting design decision was never the diagnostics' logic; it was
deciding that a playbook is a fixed shape, not free-form writing. Every one
of the 59 follows the same four movements (an opening that earns the
reader's next minute, the framework, the metrics with their traps, and the
interview questions with the reasoning behind them), and that shape is
enforced editorially, not by code. The result reads like one voice wrote all
59, even though the goal was to make each one fast to extend without a style
drift creeping in over time.

The two diagnostics apply the same discipline to decision logic instead of
prose: each is one data array of states (declining, flat, inefficient for
the funnel; absent, weak, repositioning, and similar triads for each brand
phase), and every state carries the same fields (signals, actions, what to
verify, and a linked micro-playbook). Adding a new state or a new discipline
means filling in that shape once; the app reads the data generically and
needs no code changes to grow.

Open source, with real contribution guidelines
-----------------------------------------------------

Cohortica is MIT-licensed and open to contributions, and the highest-value
one is a playbook: drop a markdown file with three frontmatter keys into the
right discipline folder, and the app picks it up at build time. The
repository's README doubles as the full contributor guide (there is no
separate documentation site for a project this size), covering how to add a
playbook, add a new discipline, and extend either diagnostic; its
CONTRIBUTING guide carries the editorial bar content contributions are held
to: the four-movement format, the tone rules (an operator's voice,
benchmarks over adjectives, no product pitches, no named clients), and the
review checklist every content pull request runs through.

Project links
-------------

- `Cohortica Studio repository on GitHub
  <https://github.com/C-Kapsalis/Cohortica_Studio>`_: source code, the full
  README-based contributor guide, and CONTRIBUTING.md.
- `Live site <https://cohortica-studio.vercel.app/>`_.

*React, Vite, no backend; MIT license.*
