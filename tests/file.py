import unittest
import lib.filemanager as fm
from lib.lift import Lift
import csv


class TestFileManagment(unittest.TestCase):
    """Test the lib/filemanager.py classes."""

    def testNewLift(self):
        self.assertEqual(
            fm.create_lift("test", "tests/lifts"), "New lift test.csv written."
        )

    def testReadLift(self):
        self.assertEqual(fm.read_lift("test", "tests/lifts"), [])
        self.assertEqual(fm.read_lift("none", "tests/lifts"), "No file none.csv")

        with open("tests/lifts/test.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            rows = [["2-12-23"], ["120", "8", "3"]]
            writer.writerows(rows)

        self.assertEqual(
            fm.read_lift("test", "tests/lifts"), [["2-12-23"], [120.0, 8.0, 3.0]]
        )

    def testMakeLiftList(self):
        man_lift = Lift("2-12-23", [[120.0, 8.0, 3.0]])
        test_lift = fm.make_lift_list("test", "tests/lifts")[0]
        no_lift = fm.make_lift_list("none", "tests/lifts")

        self.assertEqual(man_lift.date, test_lift.date)
        self.assertEqual(man_lift.sets, test_lift.sets)
        self.assertEqual(no_lift, [])
