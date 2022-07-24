import unittest


class Test_unittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('所有用例执行前 执行的')

    @classmethod
    def tearDownClass(cls) -> None:
        print('所有用例执行完成后，执行的')

    def setUp(self) -> None:
        print('每条用例执行前')

    def tearDown(self) -> None:
        print('每条用例执行后')

    def test_001(self):
        print('用例1')

    def test_002(self):
        print('用例2')


if __name__ == '__main__':
    unittest.main()
