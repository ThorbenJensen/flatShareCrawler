#/usr/bin/env python

from bs4 import BeautifulSoup as bs
#from lxml import etree
import six
from html5lib import html5parser
import urllib2

url = "http://www.wg-gesucht.de/wg-zimmer-in-Wuppertal.142.0.0.0.html"
#url = "http://www.pythonforbeginners.com"

html = urllib2.urlopen(url)
soup = bs(html)

#print(soup)
print(soup.findAll('a'))

#elem = soup.findAll('a', {'title': 'title here'})
#elem[0].text


