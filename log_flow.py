#!/usr/bin/env python
from logflow.utils import flow_logger as logger
from logflow.plugins.analyzers import analyzer
"""
LogFlow entry file
"""

if __name__ == "__main__":
    logger.i("main", "hello logger")
    logger.d("main", "hello logger")
    logger.w("main", "hello logger")
    logger.e("main", "hello logger")
    analyzer.call_analysis()
