"""Check report contents using deliberately passing and failing synthetic tests."""
import io
import json
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET

from test.run_tests import ROOT, ReportResult, portable_text, write_reports


class TestReports(unittest.TestCase):
    def test_machine_paths_are_removed(self):
        text = f'{ROOT}/test/example.py {Path.home()}/external.py'
        cleaned = portable_text(text)
        self.assertNotIn(str(ROOT), cleaned)
        self.assertNotIn(str(Path.home()), cleaned)
        self.assertIn('./test/example.py', cleaned)
        self.assertIn('<home>/external.py', cleaned)

    def test_mixed_outcomes_and_escaping(self):
        class Sample(unittest.TestCase):
            def test_pass(self):
                self.assertTrue(True)

            def test_fail(self):
                self.fail('<unsafe>& failure')

            def test_error(self):
                raise RuntimeError('example error')

            @unittest.skip('example skip')
            def test_skip(self):
                pass

        suite = unittest.defaultTestLoader.loadTestsFromTestCase(Sample)
        result = unittest.TextTestRunner(stream=io.StringIO(), resultclass=ReportResult).run(suite)
        self.assertFalse(result.wasSuccessful())
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            write_reports(result, path, 0.1)
            data = json.loads((path / 'results.json').read_text())
            self.assertEqual(data['summary']['total'], 4)
            for status in ('passed', 'failed', 'error', 'skipped'):
                self.assertEqual(data['summary'][status], 1)
            self.assertFalse(data['summary']['successful'])
            xml = ET.parse(path / 'junit.xml').getroot()
            self.assertEqual(len(xml.findall('testcase')), 4)
            self.assertEqual(len(xml.findall('testcase/failure')), 1)
            self.assertEqual(len(xml.findall('testcase/error')), 1)
            self.assertEqual(len(xml.findall('testcase/skipped')), 1)
            html = (path / 'index.html').read_text()
            self.assertIn('&lt;unsafe&gt;&amp; failure', html)
            self.assertNotIn('<unsafe>', html)
            self.assertIn('report: FAIL', html)
            for filename in ('index.html', 'results.json', 'junit.xml'):
                contents = (path / filename).read_text()
                self.assertNotIn(str(ROOT), contents)
                self.assertNotIn(str(Path.home()), contents)

    def test_subtest_failure_is_reported(self):
        class Sample(unittest.TestCase):
            def test_subtests(self):
                with self.subTest(value=1):
                    self.assertEqual(1, 2)
        result = unittest.TextTestRunner(stream=io.StringIO(), resultclass=ReportResult).run(
            unittest.defaultTestLoader.loadTestsFromTestCase(Sample))
        self.assertEqual(result.records[0]['status'], 'failed')
        self.assertIn('value=1', result.records[0]['details'])
