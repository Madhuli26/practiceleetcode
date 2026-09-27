"""Run unittest discovery and write dependency-free HTML, JSON, and JUnit reports."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from html import escape
import json
import os
from pathlib import Path
import tempfile
import time
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def portable_text(text: str) -> str:
    """Remove machine-specific directory prefixes from shared output."""
    prefixes = {
        str(ROOT): ".",
        str(Path.home()): "<home>",
        str(Path(tempfile.gettempdir()).resolve()): "<temp>",
    }
    for prefix in sorted(prefixes, key=len, reverse=True):
        text = text.replace(prefix, prefixes[prefix])
    return text


class ReportResult(unittest.TextTestResult):
    """Capture one result per test, including failure tracebacks and durations."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.records = []

    def _exc_info_to_string(self, err, test):
        return portable_text(super()._exc_info_to_string(err, test))

    def startTest(self, test):
        super().startTest(test)
        self._started = time.perf_counter()
        self._status, self._details = "passed", ""

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self._status = "failed"
        self._details = self._exc_info_to_string(err, test)

    def addError(self, test, err):
        super().addError(test, err)
        self._status = "error"
        self._details = self._exc_info_to_string(err, test)

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self._status, self._details = "skipped", reason

    def addExpectedFailure(self, test, err):
        super().addExpectedFailure(test, err)
        self._status, self._details = "skipped", self._exc_info_to_string(err, test)

    def addUnexpectedSuccess(self, test):
        super().addUnexpectedSuccess(test)
        self._status, self._details = "failed", "Unexpected success"

    def addSubTest(self, test, subtest, err):
        super().addSubTest(test, subtest, err)
        if err is not None:
            status = "failed" if issubclass(err[0], test.failureException) else "error"
            if self._status != "error":
                self._status = status
            self._details += f"{subtest}:\n{self._exc_info_to_string(err, test)}\n"

    def stopTest(self, test):
        self.records.append({
            "name": test.id(), "status": self._status,
            "duration_seconds": time.perf_counter() - self._started,
            "details": portable_text(self._details),
        })
        super().stopTest(test)


def write_reports(result: ReportResult, directory: Path, duration: float) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    counts = {status: sum(row["status"] == status for row in result.records)
              for status in ("passed", "failed", "error", "skipped")}
    summary = {"total": result.testsRun, **counts, "duration_seconds": duration,
               "successful": result.wasSuccessful() and result.testsRun > 0}
    timestamp = datetime.now(timezone.utc).isoformat()
    payload = {"generated_at": timestamp, "summary": summary, "tests": result.records}
    (directory / "results.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")

    suite = ET.Element("testsuite", name="leetcode", tests=str(result.testsRun),
                       failures=str(counts["failed"]), errors=str(counts["error"]),
                       skipped=str(counts["skipped"]), time=f"{duration:.6f}", timestamp=timestamp)
    rows = []
    for record in result.records:
        classname, _, name = record["name"].rpartition(".")
        case = ET.SubElement(suite, "testcase", classname=classname, name=name,
                             time=f'{record["duration_seconds"]:.6f}')
        tag = {"failed": "failure", "error": "error", "skipped": "skipped"}.get(record["status"])
        if tag:
            ET.SubElement(case, tag).text = record["details"]
        details = f'<details><summary>Details</summary><pre>{escape(record["details"])}</pre></details>' if record["details"] else ""
        rows.append(f'<tr><td>{escape(record["name"])}</td><td class="{record["status"]}">{record["status"].upper()}</td><td>{record["duration_seconds"]:.6f}s</td><td>{details}</td></tr>')
    ET.indent(suite)
    ET.ElementTree(suite).write(directory / "junit.xml", encoding="utf-8", xml_declaration=True)
    status = "PASS" if summary["successful"] else "FAIL"
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>LeetCode test report</title><style>
body {{font-family:system-ui,sans-serif;max-width:1200px;margin:40px auto;padding:0 20px;color:#172033}}
table {{border-collapse:collapse;width:100%;font-size:14px}} td,th {{text-align:left;padding:10px;border-bottom:1px solid #ddd}}
.passed {{color:#166534}} .failed,.error {{color:#b91c1c}} .skipped {{color:#854d0e}}
pre {{white-space:pre-wrap;overflow-wrap:anywhere}} .table {{overflow-x:auto}}
</style></head><body><h1>LeetCode test report: {status}</h1>
<p>Generated {escape(timestamp)}</p><p>{result.testsRun} tests · {counts['passed']} passed · {counts['failed']} failed · {counts['error']} errors · {counts['skipped']} skipped · {duration:.4f}s</p>
<div class="table"><table><thead><tr><th>Test</th><th>Status</th><th>Duration</th><th>Details</th></tr></thead>
<tbody>{''.join(rows)}</tbody></table></div></body></html>'''
    (directory / "index.html").write_text(html, encoding="utf-8")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report-dir", type=Path, default=ROOT / "report")
    parser.add_argument("--pattern", default="test_*.py", help="Test filename pattern")
    args = parser.parse_args(argv)
    suite = unittest.defaultTestLoader.discover(str(ROOT / "test"), pattern=args.pattern,
                                              top_level_dir=str(ROOT))
    started = time.perf_counter()
    result = unittest.TextTestRunner(verbosity=2, resultclass=ReportResult).run(suite)
    write_reports(result, args.report_dir, time.perf_counter() - started)
    print(f"Reports: {portable_text(os.path.relpath(args.report_dir / 'index.html'))}")
    if result.testsRun == 0:
        print("No tests discovered; treating this as a failed run.")
    return 0 if result.wasSuccessful() and result.testsRun > 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
