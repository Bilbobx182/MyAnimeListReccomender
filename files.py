import re
import os
import datetime
import urllib
from bs4 import BeautifulSoup

def genCacheDate():
    i = datetime.datetime.now()
    file = open("modifiedSince.txt", "w")
    file.write(str(i))
    file.close()

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def cacheTest():
    cachename='CreateCache.py'
    # If it's not there make the cache
    if not os.path.isfile(cachename):
        print("Generating Cache")
        genCacheDate()
    # otherwise compare the dates
    try:
        mtime = os.path.getmtime(cachename)
        last_modified_date = datetime.datetime.fromtimestamp(mtime)
        i = datetime.datetime.now()
        diff=i-last_modified_date
        temp=str(diff)
        temp=[x.strip() for x in temp.split(',')]
        actualdiff=temp[0]
        actualdiff=int(actualdiff[:-5])
        if(actualdiff>30):
            updateCache()
    except OSError:
        mtime = 0




cacheTest()
