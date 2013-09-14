#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import urllib

URL = "http://10.18.1.1/"

class Films:

    tree = ET.ElementTree(file='sources/total.xml')
    root = tree.getroot()

    def __init__(self):
        pass

    def get_text(self, film, tag):

        for elem in film:
            if elem.tag == tag:
                return elem.text
            else:
                continue
        return False

    def get_film(self, film_id):

        for film in self.root:
            if self.get_text(film, 'b') == film_id:
                return film

        # for elem in slef.tree.iterfind('branch/sub-branch')

    def get_name(self, film):

        return self.get_text(film, 'a')

    def get_list(self, film, tag_list):

        """
        ji ---- h
        id  ---- b
        time ---- t
        """
        text_list = []

        for tag in tag_list:
            text_list.append(self.get_text(film,tag))

        text_tuple  = tuple(text_list)

        return text_tuple

    def get_link(self, film, ji_get=0):
        ji, film_id, time = self.get_list(film, ('h', 'b', 't'))
        name = self.get_name(film)

        if ji == '1' or ji == '0':
            ji = '0'
        elif int(ji) >= int(ji_get):
            ji = str(int(ji_get) -1)
        else:
            # print ji, '-------'
            return False

        link = "%sxy_new.asp?a=%s&b=%s&time=%s" % (URL, ji, film_id, time.replace(' ',''))

        html = urllib.urlopen(link).read()
        #d_link = html[4:-3]
        import re
        try:
            d_link = re.compile(r'[a-zA-z]+://[^\s|\|]*').findall(html)[0]
            return (name, d_link)
        except IndexError:
            return False


    def search(self, keywords, t):
        """
        search function
        t is the type of the keywords
        """
        pass


    def get_film_list(self, tag, tag_content):

        '''
        name - a
        id   - b
        ji   - h
        link - by self
        '''

        film_list = []

        for film in self.tree.iter(tag='film'):

            #if self.get_text(film, tag) == tag_content.decode('utf-8'):
            #print self.get_text(film, str(tag)), '---',tag_content.decode('utf-8')
            if str(tag_content.decode('utf-8')) in str(self.get_text(film, tag)):
                tuple_films = self.get_list(film, ('a','b','h', 'e', 's'))
                film_list.append(tuple_films)
            else:
                continue

        return tuple(film_list)


    def get_tag_list(self, tag):

        tag_list = []
        for tag in self.tree.iter(tag=tag):
            try:
                text = tag.text.encode('utf-8')
            except AttributeError:
                text = text

            text_list = text.replace(' ',',').split(',')

            tag_list = tag_list + text_list

        tag_list = list(set(tag_list))

        return tuple(tag_list)




# def get_film(film_id):
#
#     url = "%s/mov/%s/film.xml" % (URL, film_id)
#
#     html = urllib.urlopen(url).read()
#     f_name = 'sources/films/%s.xml' % film_id
#     film_file = open(f_name, 'wb')
#     film_file.write(html)
#     film_file.close()
#
#     tree = ET.ElementTree(file=f_name)
#
#     return tree
#
# print get_film(film_id='687474703A2F2F6D382E6E65746B75752E636F6D2F672F6C786A2F62616F646172656E6C61696C652F2A2A2E6D6B76')


















