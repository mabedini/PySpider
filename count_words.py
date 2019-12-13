import glob
from bs4 import BeautifulSoup
import os
import re


#FLD_DOWNLOADED = input('Please enter the folder of downloaded webbpages: ')

FLD_DOWNLOADED= os.path.join('/Users/maniabedini/Non_Box/Projects/Spider/oslomet/WEBSITE_DOWNLOAD/2019-12-13')
SEARCH_WORD = 'at'


class wordCount:
  def __init__(self, flpath):
    self.filePath = flpath

  def load_html(self):
    html_file = open(self.filePath, 'rb')

    #      domain_name = urlparse(url).netloc
    page = html_file.read()
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