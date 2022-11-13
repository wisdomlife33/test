import unittest
from binarySearch import binary_search
from unittestreport import TestRunner


class TestBinarySearch(unittest.TestCase):
    # equivalence partitioning testing --all data is numbers
    # boundary value testing  --none set
    def test_case9(self):
        arr = []
        self.assertEqual(binary_search(arr, 2), -1)

    # boundary value testing  --lef boundary
    def test_case1(self):
        arr = [104, 185, 219, 253, 313, 351, 412, 434, 518, 572, 626, 662, 674, 679, 736, 802, 825, 877, 923, 980]
        self.assertEqual(binary_search(arr, 103), -1)
    #
    # # boundary value testing  --lef boundary
    # def test_case2(self):
    #     arr = [104, 185, 219, 253, 313, 351, 412, 434, 518, 572, 626, 662, 674, 679, 736, 802, 825, 877, 923, 980]
    #     self.assertEqual(binary_search(arr, 104), 0)
    #
    # # boundary value testing  --middle boundary
    # def test_case3(self):
    #     arr = [104, 185, 219, 253, 313, 351, 412, 434, 518, 572, 626, 662, 674, 679, 736, 802, 825, 877, 923, 980]
    #     self.assertEqual(binary_search(arr, 572), 9)
    #
    # # boundary value testing  --middle boundary
    # def test_case4(self):
    #     arr = [104, 185, 219, 253, 313, 351, 412, 434, 518, 572, 626, 662, 674, 679, 736, 802, 825, 877, 923, 980]
    #     self.assertEqual(binary_search(arr, 518), 8)
    #
    # # boundary value testing  --middle boundary
    # def test_case5(self):
    #     arr = [104, 185, 219, 253, 313, 351, 412, 434, 518, 572, 626, 662, 674, 679, 736, 802, 825, 877, 923, 980]
    #     self.assertEqual(binary_search(arr, 626), 10)
    #
    # # boundary value testing  --right boundary
    # def test_case6(self):
    #     arr = [104, 185, 219, 253, 313, 351, 412, 434, 518, 572, 626, 662, 674, 679, 736, 802, 825, 877, 923, 980]
    #     self.assertEqual(binary_search(arr, 980), 19)
    #
    # # boundary value testing  --right boundary
    # def test_case7(self):
    #     arr = [104, 185, 219, 253, 313, 351, 412, 434, 518, 572, 626, 662, 674, 679, 736, 802, 825, 877, 923, 980]
    #     self.assertEqual(binary_search(arr, 981), -1)
    #
    # # equivalence partitioning testing --all data is letters
    # def test_case8(self):
    #     arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
    #     self.assertEqual(binary_search(arr, 'c'), 2)

if __name__ == '__main__':
    case = unittest.defaultTestLoader.discover(r'D:\test',pattern='binaryDecisionSearchTest.py')
    runner = TestRunner(case, tester="chenjun", filename="chenjunreport", report_dir=r"D:\test", title="chenjunreport",
                        templates=1,desc="CSE565 Task1")
    runner.run()