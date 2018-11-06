import logging
LOG_FORMAT = "【%(asctime)s】\n" \
             "路径：%(pathname)s\n" \
             "文件：%(filename)s\n" \
             "行号：%(lineno)d\n" \
             "函数：%(funcName)s\n" \
             "级别：%(levelname)s\n" \
             "内容：%(message)s\n"
DATE_FORMAT = "%Y.%m.%d.%H:%M:%S%p"

logging.basicConfig(filename='my.log',
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt=DATE_FORMAT)

def test_log():
    logging.debug("This is a debug log.")
    logging.info("This is a info log.")
    logging.warning("This is a warning log.")
    logging.error("This is a error log.")
    logging.critical("This is a critical log.")



test_log()


c='传递一个参数试试'
logging.info("Test: %s",c)