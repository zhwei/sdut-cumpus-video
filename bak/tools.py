#!/usr/bin/python2.7
# -*- coding: gbk -*-


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from datetime import datetime

# print str(datetime.now())[:10]

import codecs
import chardet


# gbk_file = codecs.open('sources/Total.xml','r')

# encd =  chardet.detect(gbk_file.readlines()[1])['encoding']
#
# print encd

# print  gbk_file.read().encode(encd)
# for i in gbk_file.read():
#     print  chardet.detect(i)['encoding']
#     print i.decode(chardet.detect(i)['encoding'])

# print content
#
# file_name = "utf_file%s.xml" % str(datetime.now())[:10]
#
# print file_name
#
# utf_file = open('sources/utf_file.xml', 'a')


