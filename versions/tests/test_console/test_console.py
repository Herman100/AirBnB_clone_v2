#!/usr/bin/python3
import unittest
from console import HBNBCommand
from models import storage
from io import StringIO
from unittest.mock import patch


class TestDoCreate(unittest.TestCase):
    """Test the do_create function"""

    def setUp(self):
        """Set up for the tests"""
        self.console = HBNBCommand()

    def test_do_create(self):
        """Test creating an instance without parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)
            self.assertTrue("State" in storage.all())

    def test_do_create_with_params(self):
        """Test creating an instance with parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State name="California"')
            state = list(storage.all("State").values())[-1]
            self.assertEqual(state.name, "California")

    def test_do_create_with_invalid_params(self):
        """Test creating an instance with invalid parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State invalid_param')
            output = f.getvalue().strip()
            self.assertTrue("State" in storage.all())


if __name__ == '__main__':
    unittest.main()
