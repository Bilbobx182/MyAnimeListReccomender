from bs4 import BeautifulSoup
import urllib.request
import re

MALGENRE=["Action","Adventure","Cars","Comedy","Dementia","Demons","Mystery","Drama","Ecchi","Fantasy","Game","Hentai","Historical","Horror","Kids","Magic","Martial Arts","Mecha","Music","Parody","Samurai","Romance","School","Sci-Fi","Shoujo","Shoujo-Ai","Shounen","Shounen-Ai","Space","Sports","Super Power","Vampire","Yaoi","Yuri","Harem","Slice Of Life","Supernatural","Military","Police","Psychological","Thriller","Seinen","Josei"]
MALGENREURL='https://myanimelist.net/anime/genre/'

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def getTopOfGengre(genrenum):
    url = MALGENREURL + str(genrenum) + "/"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")
    content = []
    string = ''
    whiteSeperator = 0
    for node in soup.findAll(attrs={'class': re.compile(r".*\bseasonal-anime js-seasonal-anime\b.*")}):
        # content.append(cleanhtml(str(node)))
        temp = str(node)
        temp = cleanhtml(temp)
        temp = temp.replace('\n', ' ').replace('\r', '').replace(',', '').replace(' Watch Video ', '').replace(
            ' Watch Promotional Video ', '')
        for i in range(0, len(temp)):
            if (temp[i] == ' '):
                whiteSeperator += 1
            else:
                whiteSeperator = 0

            if whiteSeperator == 3:
                content.append(temp[:i - 2])
                break
    return content

count=1
for genre in MALGENRE:
    print("Working on "+genre)
    dir='dist/cache/'+genre+'.txt'
    print(dir)
    currentcache=getTopOfGengre(count)
    print(currentcache)
    with open(dir, mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(currentcache))
    count+=1