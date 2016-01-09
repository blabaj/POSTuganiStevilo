#!/usr/bin/env python

import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


def ugani(st):
    if st == 8:
        return "Vpisal si pravilno stevilo!"
    else:
        return "Vec srece v naslednjem poskusu!"



class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("uganiStevilo.html")
    def post(self):
        stevilo = self.request.get("steviloVnos")
        stevilo = stevilo.strip(' ')
        stevilo = int(stevilo)
        zapis = ugani(stevilo)

        podatki = {"rezultat":zapis}
        return self.render_template("uganiStevilo.html", podatki)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)