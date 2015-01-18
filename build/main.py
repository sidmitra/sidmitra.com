"""
Note: This file is not used anywhere for now, because we serve the static out
directory directly.
"""
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class MainPage(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'


application = webapp.WSGIApplication(
    [('/', MainPage)],
    debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
