#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import web
from web.contrib.template import render_jinja
from jiexi import Films
from autocache import memorize

urls = (
    '/', 'index',
    '/g/([0-9]+)/([0-9a-zA-Z]+)', 'get_video',
    '/t/([a-z]+)/(.*)', 'get_tag_films',
    '/comment', 'comment'
)


render = render_jinja('templates', encoding='utf-8')
app = web.application(urls, globals())
web.debug = True



class index():
    @memorize(10000)
    def GET(self):
        f=Films()

        video_type = f.get_tag_list(tag='g')

        diqu = f.get_tag_list(tag='f')
        juqing = f.get_tag_list(tag='e')

        return render.index(video_type=video_type, diqu=diqu,
            juqing=juqing)


class get_video:
    @memorize(10000)
    def GET(self, ji, video_id):

        print ji, video_id

        f = Films()
        # try:
        film = f.get_film(film_id=video_id)
        link = f.get_link(film, ji)

        ji_nu = int(f.get_text(film, 'h'))

        short_dec=f.get_text(film, 's')

        if ji_nu == 1:
            ji_all = None
        else:
            ji_all = range(1, ji_nu+1)

        return render.video(name=link[0], url=link[1],
                ji_all=ji_all, film_id=video_id, short_dec=short_dec)
        # except:
        #    raise web.notfound()

class get_tag_films:
    @memorize(10000)
    def GET(slef, tag, tag_contnet):

        f = Films()

        films = f.get_film_list(tag, tag_contnet)

        return render.films(films=films)


class comment:

    def GET(self):
        return render.comment()





if __name__ == "__main__":
    app.run()
