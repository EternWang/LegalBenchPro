# LegalScope: Measuring Exam-to-Case Transfer in LLM Legal Reasoning

LegalScope studies a simple question with high stakes for legal AI evaluation:
do strong public legal-exam scores actually transfer to real-case legal reasoning?

LegalScope pairs scalable public legal-exam tasks with lawyer-reviewed,
de-identified Chinese civil judgment analysis. The public repository is intentionally
a preview: it documents the research question, benchmark design, evaluation counts,
scoring protocol, release boundary, and reproducible helper code without publishing
the paper draft, full workbook, model outputs, human review sheets, or
non-de-identified case materials.

## Start Here

| If you want to understand... | Read |
| --- | --- |
| The research idea and motivation | [Project Brief](docs/PROJECT_BRIEF.md) |
| Main empirical findings and figures | [Results Summary](docs/RESULTS_SUMMARY.md) |
| Dataset scope and release boundary | [Data Card](docs/DATA_CARD.md) |
| Scoring design | [Scoring Rubric](docs/SCORING_RUBRIC.md) |
| Human validation protocol | [Annotation Protocol](docs/ANNOTATION_PROTOCOL.md) |

## Benchmark at a Glance

<img src="assets/figures/paper_collection_pipeline.png" alt="LegalScope benchmark construction pipeline" width="920">

| Component | Count |
| --- | ---: |
| Public legal-exam questions | 868 |
| Real-case issue-stance prompts | 256 |
| De-identified Chinese civil judgments | 54 |
| Legal issues extracted from judgments | 128 |
| Model groups evaluated | 20 |
| Public-exam model responses | 17,360 |
| Real-case model responses | 5,120 |
| Total dataset model responses | 22,480 |
| Human-validation responses | 1,800 |

The pipeline figure above is Figure 1 from the current manuscript. Its reliability-audit
boxes describe a 76-prompt, 15-judgment subset (1,520 model responses), not the full
256-prompt real-case split. The full paper PDF is not committed to this repository.

## Main Findings

- Public-exam scores correlate with Chinese real-case scores at the model level
  (Pearson `r = 0.835`, Spearman `rho = 0.661`), but rankings and reasoning-mode gains
  do not transfer uniformly.
- Across the 20 model groups, the public-exam mean is `72.0` and the real-case mean is
  `65.3` on the 0-100 scale.
- Real-case legal reasoning exposes a constraint-extraction bottleneck: models write
  fluent legal arguments more easily than they recover the operative legal and factual
  conditions that control those arguments (`73.3` argument validity versus `54.8`
  constraint extraction).
- Automated evaluation aligns strongly with human review on public-exam answers
  (answer-level Pearson `r = 0.925`) but weakens on real-case analysis
  (pooled-lawyer answer-level `r = 0.422`), showing why expert-grounded evaluation
  remains important.

## Repository Map

```text
assets/figures/
  paper_collection_pipeline.png
  paper_score_distribution.png
  paper_jurisdiction_means.png
  paper_transfer_model_judge.png
  paper_transfer_human.png
data/
  README.md
  metadata/dataset_summary.json
  metadata/model_groups.csv
  metadata/source_composition.csv
  sample/README.md
docs/
  PROJECT_BRIEF.md
  RESULTS_SUMMARY.md
  DATA_CARD.md
  SCORING_RUBRIC.md
  ANNOTATION_PROTOCOL.md
  AI_WORKFLOW.md
  FIGURE_SOURCES.md
  RELEASE_STATUS.md
scripts/
  extract_public_sample.py
src/legalscope/
  workbook.py
tests/
  test_workbook.py
```

## Public Release Boundary

This repository does not publish:

- the paper draft or PDF;
- the full benchmark workbook;
- complete prompts, reference answers, model answers, or row-level model-output
  matrices;
- lawyer review sheets or adjudication notes;
- non-de-identified judgments or private source documents.

The public code is a reproducibility scaffold for collaborators with authorized local
access to the private workbook. It is not enough to reconstruct the full benchmark from
the public repository alone.

## Disclaimer

LegalScope is a research benchmark for model evaluation. It is not legal advice, a
legal research product, or a substitute for jurisdiction-specific legal review.
