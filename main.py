import threading
#from queue import Queue
from spider import Spider
from domain import *
from general import *
from html_code import *

#PROJECT_NAME = input('Please enter a Project Name: ')
#HOMEPAGE = input('Please enter the web site URL: ')
PROJECT_NAME = 'oslomet'
HOMEPAGE = 'https://www.oslomet.no/'
RESUME_DOWNLOAD = False



DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = os.path.join(PROJECT_NAME , 'queue.txt')
CRAWLED_FILE = os.path.join(PROJECT_NAME , 'crawled.txt')
FLD_DOWNLOADED= os.path.join(PROJECT_NAME , 'WEBSITE_DOWNLOAD')
NUMBER_OF_THREADS = 1
#queue = Queue()
webcrawler = Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME, FLD_DOWNLOADED , RESUME_DOWNLOAD)



while  webcrawler.crawl_next_page_from_queue():
    print('still to go: ', str(webcrawler.get_queue_stats()))
