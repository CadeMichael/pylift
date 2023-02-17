import unittest
from lib.lift import Lift


class TestFileManagment(unittest.TestCase):
    """Test the lib/filemanager.py classes."""

    def testVolume(self):
        lift = Lift("2-12-23", [[1, 2, 3]])
        self.assertEqual(6, lift.volume())

    def testRelInt(self):
        lift = Lift("2-12-23", [[200, 10, 1], [200, 9, 2]])
        self.assertEqual(88.9, lift.rel_int(300))
