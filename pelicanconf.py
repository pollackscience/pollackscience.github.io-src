#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Brian Pollack'
SITENAME = 'Data Briantist'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

DEFAULT_DATE = 'fs'

THEME = '/Users/brianpollack/Coding/Blog/pelican-themes/Flex'
SITELOGO = './images/harper_framed.jpg'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('home', '/'),
         ('PollackScience', 'http://pollackscience.com'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/brianleepollack/'),
          ('github', 'https://github.com/pollackscience'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images']


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# For pelican-ipynb
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored.
IGNORE_FILES = [".ipynb_checkpoints"]
# IPYNB_USE_METACELL = True
# IPYNB_SKIP_CSS=True
# IPYNB_EXPORT_TEMPLATE = "./nb.tpl"

