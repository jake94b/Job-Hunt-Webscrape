import requests
import bs4
from bs4 import BeautifulSoup

import pandas as pd
import time


URL = "https://www.jobhired.io/cat/engineering"
page = requests.get(URL)
soup = BeautifulSoup(page.text, “html.parser”)

print(soup.prettify())

def extract_job_list_from_result(soup):
  jobs = [] 
  for section in soup.find_all(name=”section”, attrs={“class”:”jobs-list”}):
      for span in div.find_all(name=”span”, attrs={“class”:”title-res”}):
      jobs.append(span[“title-res”])
  return jobs

def extract_company_from_result(soup): 
  companies = []
  for div in soup.find_all(name=”div”, attrs={“class”:”col-md-12”}):
    company = div.find_all(name=”span”, attrs={“class”:”company-res”})
    if len(company) > 0:
      for b in company:
        companies.append(b.text.strip())
    else:
      sec_try = div.find_all(name=”span”, attrs={“class”:”result-link-source”})
        for span in sec_try:
          companies.append(span.text.strip())
 return(companies)


