import os

MALGENRE = ["Action", "Adventure", "Cars", "Comedy", "Dementia", "Demons", "Mystery", "Drama", "Ecchi", "Fantasy",
            "Game", "Hentai", "Historical", "Horror", "Kids", "Magic", "Martial Arts", "Mecha", "Music", "Parody",
            "Samurai", "Romance", "School", "Sci-Fi", "Shoujo", "Shoujo-Ai", "Shounen", "Shounen-Ai", "Space", "Sports",
            "Super Power", "Vampire", "Yaoi", "Yuri", "Harem", "Slice Of Life", "Supernatural", "Military", "Police",
            "Psychological", "Thriller", "Seinen", "Josei"]


def getCachedGenreContents(genreNum):
    # File path locations for where we want to open stuff.
    basePath = os.path.dirname(__file__)
    cacheLocation = "dist/cache/"
    fullPath = os.path.join(basePath, cacheLocation)

    try:
        f = open(fullPath + "/" + MALGENRE[genreNum] + '.txt', encoding="utf8")
        contents = f.readlines()
        f.close()
        return contents
    except IOError as e:
        print('FAILURE LOADING')
        return "ERROR"


rawList = getCachedGenreContents(0)
print(rawList)
