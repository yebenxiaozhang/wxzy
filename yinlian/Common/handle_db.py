"""
======================
Author: 潘师傅
Time: 2022-11-09 17:03
Project: wxzy
Company: 无限主义
======================
"""
from Common.handle_config import conf
import pymysql
"""
1、数据库连接 conn  cur
2、获取一条数据？
3、获取条数
4、获取所有的数据
5、关闭数据库连接
"""


class HandleDB:

    def __init__(self):
        # 连接数据库，创建游标。
        # 1、建立连接
        self.conn = pymysql.connect(
            host=conf.get("mysql", "host"),
            port=conf.getint("mysql", "port"),
            user=conf.get("mysql", "user"),
            password=conf.get("mysql", "password"),
            database=conf.get("mysql", "database"),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        # 2、创建游标
        self.cur = self.conn.cursor()

    def select_one_data(self, sql):
        """
        获取第一条数据
        :param sql:
        :return:
        """
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def select_all_data(self, sql):
        """
        获取所有数据
        :param sql:
        :return:
        """
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def get_count(self, sql):
        """
        获取条数
        :param sql:
        :return:
        """
        self.conn.commit()
        return self.cur.execute(sql)

    def update(self, sql):
        """
        对数据库进行增、删、改的操作。
        :param sql:
        :return:
        """
        self.cur.execute(sql)
        self.conn.commit()

    def close(self):
        """
        关闭游标、关闭数据库链接
        :return:
        """
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    # sql = 'select * from goods LIMIT 3'
    # db = HandleDB()
    # count = db.get_count(sql)
    # print("结果个数为：",count)
    # data = db.select_one_data(sql)
    # print("一条数据：",data)
    # all = db.select_all_data(sql)
    # print("所有的数据：",all)
    # db.close()
    # 初始化数据库对象
    db = HandleDB()
    sql = 'select * from usr_member where phone = "19859080323"'
    # 发起一个登录请求
    from Common.handle_requests import send_requests
    case = {
        "method": "POST",
        "url": "https://test.quanxianglife.cn/api/auth/authentication/mobile",
        "request_data": {
                        "appId": "wxdb8f809214c26e2e",
                        "type": "moblile",
                        "mobile": "19859080323",
                        "smsCode": "1"}}
    response = send_requests(case["method"], case["url"], case["request_data"])  # 接口
    print("响应结果：", response.json())
    # 查询注册的手机号码
    count = db.get_count(sql)
    print("获取到的结果为：", count)


