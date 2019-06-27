import json
import logging
from logging import handlers
import time
import os

class Logger(object):
    def __init__(self, default_path="logging.json", default_level=logging.INFO, env_key="LOG_CFG"):
        """
        Use the specified filename for streamed logging
        """
        path = default_path
        value = os.getenv(env_key, None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path, "r") as f:
                config = json.load(f)
                logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)

        logger = logging.getLogger('standard')  # 生成一个log实例
        logger.info('It works!')  # 记录该文件的运行状态
        return logger
        # # 初始化logger
        # logger = logging.getLogger()
        # # 配置日志级别，如果不显示配置，默认为Warning，表示所有warning级别已下的其他level直接被省略，
        # # 内部绑定的handler对象也只能接收到warning级别以上的level，你可以理解为总开关
        # logger.setLevel(logging.INFO)
        #
        # formatter = logging.Formatter(fmt="%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s - %(message)s",
        #                               datefmt="%m/%d/%Y %I:%M:%S %p")  # 创建一个格式化对象
        #
        # console = logging.StreamHandler()  # 配置日志输出到控制台
        # console.setLevel(logging.WARNING)  # 设置输出到控制台的最低日志级别
        # console.setFormatter(formatter)  # 设置格式
        # logger.addHandler(console)

    def setup_logging(default_path="logging.json", default_level=logging.INFO, env_key="LOG_CFG"):
        path = default_path
        value = os.getenv(env_key, None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path, "r") as f:
                config = json.load(f)
                logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)


    def func():
        logging.info("start func")

        logging.info("exec func")

        logging.info("end func")
