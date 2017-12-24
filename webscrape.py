from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

BASE_URL = "https://www.jobhired.io/cat/engineering"

cityName = "San Francisco"

soup = bs4.BeautifulSoup(BASE_URL, 'html.parser')
results = soup.body.find_all(string=re.compile('.*{0}.*'.format(searched_word)), recursive=True)

print 'Found the word "{0}" {1} times\n'.format(cityName, len(results))

for content in results:
	words = content.split()
		for index, word in enumerate(words)
		# If the content contains the search word twice or more this will fire 			for each occurence
                	if word == cityName:
                		
                		# Check if it's a first word
                	if index != 0:

                		# Check if it's a last word
            		
            print '\tWord before: "{0}", word after: "{1}"'.format(before, after)
