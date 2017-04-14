import spice_api as spice
from bs4 import BeautifulSoup
import urllib.request
import timeit
import re
import os

def findTopGenre():
    o=0
    i=1
    for id in animeIDList:
        if (o > animeaccuracy):
            break
        basicurl = "https://myanimelist.net/anime/"
        url = basicurl + str(id) + "/"
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page.read(), "html.parser")
        text = soup.get_text()

        iterator = iter(text.splitlines())
        for line in iterator:
            if "Genre" in line:
                currentgenre = [x.strip() for x in next(iterator).split(',')]
                # problem is it loops around incrementing
                for genre in currentgenre:
                    if genre in genrelist:
                        location = genrelist.index(genre)
                        genrecount[location] += 1
                    if genre not in genrelist:
                        genrelist.append(genre)
                        genrecount.append(1)
        i += 1
        o += 1

def suggestFile():
    count = 0
    for topgenre in genrelist:
        print("---------------------------------------------")
        print(str(genrelist[count]) + " RECCOMENDATIONS:")
        print("---------------------------------------------")
        with open('dist/cache/' + topgenre + ".txt") as f:
            toplist = f.read().splitlines()
        oldSet = set(animeNamesList)
        newSet = set(toplist)
        removedElements = oldSet - newSet
        newElements = newSet - oldSet
        mc = 0
        for element in newElements:
            if (mc < maxSuggestion):
                results = spice.search(element, spice.get_medium('anime'), creds)
                if (results):
                    print(str(element) + " https://myanimelist.net/anime/" + results[0].id + "/")
                    mc += 1
            else:
                break
        toplist.clear()
        count += 1

username='eternal_atom'
maxSuggestion=maxgenre=5
animeaccuracy=5

# VARIABLES
# Used for indexing the MALGENRE URL
MALGENRE=["Action","Adventure","Cars","Comedy","Dementia","Demons","Mystery","Drama","Ecchi","Fantasy","Game","Hentai","Historical","Horror","Kids","Magic","Martial Arts","Mecha","Music","Parody","Samurai","Romance","School","Sci-Fi","Shoujo","Shoujo-Ai","Shounen","Shounen-Ai","Space","Sports","Super Power","Vampire","Yaoi","Yuri","Harem","Slice Of Life","Supernatural","Military","Police","Psychological","Thriller","Seinen","Josei"]
creds = spice.init_auth('SuggestionB0t182',"linkBlink@182")
rawUserList = spice.get_list(spice.get_medium('anime'),username, creds)
animeIDList=rawUserList.get_ids()
animeNamesList=rawUserList.get_titles()
genrelist=[]
genrecount=[]
i=0
o=0
animeaccuracy=(len(animeNamesList) * (.1 * animeaccuracy))
print("")
print("Processing request based on the genres of " + str(animeaccuracy) + " anime you watched.")

start = timeit.default_timer()


findTopGenre()

# Sorting the genres out
genrelist = ([x for (y, x) in sorted(zip(genrecount, genrelist))])
genrelist.reverse()
genrelist= genrelist[:maxgenre]
print(genrelist)
##making suggestions based on file.

recs= [[] for i in range(maxgenre)]
suggestFile()
stop = timeit.default_timer()
print(stop - start)

something=input("Hit the key then enter to quit, enjoy watching some good stuff :)")