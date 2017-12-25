import requests
import bs4
from bs4 import BeautifulSoup

import pandas as pd
import time


URL = "https://www.jobhired.io/cat/engineering"
page = requests.get(URL)
soup = BeautifulSoup(page.text, “html.parser”)

print(soup.prettify())

def extract_job_title_from_result(soup): 
  jobs = []
  return(jobs)

extract_job_title_from_result(soup)
