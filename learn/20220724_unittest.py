import unittest
import ddt


datas = [
    {'name': '这是第一条用例'},
    {'name': '这是第二条用例'},
    {'name': '这是第三条用例'},
    {'name': '这是第四条用例'},
]


@ddt.ddt()
class test(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("这所有用例执行之前执行的")

    @classmethod
    def tearDownClass(cls) -> None:
        print("这是所有用例之前后 执行的 一般指的是收尾共工作/数据清理")

    def setUp(self) -> None:
        print('这是每一条用例执行前 执行的')

    def tearDown(self) -> None:
        print("这每条用例执行之后 执行的")

    @ddt.data(*datas)
    def test_01(self, case):
        """
        :return: 这个是用例描述
        """
        print(case["name"])

    def test_02(self):
        print('2')


if __name__ == '__main__':
    unittest.main()
