from unittest.mock import MagicMock, patch
import unittest
import cve_analyzer
import json


class TestCVE(unittest.TestCase):
    @patch('cve_analyzer.get_cve')
    def test_get_cve(self, mock_get_cve):
        mock_data = json.load(open('metrics.json'))
        mock_get_cve.return_value = MagicMock()
        mock_get_cve.return_value.json.return_value = mock_data
        results = cve_analyzer.get_cve('CVE-2025-29927')
        results = results.json()
        print(results)
        self.assertFalse(True)



