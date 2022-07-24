import logging

logger = logging.getLogger('无限主义')
# 配置日志名称

logger.setLevel(logging.INFO)
# 配置日志输出级别

handle1 = logging.StreamHandler()
# 配置日志输出在那些渠道

fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d行: %(message)s'
formatter = logging.Formatter(fmt)
# 设置渠道输出内容格式

handle1.setFormatter(formatter)
# 将日志格式绑定到渠道中

logger.addHandler(handle1)
# 将设置好的渠道，添加到日志收集器上

logger.info('111')






