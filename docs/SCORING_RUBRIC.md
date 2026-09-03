# Scoring Rubric

This document summarizes the LegalScope scoring protocol used in the benchmark.

## Public Legal-Exam Scoring

Public-exam answers receive one reference-aware score from 0 to 4.

| Score | Anchor |
| ---: | --- |
| 0 | Wrong, irrelevant, or not evaluable. |
| 1 | Generic or only weakly related legal statements. |
| 2 | Relevant legal content that applies the reference answer incompletely. |
| 3 | The core direction is correct, but some elements are missing. |
| 4 | Covers the decisive legal points and reaches a compatible conclusion. |

## Real-Case A/B/C Rubric

Real-case answers receive three 0-4 scores.

### A. Citation Relevance

Checks whether the answer identifies legally responsive authority and connects it to a
usable legal proposition.

### B. Constraint Extraction

Checks whether the answer follows the assigned stance, extracts operative constraints,
avoids invented facts, respects the prompt boundary, and covers the requested issue.

### C. Argument Validity

Checks whether the answer states a defensible conclusion, applies rules to facts,
handles counterpoints, and avoids unsupported reasoning.

## Calibration Notes

The calibrated rubric keeps strict high-score thresholds while reducing over-penalty
for ordinary incompleteness. Severe failures such as stance reversal, non-answer,
refusal, major truncation, or unusable output remain capped at very low scores. If an
answer lacks a responsive legal basis, citation relevance can be zero while argument
or constraint dimensions may still receive limited credit for substantive reasoning.

The final calibrated setting yields a full-split real-case mean of `65.3`, with `54.5%`
of dimension scores at 3 or 4. On the 200-answer Lawyer 1 overlap, the automatic mean
is `66.8` versus the lawyer mean of `75.5`.
