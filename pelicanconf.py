#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yogeswaran Thulasidoss'
SITENAME = u"Yogi's corner"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Planet Python', 'http://planetpython.org/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/yogeswarant'),
        ('github', 'https://github.com/yogeswarant'),
        ('LinkedIn', 'https://in.linkedin.com/in/yogeswaran-thulasidoss-ab29a22a'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags.html'

#bootstrap customization
STATIC_PATHS = ['extras/custom.css']
EXTRA_PATH_METADATA = {
'extras/custom.css': {'path': 'static/custom.css'}
}
CUSTOM_CSS = 'static/custom.css'


# theme settings
THEME='themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'cosmo' #'lumen' #'sandstone' #'cosmo'
PYGMENTS_STYLE = 'monokai'
ABOUT_ME = 'Passionate programmer.  Proud father.  Prospective agriculturist.'
SITELOGO = 'images/logo.jpeg'
SITELOGO_SIZE = 24
FAVICON = 'images/logo.jpeg'

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

# plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['simple_footnotes', 'extract_toc', 'feed_summary']
FEED_USE_SUMMARY = True
SUMMARY_MAX_LENGTH = 100

MD_EXTENSIONS = ['toc', 'fenced_code', 'codehilite(css_class=highlight)', 'extra']

#PLUGINS = PLUGINS + ['disqus_static']
#DISQUS_SITENAME = 'everyogi-in'
ADDTHIS_PROFILE ='ra-5800fd37485cdfec'
ADDTHIS_DATA_TRACK_ADDRESSBAR = False
