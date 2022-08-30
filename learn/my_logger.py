import logging


class MyLogger(logging.Logger):

    def __init__(self, name,  level=logging.INFO, file=None):
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


logger = MyLogger("wxzy", file="my_logger.log")

if __name__ == '__main__':
    mlogger = MyLogger("wxzy", file="my_logger.log")
    mlogger.info("测试，我自己封装的日志类！！！！")

