from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "https://www.jobhired.io/cat/engineering"

cityName = "San Francisco"

soup = bs4.BeautifulSoup(BASE_URL, 'html.parser')
results = soup.body.find_all(string=re.compile('.*{0}.*'.format(searched_word)), recursive=True)
