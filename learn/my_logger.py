import logging
from learn.handle_config import conf


class MyLogger(logging.Logger):

    def __init__(self, name,  level="INFO", file=None):
        # 设置输出级别、输出渠道、输出日志格式
        super().__init__(name, level)

        # 日志格式
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line：%(message)s'
        formatter = logging.Formatter(fmt)

        # 控制台渠道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        if file:
            # 文件渠道
            handle2 = logging.FileHandler(file,  encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)


# 是否需要写入文件
if conf.getboolean("log", "file_ok"):
    file_name = conf.get("log", "file_name")
else:
    file_name = None

logger = MyLogger(conf.get("log", "name"), conf.get("log", "level"), file_name)
# logger = MyLogger(file_name)

# logger.info("1111111111111111")

# logger = MyLogger("wxzy")

# if __name__ == '__main__':
#     mlogger = MyLogger("wxzy")
#     mlogger.info("测试，我自己封装的日志类！！！！")

