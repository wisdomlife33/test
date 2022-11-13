import unittest
from binarySearch import binary_search
from unittestreport import TestRunner


        
class TestBinarySearch2(unittest.TestCase):

    # boundary value testing  --lef boundary
    def test_case2(self):
        arr = [104, 185, 219, 253, 313, 351, 412, 434, 518, 572, 626, 662, 674, 679, 736, 802, 825, 877, 923, 980]
        self.assertEqual(binary_search(arr, 103), -1)

if __name__ == '__main__':
    case = unittest.defaultTestLoader.discover(r'D:\test',pattern='binaryDecisionSearchTest2.py')
    runner = TestRunner(case, tester="chenjun", filename="chenjunreport", report_dir=r"D:\test", title="chenjunreport",
                        templates=1,desc="CSE565 Task1")
    runner.run()