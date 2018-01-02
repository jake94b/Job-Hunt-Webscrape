import requests
import bs4
from bs4 import BeautifulSoup

import pandas as pd
import time

languages = ['bash', 'java', 'javascript', 'php' ]
db_lang = ['sql', 'mysql', 'mongodb', 'rdbms']
os = ['linux', 'debian', 'ubuntu',  'mac os x', 'windows']
overall_dict = languages + db_lang + os


base_url = "http://www.indeed.com"    
#change the start_url can scrape different cities.
start_url = "https://www.indeed.com/jobs?q=&l=California"



