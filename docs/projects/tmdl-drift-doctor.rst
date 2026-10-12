
tmdl-drift-doctor
=================

**A drift-detection and remediation suite for fleets of Power BI semantic
models, with a documentation set built to match its scope, not its
feature count.**

The problem it solves is one I know from the inside. When a company
delivers analytics as one semantic model per client, all derived from a
shared template, entropy is the default: the template improves, and a
dozen client models each drift a little, an edited measure here, a
missing column there, a table retired months ago still haunting three
tenants. tmdl-drift-doctor turns "are the clients up to date" from an
afternoon of eyeballing diffs into three commands: ``capture`` a
baseline of the template, ``detect`` typed drift findings per model, and
``remediate`` by cascading template truth back out, allowlist-gated,
dry-runnable, and recorded in an append-only audit ledger.

I built it as an open-source Python package (CLI, parser, safe
text-surgery engine, 130 tests over a fictional gym-chain fleet), and its
documentation is not an appendix to the tool. Before release the suite
was also exercised against a production-scale fleet, a 108-table,
614-measure template with three derived client models and roughly 780
findings, so the claims in the docs are validated, not merely tested.

The documentation
-----------------

The docs follow `Diátaxis <https://diataxis.fr>`_, but not to the
letter: a tutorial walks a sandbox fleet from first capture to first
cascade, one how-to guide covers the three tasks an operator actually
faces (onboarding a model, cascading a retirement, recovering from an
unwanted remediation), a second covers CI, and two reference pages
cover the CLI plus configuration, and the drift-kind catalog plus the
ledger format.

The design decisions live inside those reference pages instead of in a
separate explanation section, because each one earns its place next to
the command or config key it justifies rather than as a standalone
essay. The one I am proudest of: why nothing cascades unless an
allowlist names it, why deletions need a second flag on top of that,
why a stale baseline is refused rather than silently trusted, and the
guarded raw-text editing that exists because a naive version of it once
injected a property line into a bare multi-line DAX expression and broke
every affected measure across a production fleet in one pass. The
drift-kind catalog carries the same discipline down to the per-kind
level: every kind's table row gets a "do not cascade blindly when" note,
so the reference doubles as the judgment calls an operator needs before
running ``--sync``.

Writing that discipline out was not decoration; it was verification.
Stating plainly when a kind should not be auto-fixed forced design
decisions the code then had to honor: extras on shared tables became
advisory-only findings with no remediation path at all, and the
stale-baseline failure mode became a guard that refuses to run rather
than a warning. If the reasoning cannot be written cleanly, the behavior
is usually wrong.

What 1.1.0 added: governing the fleet, not just syncing it
----------------------------------------------------------

The first release could detect drift and push the template back out. Version
1.1.0 is about what makes that safe to run every week.

- **Deletions that cannot break a model.** Relationships are now first-class
  drift, matched on the columns they join rather than on generated IDs, so
  Power BI re-saves never count as changes. Retiring a table or column now
  sweeps the relationships that point at it, and *refuses* while a client's
  own measures, relationships, sort orders or hierarchies still depend on it.
  A refused deletion becomes an item for a human, never a broken model.
- **Moved, not duplicated.** A measure living on a different table in a
  client model is now recognized as the same measure and moved verbatim,
  instead of being inserted a second time under the same name.
- **Declared divergence.** A client that is *meant* to differ gets an
  override in the fleet file with a required reason, an owner and a date.
  Overridden items are never remediated, and every one is printed as an
  acknowledgement, so a suppression can never become invisible.
- **Debt may shrink but never grow.** ``ratchet`` keeps per-model floors that
  only tighten, so a fleet with a backlog can adopt a CI gate on day one.
  A retired object coming back is never floorable: it fails as a
  resurrection, not as a number that quietly went up.
- **Proof that fixes stuck.** ``audit`` re-checks every fix recorded in the
  ledger and fails when one has been reverted by a merge, and ``review``
  writes everything the rules route to a human into one checklist. The
  doctrine printed at its top is the one I care most about: anything that
  recurs there is a missing rule.

The documentation followed the same discipline: every new drift kind got its
"do not cascade blindly when" note in the catalog, and the CI how-to was
rewritten around the ratchet, the audit and the review queue.

- **Stack:** Python, Click, pytest; documentation organized with
  Diátaxis
- **Docs:** index, one tutorial, two how-to guides, two reference pages,
  contributing

Project links
-------------

- `tmdl-drift-doctor repository on GitHub
  <https://github.com/c-kapsalis/tmdl-drift-doctor>`_: source code, release
  notes, and a runnable example fleet (a
  fictional gym chain) under ``examples/``, plus the `v1.1.0 release
  <https://github.com/C-Kapsalis/tmdl-drift-doctor/releases/tag/v1.1.0>`_.
- `Documentation site
  <https://tmdl-drift-doctor-documentation.readthedocs.io/en/latest/>`_:
  the published docs, on Read the Docs.

The documentation lives in its own repository and is published on Read
the Docs; this page introduces the project, not the docs themselves.
