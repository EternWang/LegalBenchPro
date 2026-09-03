from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class MetadataConsistencyTests(unittest.TestCase):
    def test_dataset_totals_match_component_counts(self) -> None:
        summary = json.loads(
            (ROOT / "data" / "metadata" / "dataset_summary.json").read_text(
                encoding="utf-8"
            )
        )
        counts = summary["counts"]

        self.assertEqual(
            counts["dataset_items_total"],
            counts["public_exam_items"] + counts["real_case_issue_stance_prompts"],
        )
        self.assertEqual(
            counts["dataset_model_responses_total"],
            counts["public_exam_model_responses"]
            + counts["real_case_model_responses"],
        )
        self.assertEqual(
            counts["real_case_model_responses"],
            counts["real_case_issue_stance_prompts"] * counts["model_groups"],
        )
        self.assertEqual(
            summary["robustness_audit"]["clustered_subset_model_responses"],
            summary["robustness_audit"]["clustered_subset_prompts"]
            * counts["model_groups"],
        )

    def test_source_composition_counts_match_paper_splits(self) -> None:
        with (ROOT / "data" / "metadata" / "source_composition.csv").open(
            newline="", encoding="utf-8"
        ) as handle:
            rows = list(csv.DictReader(handle))

        real_case_rows = [
            row
            for row in rows
            if row["split"] == "real_case"
            and row["dimension"] == "legal_category"
        ]
        self.assertEqual(sum(int(row["count"]) for row in real_case_rows), 256)
        self.assertEqual(
            {row["value"] for row in real_case_rows},
            {"Tort", "Contract", "Property"},
        )

        country_rows = [
            row
            for row in rows
            if row["split"] == "public_exam" and row["dimension"] == "country"
        ]
        us_source_rows = [
            row for row in rows if row["split"] == "public_exam_us_source"
        ]
        public_category_rows = [
            row
            for row in rows
            if row["split"] == "public_exam"
            and row["dimension"] == "legal_category"
        ]
        self.assertEqual(sum(int(row["count"]) for row in country_rows), 868)
        self.assertEqual(sum(int(row["count"]) for row in us_source_rows), 604)
        self.assertEqual(sum(int(row["count"]) for row in public_category_rows), 868)

    def test_model_metadata_uses_current_manuscript_names(self) -> None:
        with (ROOT / "data" / "metadata" / "model_groups.csv").open(
            newline="", encoding="utf-8"
        ) as handle:
            names = {row["model_group"] for row in csv.DictReader(handle)}

        self.assertEqual(len(names), 20)
        self.assertIn("GPT-5.4 xhigh", names)
        self.assertIn("GPT-5.4 medium", names)
        self.assertIn("Gemini 3 Flash Low", names)


if __name__ == "__main__":
    unittest.main()
