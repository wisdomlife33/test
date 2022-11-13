import unittest
from binarySearch import binary_search
from unittestreport import TestRunner


class TestBinarySearch1(unittest.TestCase):
    # equivalence partitioning testing --all data is numbers
    # boundary value testing  --none set
    def test_case1(self):
        arr = []
        self.assertEqual(binary_search(arr, 2), -1)


if __name__ == '__main__':
    case = unittest.defaultTestLoader.discover(r'D:\test',pattern='binaryDecisionSearchTest1.py')
    runner = TestRunner(case, tester="chenjun", filename="chenjunreport", report_dir=r"D:\test", title="chenjunreport",
                        templates=1,desc="CSE565 Task1")
    runner.run()