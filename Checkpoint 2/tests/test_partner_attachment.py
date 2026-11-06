"""Partner eligibility uses the actual assignment month without altering a run."""
from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

BASE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE))
from prepare_submission import PreparationError,attach_partner


class PartnerAttachmentTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix="checkpoint2-partner-tests-")
        self.root=Path(self.temp.name)
        self.run=self.root/"runs"/"partner"
        self.run.mkdir(parents=True)
        self.config={"ticker":"TEST","as_of":"2026-11-05"}
        self.quarter={"release_date":"2026-10-27"}
        (self.run/"run_config.json").write_text(json.dumps(self.config),encoding="utf-8")
        (self.run/"quarter_observations.json").write_text(json.dumps(self.quarter),encoding="utf-8")
        self.manifest={"primary_run":"existing-primary","partner_run":None}
        self.base_patch=patch("prepare_submission.BASE",self.root)
        self.validation_patch=patch("prepare_submission.validate_live")
        self.base_patch.start()
        self.validation_patch.start()

    def tearDown(self):
        self.validation_patch.stop()
        self.base_patch.stop()
        self.temp.cleanup()

    def test_default_month_mismatch_is_actionable_and_does_not_attach(self):
        before=deepcopy(self.manifest)
        with self.assertRaises(PreparationError) as caught:
            attach_partner(self.manifest,self.run)
        for expected in ("2026-10-27","2026-11","2026-11-05","--reporting-month"):
            self.assertIn(expected,str(caught.exception))
        self.assertEqual(self.manifest,before)

    def test_explicit_assignment_month_preserves_information_cutoff(self):
        before={p.name:p.read_bytes() for p in self.run.iterdir()}
        attach_partner(self.manifest,self.run,"2026-10")
        self.assertEqual(self.manifest["partner_run"],"runs/partner")
        self.assertEqual(self.manifest["partner_reporting_month"],"2026-10")
        self.assertEqual(before,{p.name:p.read_bytes() for p in self.run.iterdir()})

    def test_explicit_month_still_enforces_eligibility(self):
        before=deepcopy(self.manifest)
        with self.assertRaises(PreparationError):
            attach_partner(self.manifest,self.run,"2026-11")
        self.assertEqual(self.manifest,before)

    def test_invalid_reporting_month_is_rejected(self):
        for month in ("2026-13","2026-1","October 2026",""):
            with self.subTest(month=month),self.assertRaisesRegex(PreparationError,"YYYY-MM"):
                attach_partner(self.manifest,self.run,month)
        self.assertIsNone(self.manifest["partner_run"])


if __name__=="__main__":
    unittest.main()
