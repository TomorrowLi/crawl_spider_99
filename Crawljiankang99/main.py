#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/21 17:20
# @Author  : tomorrowli

import sys
import os
from scrapy.cmdline import execute
print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(['scrapy','crawl','99spider'])