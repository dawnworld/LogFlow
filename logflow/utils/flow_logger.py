#!/usr/bin/env python
import sys
import logging

class FlowLogger(object):
    def __init__(self):
        self.logger = logging.getLogger('mylogger')  
        self.logger.setLevel(logging.DEBUG) 
        ch = logging.StreamHandler()  
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        return

    def __format(self, level, tag, m):
        return '{0} {1} : {2}'.format(level, tag, m)

    def d(self, tag, m):
        self.logger.debug(self.__format('D', tag, m))
        return

    def i(self, tag, m):
        self.logger.info(self.__format('I', tag, m))
        return

    def w(self, tag, m):
        self.logger.warn(self.__format('W', tag, m))
        return

    def e(self, tag, m):
        self.logger.error(self.__format('E', tag, m))
        return

sys.modules[__name__] = FlowLogger()
