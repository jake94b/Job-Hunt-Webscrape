from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "https://www.jobhired.io/cat/engineering"

def get_cityname(section_url):
	html = urlopen(section_url).read()
	soup = BeatifulSoup(html, "lxml")
	cityname = soup.find("div", "container")
	
