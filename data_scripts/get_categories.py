from bs4 import BeautifulSoup
from csv import writer as csv_writer
import requests


def get_categories_for_search(soup):
    fields = soup.find(id='facetapi-facet-apachesolrsolr-block-im-field-terms-cochrane-library')

    links = fields.find_all('a')

    categories = []
    for link in links:
        category_name = link.contents[0]
        category_number_of_items = link.span.string
        category = '{} {}'.format(category_name, category_number_of_items)
        categories.append(category)
    return categories


def main():
    req = requests.get('http://summaries.cochrane.org/search/site/chocolate')

    soup = BeautifulSoup(req.text)

    categories = get_categories_for_search(soup)

    filename = 'categories.csv'
    with open(filename, 'w') as csv_file:
        for category in categories:
            spamwriter = csv_writer(csv_file)
            spamwriter.writerow([category])

main()
