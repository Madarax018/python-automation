import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class AutomationTests(unittest.TestCase):
    def test_organize_sample_files(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            (folder / "sample.txt").write_text("hello")
            result = subprocess.run(
                [sys.executable, str(ROOT / "main.py"), temp],
                capture_output=True, text=True, timeout=10
            )
            self.assertEqual(result.returncode, 0)
            self.assertEqual(
                (folder / "txt" / "sample.txt").read_text(),
                "hello"
            )
