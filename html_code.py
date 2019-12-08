import urllib.request
import sys
import os


def html_code(directory):
    crawled = os.path.join(directory, 'crawled.txt')
    file = open(crawled)
    for line in file:
        url = urllib.request.urlopen(line).read()
        filename = line.replace('\n', '').split('//')
        filename = filename[1].replace('/','_')
        html_file = open(os.path.join(directory,(filename+'.html')),'wb')
        html_file.write(url)
    file.close()
    html_file.close()
