from urllib.request import urlopen
from link_finder import LinkFinder
from domain import *
from general import *
from html_code import *
import datetime
import pandas as pd
#import cgi
from net_viz import web_graph
import pickle

class Spider:

    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    fld_downloaded =''
    urldownloaded_file = ''
    queue = set()
    crawled = set()
    downloaded_pages = {}
    web_netgraph = None
    resume_download = True

    def __init__(self, project_name, base_url, domain_name, fld_downloaded, resume_dl):
        self.project_name = project_name
        self.base_url = base_url
        self.domain_name = domain_name
        self.fld_downloaded = fld_downloaded
        self.queue_file = project_name + '/queue.txt'
        self.crawled_file = project_name + '/crawled.txt'
        self.urldownloaded_file = project_name + '/downloaded_url_files.pkl'
        self.resume_download = resume_dl
        self.queue.add(base_url)
        self.web_netgraph = web_graph(project_name)
        self.boot()
        #crawl_next_page_from_queue()

    # Creates directory and files for project on first run and starts the spider
    def boot(self):
        create_project_dir(self.project_name)
        create_project_dir(self.fld_downloaded)
        create_data_files(self.project_name, self.base_url)
        # check if we want to resume the downlaod files or craw from first page again
        if (self.resume_download) :
            self.queue = file_to_set(self.queue_file)
            self.crawled = file_to_set(self.crawled_file)
        # load the path to existing  downloaded pages
        if os.path.isfile(self.urldownloaded_file):
          self.downloaded_pages = unpickle_obj(self.urldownloaded_file)

    # Updates user display, fills queue and updates files
    def crawl_page(self,page_url):
        if page_url not in self.crawled:
            self.add_links_to_queue(page_url,self.gather_links(page_url))
            #self.queue.remove(page_url)
            self.crawled.add(page_url)
            self.update_files()
            return True

    def crawl_next_page_from_queue(self):
        if len(self.queue) > 0 :
            url = self.queue.pop()
            return (self.crawl_page(url) )

        else:
            return (False)
    def get_queue_stats(self):
        return  len(self.queue)

    # Converts raw response data into readable information and checks for proper html formatting
    def gather_links(self,page_url):
        html_string = ''
        try:
            print('parsing: '+page_url)
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
                dl_datetime = response.getheader('Date')
                dl_date= pd.to_datetime(dl_datetime)
                dl_folder= os.path.join(self.fld_downloaded,str(dl_date.date()))
                dlpath = downlaod_link(page_url, dl_folder , self.downloaded_pages )
                if dlpath != None :
                    self.downloaded_pages[page_url] = dlpath

            finder = LinkFinder(self.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    # Saves queue data to project files
    def add_links_to_queue(self,page_url,links):
        for url in links:
            self.web_netgraph.add_edge(page_url,url)
            if (url in self.queue) or (url in self.crawled):
                continue
            if self.domain_name != get_domain_name(url):
                continue
            self.queue.add(url)
        self.web_netgraph.draw_graph()


    def update_files(self):
        self.web_netgraph.Network_toFile()
        set_to_file(self.queue, self.queue_file)
        set_to_file(self.crawled, self.crawled_file)
        pickle_obj(self.downloaded_pages,self.urldownloaded_file)
