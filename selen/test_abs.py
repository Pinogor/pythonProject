# def test_abs1():
#    assert abs(-42) == 42, "asdfgh"
# def test_abs2():
#      assert abs(-42) == -42, "asdfgh"
# if __name__ == "__main__":
#     test_abs1()
#     test_abs2()
#     print("All test passed")
# import unittest
# class TestAbs(unittest.TestCase):
def test_abs1():
    assert abs(-42) == 42, "not ok"
def test_abs2():
    assert  abs (-42) == -42, 'not ok'
#     def test_abs1(self):
#         self.assertAlmostEqual(abs(-42), 42, "not ok")
#     def test_abs2(self):
#         self.assertAlmostEqual(abs(-42), -42, "not ok")
# if __name__ == "__main__":
#     unittest.main()