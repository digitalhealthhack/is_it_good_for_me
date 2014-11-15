import requests
from bs4 import BeautifulSoup

req = requests.get('http://summaries.cochrane.org/search/site/chocolate')

soup = BeautifulSoup(req.text)

fields = soup.find(id='facetapi-facet-apachesolrsolr-block-im-field-terms-cochrane-library')

links = fields.find_all('a')

for link in links:
    category_name = link.contents[0]
    category_number_of_items = link.span.string
    print '{} {}'.format(category_name, category_number_of_items)


