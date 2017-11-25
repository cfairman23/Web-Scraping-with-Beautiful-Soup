'''
In this module, I will use BeautifulSoup to get all headlines from the New York Times homepage.

Created on Nov 24, 2017

@author: connorfairman
'''

from bs4 import BeautifulSoup
import urllib2

nytFile = urllib2.urlopen("https://www.nytimes.com/")
nytHtml = nytFile.read()
nytFile.close()

soup = BeautifulSoup(nytHtml, "html.parser")
nytAll = soup.find_all("a")
for title in soup.find_all(class_="story-heading"):
    if title.a:
        print(title.a.text)