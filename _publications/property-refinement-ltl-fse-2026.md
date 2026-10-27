---
# ---- Publication record -----------------------------------------------------
# The file name (without .md) is the slug and the URL: /publications/<slug>/
# Everything on the paper page, the publication cards, the citation metadata
# and the sitemap entry is generated from this front matter.
title: "Property Refinement in Linear Temporal Logic: Formal Semantics and Algorithms for Software Verification"
authors:
  - Luca Brodo
  - Giuseppe Scalora
  - Stefan Henkler
date: 2026-06-30
venue: "ACM International Conference on the Foundations of Software Engineering (FSE 2026)"
venue_detail: "published in Proceedings of the ACM on Software Engineering, Vol. 3, No. FSE, Article FSE120"
venue_short: "FSE 2026"
venue_type: journal
citation_venue: "Proceedings of the ACM on Software Engineering"
publisher: ACM
volume: "3"
issue: "FSE"
firstpage: "2698"
lastpage: "2719"
status: Published
status_note: "Version of record available from ACM via the DOI."
doi: "10.1145/3808127"
pdf: /publications/property-refinement-ltl-fse-2026/brodo-2026-property-refinement-ltl-fse.pdf  # served next to the paper page (Google Scholar guideline); original kept in assets/paper/FSELTL.pdf
pdf_note: "Authors' version (CC BY 4.0)"
license: https://creativecommons.org/licenses/by/4.0/
license_label: "CC BY 4.0"
featured: true   # shown under "Selected publications"
featured_order: 2  # position in the selected list
tutorial: ltl-property-redundancy   # slug in _tutorials/, linked from the paper page
research_area: property-refinement   # id from _data/research.yml (Research page grouping)
topics: [Property refinement, LTL, Model checking]
keywords:
  - property refinement
  - Linear Temporal Logic (LTL)
  - model checking
  - formal verification
  - specification debt
  - requirements engineering
  - Büchi automata
  - minimal sufficient set
description: "Brodo, Scalora and Henkler (FSE 2026) define property refinement for LTL and an algorithm that removes redundant properties, cutting verification tasks by up to 75%."
summary_short: "Formal theory and algorithm for finding LTL properties that are already implied by stronger ones, so a verification suite can be reduced to a minimal sufficient set before model checking."
related:
  - minimal-sufficient-temporal-properties-icse-2026
  - property-refinement-ctl
  - social-norm-pattern-catalog-models-2026
abstract: |
  Model checking using temporal logic is a key aspect of formal verification of modern complex software systems. These systems are often result of distributed development processes, involving multiple teams and iterative design cycles. This complexity is mirrored in the corresponding formal specifications, which often consist of a large number of temporal logic properties that need to be verified against a system model. Many of these properties overlap semantically, yet traditional verification treats them as independent, resulting in redundant checks that waste computational resources and inflate engineering effort

  We address this by introducing and operationalizing a formal theory of property refinement for temporal logic into a concrete methodology that automatically identifies redundant properties from a verification suite. This is achieved by first partitioning specifications into equivalence classes based on shared atomic propositions, followed by an analysis of intra-class refinement relations to construct the minimal sufficient subset. Our extensive empirical evaluation confirms the practical viability of our approach, demonstrating it can reduce the number of required verification tasks by up to 75% and accelerate model checking by up to three orders of magnitude, with a one-time associated overhead cost of 0.035% for the refinement analysis. The results of the evaluation confirm that the benefits of this approach are threefold: it reduces the computational requirements for formal verification; it allows engineers to focus on the core requirements of the system, hereby reducing engineering effort; finally, the one-time negligible investment in refinement yields compounding returns, making it particularly advantageous for agile and long-term development lifecycles.

  This work thus establishes property refinement analysis as a key technique for scaling requirement engineering and software verification to modern complex software systems
bibtex: |
  @article{brodo2026ltlrefinement,
    author    = {Brodo, Luca and Scalora, Giuseppe and Henkler, Stefan},
    title     = {Property Refinement in Linear Temporal Logic: Formal Semantics and Algorithms for Software Verification},
    journal   = {Proceedings of the ACM on Software Engineering},
    volume    = {3},
    number    = {FSE},
    articleno = {FSE120},
    numpages  = {22},
    year      = {2026},
    month     = jul,
    publisher = {Association for Computing Machinery},
    doi       = {10.1145/3808127},
    url       = {https://doi.org/10.1145/3808127}
  }
---

### Research question

Formal specifications for industrial software rarely stay small. Requirements are inherited from legacy designs, added by different teams and revised across design iterations, and each one is usually formalised as a separate Linear Temporal Logic (LTL) property and model-checked in isolation. The paper asks whether this "checklist" view of a specification wastes effort: if one property is already guaranteed by a stronger one, verifying both adds cost without adding assurance. The authors call this gradual accumulation of redundant and interdependent properties *specification debt*.

### Approach

The paper develops a formal notion of **property refinement** for LTL. Informally, a property refines another when every execution trace that satisfies the first also satisfies the second, with a non-emptiness condition so that unsatisfiable formulas cannot trivially "refine" everything. The authors establish the algebraic groundwork needed to reason about specification strength in a principled way, and use it to build a concrete methodology:

1. partition the properties of a verification suite into equivalence classes according to the atomic propositions they share, so that only potentially related properties are compared;
2. analyse refinement relations inside each class, using checks based on Büchi automata constructed from the LTL formulas;
3. construct the *minimal sufficient subset*: the most refined properties whose verification guarantees that the whole original suite holds.

This refinement analysis is inserted as an additional step between formalisation and verification in the usual requirements-to-model-checking workflow, and is independent of any particular system model.

### Contribution and results

According to the evaluation reported in the paper, the approach reduces the number of required verification tasks by up to 75% and speeds up model checking by up to three orders of magnitude, with a one-time overhead of 0.035% for the refinement analysis itself. Because the analysis is done once on the specification, its benefit compounds as a system is re-verified over a long or agile development lifecycle. The paper also discusses limitations, notably the exponential cost of automaton construction, and outlines heuristics and toolchain integration as future work.

### Why it matters

For researchers working on model checking, requirements engineering or specification quality, the paper offers both a formal semantics for comparing the strength of temporal properties and a practical way to reduce verification cost on the specification side, complementing model-side techniques such as abstraction and compositional reasoning. The ICSE 2026 companion paper carries the idea over to Computation Tree Logic (CTL), and a later paper develops a complete refinement theory for CTL.
