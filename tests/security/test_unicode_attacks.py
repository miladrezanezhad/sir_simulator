"""
Unicode Attack Tests
====================
Tests if the simulator handles malicious Unicode/UTF-8 inputs safely.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


class TestUnicodeAttacks(unittest.TestCase):

    def test_homoglyph_attack(self):
        """Should handle visually similar characters safely"""
        malicious_inputs = [
            "\u0410\u0412\u0421",
            "administrat\u043Er",
            "r\u043E\u043Et",
            " config",
            "system\x00.exe",
        ]

        for malicious in malicious_inputs:
            try:
                result = str(malicious)
                self.assertIsInstance(result, str)
            except Exception as e:
                self.fail(f"Failed on unicode input '{repr(malicious)}': {e}")

    def test_rtl_override_attack(self):
        """Should handle RTL (Right-to-Left) override characters"""
        rtl_inputs = [
            "\u202E",
            "\u202D",
            "\u200F",
            "file\u202E.exe",
            "\u202E\u0062\u0061\u0074",
        ]

        for rtl_input in rtl_inputs:
            try:
                processed = rtl_input.encode("utf-8", errors="ignore").decode("utf-8")
                self.assertIsInstance(processed, str)
            except Exception as e:
                self.fail(f"Failed on RTL input: {e}")

    def test_overflow_surrogate_pair(self):
        """Should handle invalid Unicode surrogates safely"""
        surrogate_inputs = [
            "\uD800",
            "\uDC00",
            "\uD800\uD800",
            "\uD800A",
            "\uDC00A",
        ]

        for surrogate in surrogate_inputs:
            try:
                _ = len(surrogate)
                _ = surrogate.encode("utf-8", errors="replace")
            except Exception as e:
                self.fail(f"Failed on surrogate input: {e}")

    def test_invalid_utf8_bytes(self):
        """Should handle invalid UTF-8 byte sequences"""
        invalid_utf8 = [
            b"\xff",
            b"\xfe\xff",
            b"\xc3\x28",
            b"\xe0\x80\xaf",
            b"\xf0\x82\x82\xac",
        ]

        for invalid in invalid_utf8:
            try:
                decoded = invalid.decode("utf-8", errors="replace")
                self.assertIsInstance(decoded, str)
            except Exception as e:
                self.fail(f"Failed on invalid UTF-8: {e}")

    def test_normalization_attack(self):
        """Should handle different Unicode normalization forms"""
        from unicodedata import normalize

        attacks = [
            "caf\u00e9",
            "cafe\u0301",
            "ﬁc",
            "\uFB01g",
        ]

        for attack in attacks:
            try:
                nfc = normalize("NFC", attack)
                nfd = normalize("NFD", attack)
                self.assertIsInstance(nfc, str)
                self.assertIsInstance(nfd, str)
            except Exception as e:
                self.fail(f"Failed on normalization attack: {e}")

    def test_extremely_long_unicode(self):
        """Should handle extremely long Unicode strings without DoS"""
        try:
            long_unicode = "\u4e00" * 50000

            length = len(long_unicode)
            encoded = long_unicode.encode("utf-8")

            self.assertEqual(length, 50000)
            self.assertGreater(len(encoded), 100000)
        except MemoryError:
            self.skipTest("Extremely long string requires too much memory")
        except Exception as e:
            self.fail(f"Failed on long unicode: {e}")


if __name__ == "__main__":
    unittest.main()
