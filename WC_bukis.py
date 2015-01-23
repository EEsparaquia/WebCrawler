#! Python

#	This Web Crawler is for read all Bukis
#	songs from the site http://www.lyricsmode.com
#	
#	1.- Read the "search" in the url to choose the
#	artist.
# 	2.- Collect all the songs by href tag, fallow them
#	and extract all the songs.
#	3.- Using regular expressions extract the quotes of the
#	songs.



# 	http://www.lyricsmode.com/search.php?search=marco%20antonio%20solis
import re
import requests
from bs4 import BeautifulSoup

print(''' 
 _______________________
< Handle with carefully >
 -----------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||----w |
                ||     ||
''')

url = "http://www.lyricsmode.com/search.php?search=marco%20antonio%20solis"
url_composer = ['http://www.lyricsmode.com']
extension = ['.html']
arr_names = []
arr_links = []
arr_url = []
urls = []

r = requests.get(url)
soup = BeautifulSoup(r.content)
hrefs = soup.find_all("table", {"class":"songs_list"})


for links in hrefs:
	name_link = links.find_all("a", {"class":"b search_highlight"})
	
	for ref in name_link:
		resultado1 = re.findall('href="(.*?).html"', str(ref))
		arr_names.append(resultado1)

for x in range(0,len(arr_names)):
	arr_links.append(url_composer+arr_names[x]+extension)
	arr_url = ''.join(arr_links[x])
	urls.append(arr_url) 

#for y in range(0, len(urls)):
for y in range(0, 1):
	print urls[y]
	rr = requests.get(urls[y])
	sopa = BeautifulSoup(rr.content)
	songs = sopa.find_all("p", {"id":"lyrics_text"})

	for texto in songs:
		appendMe = texto.text
		print appendMe
		'''
		saveFile = open('url_composer.txt', 'w')
		saveFile.write('\n')
		saveFile.write(appendMe)
		saveFile.close()
		'''