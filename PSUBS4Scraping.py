import requests
from bs4 import BeautifulSoup

class PSUBS4Scraping():

    def __init__(self, level="undergraduate", department="all"):
        self.sitemap_url = "https://bulletins.psu.edu/sitemap.xml"              #this is the overall bulletin sitemap
        self.level = level                                                      #level refers to undergraduate, graduate, law, etc
        self.department = department                                            #optional to scrape only certain departments
        self.site_list = []

        self.dickinson_law_class_list = []                                      #these are bulletin pages with respective classes listed
        self.graduate_class_list = [] 
        self.undergraduate_class_list = []
        self.medicine_class_list = []
        self.penn_state__law_class_list = []

        self.dickinson_law_list = []                                            #these are bulletin pages with program requirements
        self.graduate_list = [] 
        self.undergraduate_list = []
        self.medicine_list = []
        self.penn_state__law_list = []

    def parse_site(self, site=None):
        if site == None:
            site = self.sitemap_url
        page = requests.get(site)
        site_map = BeautifulSoup(page.content, 'xml')                           #we assume xml site because the PSU bulletin sitemap is xml and default for this method
        department_URL_Result_Set = site_map.find_all('loc')
        department_URL = [url.string for url in department_URL_Result_Set]      #BS ResultSet doesn't allow for as easy parsing
        for url in department_URL:
            url = url.strip("<loc>")
            url.strip("</loc>")
        return department_URL                                                   #returns list of strings that are exact URL's

    def test_print(self):                                                       #dev tool
        self.site_list = self.parse_site(None)
        for url in self.site_list:
            print(url)
        