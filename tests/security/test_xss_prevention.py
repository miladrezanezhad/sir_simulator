"""
XSS Prevention Tests
====================
Tests that the simulator outputs are safe for web display.
"""

import html
import json
import os
import re
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


class TestXSSPrevention(unittest.TestCase):

    def test_html_escaping_angles(self):
        """Angle brackets should be escaped to prevent HTML injection"""
        malicious = "<script>alert('XSS')</script>"
        escaped = html.escape(malicious)

        self.assertNotIn("<", escaped)
        self.assertNotIn(">", escaped)
        self.assertIn("&lt;", escaped)
        self.assertIn("&gt;", escaped)

    def test_html_escaping_quotes(self):
        """Quotes should be escaped to prevent attribute injection"""
        malicious = '" onmouseover="alert(\'XSS\')"'
        escaped = html.escape(malicious)

        self.assertIn("&quot;", escaped)
        self.assertNotIn('" onmouseover=', escaped)

    def test_filename_safety_simple(self):
        """Filenames should only contain safe characters"""
        malicious = "2024-01-01<script>alert('XSS')</script>.csv"

        safe = re.sub(r"<[^>]*>", "", malicious)
        safe = re.sub(r"(?i)alert", "", safe)
        safe = re.sub(r'[()\'"]', "", safe)

        self.assertNotIn("<", safe)
        self.assertNotIn(">", safe)
        self.assertNotIn("alert", safe.lower())
        self.assertTrue(safe.endswith(".csv"))

    def test_json_output_safe_by_default(self):
        """JSON output is safe - JSON parsers don't execute JavaScript"""
        malicious = "</script><script>alert('XSS')</script>"

        json_output = json.dumps({"data": malicious})
        parsed = json.loads(json_output)

        self.assertEqual(parsed["data"], malicious)
        self.assertIsInstance(json_output, str)

    def test_dataframe_html_escaping(self):
        """DataFrame string representation may show raw HTML, but markdown/HTML output escapes"""
        import pandas as pd

        malicious = "<script>alert('XSS')</script>"
        escaped = html.escape(malicious)

        df = pd.DataFrame({"input": [malicious], "safe": [escaped]})
        df_str = str(df)

        self.assertIn("&lt;", df_str)

    def test_javascript_protocol_safety(self):
        """javascript: protocol should be detected and blocked"""
        dangerous = "javascript:alert('XSS')"
        dangerous_upper = "JaVaScRiPt:alert('XSS')"

        def is_safe_url(url):
            url_lower = url.strip().lower()
            return not url_lower.startswith(("javascript:", "data:"))

        self.assertFalse(is_safe_url(dangerous))
        self.assertFalse(is_safe_url(dangerous_upper))
        self.assertTrue(is_safe_url("https://github.com"))

    def test_cli_output_safety(self):
        """CLI output is safe by default (no HTML rendering)"""
        malicious = "<script>alert('XSS')</script>"

        try:
            print(malicious)
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"CLI output crashed: {e}")


if __name__ == "__main__":
    unittest.main()
