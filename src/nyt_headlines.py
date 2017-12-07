'''
In this module, I will use BeautifulSoup to get all headlines from the New York Times homepage.

Created on Nov 24, 2017

@author: connorfairman
'''

from bs4 import BeautifulSoup
import urllib2
from datetime import datetime
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day+1, hour=1, minute=30, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def writeTitles():
    nytFile = urllib2.urlopen("https://www.nytimes.com/")
    nytHtml = nytFile.read()
    nytFile.close()
    
    # Open a file for writing
    file_object = open("nytHeadlines.txt", "a")
    
    soup = BeautifulSoup(nytHtml, "html.parser")
    for title in soup.find_all(class_="story-heading"):
        if title.a:
            file_object.write(title.a.text.encode('utf-8') + '\n')
            print(title.a.text)
    file_object.write("-------------------------------------------------------------------------------------------------- \n")
    file_object.write("-------------------------------------------------------------------------------------------------- \n")
    file_object.write("------------------------------------------------" + x + "----------------------------------------- \n")
    file_object.write("-------------------------------------------------------------------------------------------------- \n")
    file_object.write("-------------------------------------------------------------------------------------------------- \n")
    file_object.write("-------------------------------------------------------------------------------------------------- \n")        
    file_object.close()
    
t = Timer(secs, writeTitles)
t.start()










