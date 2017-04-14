from bs4 import BeautifulSoup
import urllib.request


basicurl = "https://myanimelist.net/anime/"
url = basicurl + "1" + "/"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")
text = soup.get_text()
print(text)