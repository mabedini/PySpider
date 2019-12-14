import urllib.request
import sys
import os
from domain import *


# download all urls, from a text, crawled by the  spider  crawler and save it into a local folder
def downlaod_mass(fileOfLinks, directory):
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
def downlaod_link(link, directory, downloaded_pages):
    url = urllib.request.urlopen(link).read()
    # check if the latest version already downloaded and different
    if link in downloaded_pages :
        dlfile = downloaded_pages[link]

        if os.path.exists(dlfile) :
            html_file = open(dlfile, 'rb')
            dl_page = html_file.read()
            # if content has been changed compare to already downloaded page
            if dl_page == url :
                return None

    # otherwise, if non downkloaded or old content, save the new page
    os.makedirs(directory, exist_ok=True)
    filename = link.replace('\n', '').replace('.','_').split('//')
    filename = filename[1].replace('/', '_')
    filename = os.path.join(directory, (filename + '.html'))
    html_file = open(filename, 'wb')
    html_file.write(url)


    return filename


