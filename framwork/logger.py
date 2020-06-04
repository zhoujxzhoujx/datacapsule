# coding = utf-8
import logging
import logging.config
import os


class MyLog:
    CONF_LOG = os.path.dirname(os.path.dirname(__file__)) + '/config/log_config.ini'

    def get_log(self, name):
        logging.config.fileConfig(self.CONF_LOG)
        logger = logging.getLogger(name)
        return logger

if __name__ == '__main__':
    mylog = MyLog()
    logger = mylog.get_log('myAutoTest')
    logger.info('啊')
    logger.debug('en')
    logger.debug('a')
    logger.info('b')
