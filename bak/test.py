#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jiexi import Films


fff = Films()
#
#
# a = fff.get_film(id='687474703A2F2F6D392E6E65746B75752E636F6D2F662F7A792F6665696368656E67777572616F32303133303831302F312E6D6B76')
# print fff.get_link(a)[1][-3:]
# # for

#for i in fff.root:
#    u = fff.get_link(i)
#    print u[1]
#    if  u[1][-3:] !='mkv':
#        print  u[0], '----------', u[1]
#

#print fff.get_film('687474703A2F2F6D382E6E65746B75752E636F6D2F472F64792F78696F6E676C696E676A696171692F312E6D6B76')

# t = fff.get_film_list(tag='e', name='历史' )

# print t

# for i in t:
# 	print fff.get_name(i)

for i in fff.get_tag_list('e'):
	print '--',i,'++++'
	# pass
