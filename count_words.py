import glob
from bs4 import BeautifulSoup
import os
import re
from urllib.request import urlopen


#FLD_DOWNLOADED = input('Please enter the folder of downloaded webbpages: ')

FLD_DOWNLOADED= '/Users/maniabedini/Non_Box/Projects/Spider/oslomet/WEBSITE_DOWNLOAD/2019-12-13'
SEARCH_WORD = 'at'

from html.parser import HTMLParser

class paragraph_finder(HTMLParser):

    def __init__(self):
      super().__init__()
      self.inPar = 0

    def handle_startendtag(self, startendTag, attrs):
      if startendTag == 'p':
        self.inPar += 1

    def handle_starttag(self, tag, attrs):
      if tag == 'p':
        self.inPar -= 1

    # def handle_endtag(self, tag):
    #     print("Encountered an end tag :", tag)

    def handle_data(self, data):
        if (self.inPar) :

          print("Encountered some data  :", data)



class wordCount:
  def __init__(self,flpath):
    self.filePath = flpath

    self.parser = paragraph_finder()

  def load_html(self):
    html_file = open(self.filePath, 'rt')

    #      domain_name = urlparse(self.filePath).netloc
    page = html_file.read()
    #print(page)
    #self.parser.feed(html_file.read())


    soup = BeautifulSoup(page, "html.parser")
    results = [p_tag.text.lower() for p_tag in soup.find_all("p")]

    return results

  def count(self,word):

    count_num = list()
    text_list = self.load_html()
    for text in text_list:
      count_num.append(len(re.findall(word, text )))


    return sum(count_num)


def main() :
  wordOcc = 0
  # look for all saved webpages
  for filePath in glob.glob(os.path.join(FLD_DOWNLOADED,"*.html")):
    print(filePath)
    wc = wordCount(filePath)
    wordOcc+=wc.count( SEARCH_WORD.lower())

  print(wordOcc)


if __name__ == "__main__":
    main()