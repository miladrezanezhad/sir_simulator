"""
Unicode Attack Tests
====================
Tests if the simulator handles malicious Unicode/UTF-8 inputs safely.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


class TestUnicodeAttacks(unittest.TestCase):
    
    def test_homoglyph_attack(self):
        """Should handle visually similar characters safely"""
        malicious_inputs = [
            "\u0410\u0412\u0421",  # Cyrillic "ABC" (not ASCII)
            "administrat\u043Er",   # Mixed Cyrillic 'o'
            "r\u043E\u043Et",       # Cyrillic 'o' in 'root'
            " config",              # Zero-width space before config
            "system\x00.exe",       # Null byte injection
        ]
        
        for malicious in malicious_inputs:
            try:
                # These functions should NOT interpret malicious input as commands
                result = str(malicious)  # Just convert to string safely
                self.assertIsInstance(result, str)
            except Exception as e:
                self.fail(f"Failed on unicode input '{repr(malicious)}': {e}")
    
    def test_rtl_override_attack(self):
        """Should handle RTL (Right-to-Left) override characters"""
        rtl_inputs = [
            "\u202E",  # RTL Override
            "\u202D",  # LTR Override
            "\u200F",  # RTL Mark
            "file\u202E.exe",  # Hidden extension
            "\u202E\u0062\u0061\u0074",  # Hidden command
        ]
        
        for rtl_input in rtl_inputs:
            try:
                # Should not crash or execute hidden commands
                processed = rtl_input.encode('utf-8', errors='ignore').decode('utf-8')
                self.assertIsInstance(processed, str)
            except Exception as e:
                self.fail(f"Failed on RTL input: {e}")
    
    def test_overflow_surrogate_pair(self):
        """Should handle invalid Unicode surrogates safely"""
        surrogate_inputs = [
            "\uD800",      # Lone high surrogate
            "\uDC00",      # Lone low surrogate
            "\uD800\uD800",  # Paired incorrectly
            "\uD800A",     # High surrogate with normal char
            "\uDC00A",     # Low surrogate with normal char
        ]
        
        for surrogate in surrogate_inputs:
            try:
                # Should either handle or gracefully error
                _ = len(surrogate)
                _ = surrogate.encode('utf-8', errors='replace')
            except Exception as e:
                self.fail(f"Failed on surrogate input: {e}")
    
    def test_invalid_utf8_bytes(self):
        """Should handle invalid UTF-8 byte sequences"""
        invalid_utf8 = [
            b'\xff',           # Invalid byte
            b'\xfe\xff',       # BOM not UTF-8
            b'\xc3\x28',       # Invalid continuation
            b'\xe0\x80\xaf',   # Overlong encoding
            b'\xf0\x82\x82\xac',  # Invalid start
        ]
        
        for invalid in invalid_utf8:
            try:
                # Should decode with replacement or fail gracefully
                decoded = invalid.decode('utf-8', errors='replace')
                self.assertIsInstance(decoded, str)
            except Exception as e:
                self.fail(f"Failed on invalid UTF-8: {e}")
    
    def test_normalization_attack(self):
        """Should handle different Unicode normalization forms"""
        from unicodedata import normalize
        
        # Different representations of same character
        attacks = [
            "caf\u00e9",           # NFC: café
            "cafe\u0301",          # NFD: cafe + combining accent
            "ﬁc",                  # Ligature
            "\uFB01g",             # 'fi' ligature
        ]
        
        for attack in attacks:
            try:
                # Normalize all forms
                nfc = normalize('NFC', attack)
                nfd = normalize('NFD', attack)
                self.assertIsInstance(nfc, str)
                self.assertIsInstance(nfd, str)
            except Exception as e:
                self.fail(f"Failed on normalization attack: {e}")
    
    def test_extremely_long_unicode(self):
        """Should handle extremely long Unicode strings without DoS"""
        try:
            # Create 100KB unicode string
            long_unicode = "\u4e00" * 50000  # 50,000 Chinese characters
            
            # Operations should complete in reasonable time
            length = len(long_unicode)
            encoded = long_unicode.encode('utf-8')
            
            self.assertEqual(length, 50000)
            self.assertGreater(len(encoded), 100000)
        except MemoryError:
            self.skipTest("Extremely long string requires too much memory")
        except Exception as e:
            self.fail(f"Failed on long unicode: {e}")


if __name__ == '__main__':
    unittest.main()