#!/usr/bin/env python
import os.path
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options


# application settings and handle mapping info
class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/([^/]+)?", MainHandler)
		]
		settings = dict(
			page_title=u'Deployed!',
			debug=True,
		)
		tornado.web.Application.__init__(self, handlers, **settings)


# proof that your deploy worked
class MainHandler(tornado.web.RequestHandler):
	def get(self, phrase):
		self.write("""<html><body><h1>Deploy successful!</h1><p>You just deployed to Heroku using an Arduino and a few scraps of Python!  Isn't that exciting?</p></body></html>""")


# kick it off
def main():
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(os.environ.get("PORT", 5000))
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()
