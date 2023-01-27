import requests
from bs4 import BeautifulSoup

class PSUBS4Scraping():

    def __init__(self):
        self.sitemap_url = "https://bulletins.psu.edu/sitemap.xml"              #this is the overall bulletin sitemap
        self.site_list = []

        self.main_class_list = []                                               #these are bulletin pages with respective classes listed
        self.dickinson_law_class_list = []                                      
        self.graduate_class_list = [] 
        self.undergraduate_class_list = []
        self.medicine_class_list = []
        self.penn_state_law_class_list = []

        self.main_list = []                                                     #these are bulletin pages with program requirements
        self.dickinson_law_list = []                                            
        self.graduate_list = [] 
        self.undergraduate_list = []
        self.medicine_list = []
        self.penn_state_law_list = []

    #this method parses the sitemap and segements class lists by grad, undergrad, etc. 
    def parse_site_map(self):                                                   #this parses by department, if we need to parse by campus later this is also a good place
        page = requests.get(self.sitemap_url)
        site_map = BeautifulSoup(page.content, 'xml')                           #we assume xml site because the PSU bulletin sitemap is xml and default for this method
        department_URL_Result_Set = site_map.find_all('loc')
        department_URL = [url.string for url in department_URL_Result_Set]      #BS ResultSet doesn't allow for as easy parsing, cast to string
        for url in department_URL:
            url = url.strip("<loc>")
            url.strip("</loc>")
            if "/undergraduate" in url:
                if "description" in url:                                        #the "description" string is in url's with class descriptions
                    self.undergraduate_class_list.append(url)
                    self.main_class_list.append(url)
                else:                                                           #else append to general list (this will be program info instead of class info)
                    self.undergraduate_list.append(url)
            if "/graduate" in url:
                if "description" in url:                                        
                    self.graduate_class_list.append(url)
                    self.main_class_list.append(url)
                else:                                                           
                    self.graduate_list.append(url)
            if "/graduate" in url:
                if "description" in url:                                        
                    self.graduate_class_list.append(url)
                    self.main_class_list.append(url)
                else:                                                           
                    self.graduate_list.append(url)
            if "/medicine" in url:
                if "description" in url:                                        
                    self.medicine_class_list.append(url)
                    self.main_class_list.append(url)
                else:                                                           
                    self.medicine_list.append(url)
            if "/dickinsonlaw" in url:
                if "description" in url:                                        
                    self.dickinson_law_class_list.append(url)
                    self.main_class_list.append(url)
                else:                                                           
                    self.dickinson_law_list.append(url)
            if "/pennstatelaw" in url:
                if "description" in url:                                        
                    self.penn_state_law_class_list.append(url)
                    self.main_class_list.append(url)
                else:                                                           
                    self.penn_state_law_list.append(url)
        return department_URL                                                   #returns list of strings that are exact URL's

    def scrape_department_classes(self, department="all"):
        deparment = deparment.lower()               
        if department == "all":
            department = self.main_class_list
        elif department == "undergaduate":
            department = self.undergraduate_class_list
        elif department == "graduate":
            deparment = self.graduate_class_list
        elif department == "medicine":
            department = self.medicine_class_list
        elif department == "dickinsonlaw":
            deparment = self.dickinson_law_class_list
        elif deparment == "pennstatelaw":
            deparment = self.penn_state_law_class_list

    def test_print_all_urls(self):                                              #dev tool
        self.site_list = self.parse_site(None)
        for url in self.site_list:
            print(url)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ MASTER LIST ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("PRINTING UNDERGRADUATE CLASS LIST.................................................")
        for url in self.undergraduate_class_list:
            print(url)
        print("PRINTING UNDERGRADUATE LIST.......................................................")
        for url in self.undergraduate_list:
            print(url)
        print("PRINTING GRADUATE CLASS LIST......................................................")
        for url in self.graduate_class_list:
            print(url)
        print("PRINTING GRADUATE LIST............................................................")
        for url in self.graduate_list:
            print(url)
        
    def test_print_last_ug_desc(self):
        if len(self.undergraduate_class_list) > 0:
            print(self.undergraduate_class_list[-1])
        else:
            print("list is empty") 