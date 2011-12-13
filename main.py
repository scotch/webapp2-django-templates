import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import webapp2
from webapp2 import Route


DEBUG = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

routes = [
    Route('/', handler='handlers.PageHandler:root', name='pages-root'),
    ]


application = webapp2.WSGIApplication(routes, debug=DEBUG, config={})