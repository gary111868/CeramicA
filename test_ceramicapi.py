# test_ceramicapi.py
"""
Tests for CeramicAPI module.
"""

import unittest
from ceramicapi import CeramicAPI

class TestCeramicAPI(unittest.TestCase):
    """Test cases for CeramicAPI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CeramicAPI()
        self.assertIsInstance(instance, CeramicAPI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CeramicAPI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
