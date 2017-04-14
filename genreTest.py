import os
for dirName, subdirList, fileList in os.walk(os.getcwd()):
    if("cache" in dirName):
        print("in cache")
        print(dirName)
        for fname in fileList:
            print(fname)
            if("Police" in fname):
                with open(dirName + "\\Police.txt", "r") as f:
                    content= f.readlines()
for item in content:
    print(item)




'''

username=input('Enter username:')
try:
    maxSuggestion = int(input('How many suggestion per genre (Enter 999 for max):'))
    maxgenre = int(input('How many genres you want recommendations for:'))
    print("HINT: If you watch a lot of anime(ie 100+)try low values in the next part")
    animeaccuracy = int(input('Enter how accurate you want it on a scale of 1-10:'))
    if animeaccuracy < 1 or animeaccuracy >10:
        quit()
except ValueError:
   print("That's not an number!")



'''