import urllib.request
import sys
import os
from domain import *


# download all urls, from a text, crawled by the  spider  crawler and save it into a local folder
def downlaod_mass(fileOfLinks):
    #crawled = os.path.join(directory, 'crawled.txt')

    file = open(fileOfLinks)
    for line in file:
        url = urllib.request.urlopen(line).read()
        filename = line.replace('\n', '').split('//')
        filename = filename[1].replace('/', '_')
        html_file = open(os.path.join(directory, (filename + '.html')), 'wb')
        html_file.write(url)
    file.close()
    html_file.close()


# downlaod one link and save it into a local folder
def downlaod_link(link,directory):
    url = urllib.request.urlopen(link).read()
    os.makedirs(directory, exist_ok=True)
    filename = link.replace('\n', '').replace('.','_').split('//')
    filename = filename[1].replace('/', '_')
    html_file = open(os.path.join(directory, (filename + '.html')), 'wb')
    html_file.write(url)


