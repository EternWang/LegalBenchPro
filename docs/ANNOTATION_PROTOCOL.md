# Annotation Protocol

## Purpose

The human-validation protocol checks whether automated and model-judge scores align
with human legal review, and whether the failure modes found in real cases differ from
public-exam scoring.

## Human-Scored Subset

| Subset | Items | Model groups | Human-validation responses |
| --- | ---: | ---: | ---: |
| Public legal exams | 80 | 20 | 1,600 |
| Chinese real cases | 10 | 20 | 200 |
| Total | 90 | 20 | 1,800 |

## Review Focus

Human review checks:

- source and reference-answer alignment for public-exam rows;
- issue and stance consistency for real-case rows;
- privacy and de-identification constraints;
- citation relevance;
- constraint extraction;
- argument validity;
- cases where automated scores appear too generous or too punitive.

## Preferred Review Notes

Review notes should be brief and audit-friendly. Useful tags include:

- opposite stance;
- invented facts;
- missing operative constraint;
- weak citation linkage;
- wrong legal domain;
- missed key issue;
- thin rule-to-fact analysis;
- mostly aligned with minor gaps.

## Reliability Reporting

Public-exam automatic scores align strongly with independent review at the answer
level (`r = 0.925`, `rho = 0.928`) and model level (`r = 0.992`, `rho = 0.986`).
For real cases, the equal-weight mean of the two lawyers gives lower answer-level
agreement (`r = 0.422`, `rho = 0.364`) and more stable model-level agreement
(`r = 0.800`, `rho = 0.577`).

The two real-case lawyers' quadratic-weighted kappa is `0.669`, `0.577`, and `0.579`
for citation relevance, constraint extraction, and argument validity. Their pooled
dimension means are `69.75`, `71.38`, and `75.44`, respectively. Both lawyers place
constraint extraction below argument validity; a 10,000-draw prompt-cluster bootstrap
estimates the gap at `4.06` points (95% CI `[1.38, 6.69]`).

The public-exam reviewers and both real-case lawyers were excluded from benchmark
construction. Raw human review sheets remain outside the public repository.
