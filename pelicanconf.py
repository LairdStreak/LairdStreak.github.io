#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Laird Streak'
SITENAME = 'Laird Streak`s Blog'
SITEURL = 'https://LairdStreak.github.io'
ARCHIVES_SAVE_AS = 'archives.html'
# GITHUB_URL = 'https://github.com/lairdstreak/'
USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = True

PATH = 'content'

TIMEZONE = 'Pacific/Auckland'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'

# Blogroll
# LINKS = (('Creality', 'https://www.creality.com/'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/laird.streak.3'),
          ('Twitter', 'https://twitter.com/lairdstreak'),
          )

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
  
# THEME = "notmyidea-cms"
DISQUS_SITENAME = "https://lairdstreak-github-io.disqus.com"

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME = True
DISPLAY_MENU = True
GOOGLE_ANALYTICS = True


# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
TAGS_URL = 'tags'
TAGS_SAVE_AS = 'tags/index.html'
AUTHORS_URL = 'authors'
AUTHORS_SAVE_AS = 'authors/index.html'
CATEGORIES_URL = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL = 'archives'
ARCHIVES_SAVE_AS = 'archives/index.html'

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ('Tags', TAGS_URL, TAGS_SAVE_AS),
    ('Authors', AUTHORS_URL, AUTHORS_SAVE_AS),
    ('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)
# additional menu items
# MENUITEMS = (
#     ('My GitHub', 'https://github.com/'),
#     ('Linux Kernel', 'https://www.kernel.org/'),
# )
