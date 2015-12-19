#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u''
SITENAME = u'21\u5929\u5b66\u901aErlang'
SITEURL = ''

PLUGINS = ['i18n_subsites']

PATH = 'content'
THEME = 'theme'

TIMEZONE = 'Asia/Shanghai'

USE_FOLDER_AS_CATEGORY = False

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
CATEGORY_SAVE_AS = False
CATEGORIES_SAVE_AS = False
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
TAG_SAVE_AS = False
TAGS_SAVE_AS = False

# i18n

DEFAULT_LANG = u'zh-cn'

I18N_SUBSITES = {
    'en': {
        'SITENAME': 'Teach Yourself Erlang in 21 days',
        }
    }

languages_lookup = {
  'en': 'English',
  'zh-cn': '简体中文',
}

DATE_FORMATS = {
  'en': '%a, %d %b %Y',
  'zh-cn': '%Y年%m月%d日',
}


def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]

JINJA_FILTERS = {
  'lookup_lang_name': lookup_lang_name,
}


# Feed generation is usually not desired when developing
FEED_ATOM = 'feeds.atom'
FEED_RSS = 'feeds.rss'
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = None
SOCIAL = None

I18N_MENUITEMS = {
  'en': (),
  'zh-cn': (('获取最新版本', '/book/'),)
}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
