#/usr/bin/env python

from bs4 import BeautifulSoup as bs
#from lxml import etree
import six
from html5lib import html5parser
import urllib2
import re

debug = 1

## gets an url and returns a set of the found advertisement IDs
def urlToIds(url):

    if debug == 1:
        print "Getting IDs from url: " + url

    # get page source
    html = urllib2.urlopen(url)
    soup = bs(html)
    isBlocked(soup.getText())

    # fill set 'ids' with IDs
    ids = set()    # IDs for url
    tags1 = soup.findAll("a", "list listenansicht0 ")
    tags2 = soup.findAll("a", "list listenansicht1 ")
    for tag in tags1 + tags2:
        ids.add( tag["href"] )

    if debug == 1:
        ids2 = set()
        tags3 = soup.findAll("a", "list   ")
        for tag in tags3:
            ids2.add( tag["href"] )
        print "ids2:"
        print ids2
        print "ids:"
        print ids

    return ids

## test if ID is active
def isActive(ID):

    print "Checking if link http://www.wg-gesucht.de/"+ ID + " is active."

    # get source
    url = "http://www.wg-gesucht.de/" + ID
    html = urllib2.urlopen(url)
    source = html.read()

    # if source contains statement of inactivity: it's inactive
    if source.count("der Inserent hat bereits genug Anfragen erhalten") == 0:
        return True
    else:
        return False

## get properties for ID
def idProps(ID):
    # get source
    url = "http://www.wg-gesucht.de/" + ID
    html = urllib2.urlopen(url)
    soup = bs(html)
    isBlocked(soup.getText())
    # get date and square meters
    main_data = soup.find("h2", "ang_detail_main_data").getText()
    miete = re.search( r'miete: \d+', main_data ).group(0).replace("miete: ","")
    qm = re.search( r'e: \d+m', main_data ).group(0).replace("e: ","").replace("m","")
    # get date
    source = soup.getText()
    date = re.search( r'\d\d.\d\d.\d\d\d\d', source ).group(0)
    
    return [miete, qm, date]

## check if blocked
def isBlocked(source):
    if source.count("Besondere Bedingungen zur Datenbankabfrage") > 0:
        print "Access is blocked!"
        return True
    else:
        return False

## get all active IDs
url = "http://www.wg-gesucht.de/wg-zimmer-in-Wuppertal.142.0.0.15.html"
ids = urlToIds(url)

# TODO: wrong results for page 15 (retrieved results are from page 1)

# check if all are active
#all_active = True
#for ID in ids:
#    if isActive(ID):
#        print ID + " is active!"
#    else:
#        print ID + " is NOT active!"
#        all_active = False
#        break

#print all_active





