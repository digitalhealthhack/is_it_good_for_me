from requests import get as get_page
from bs4 import BeautifulSoup
import csv
import codecs
import cStringIO


TOPIC = 'chocolate'


def _get_study_url(url):
    # Receives the url of a cochrane search result and returns the url for the
    # study
    result_page = get_page(url)
    result_soup = BeautifulSoup(result_page.text)
    study_url = result_soup \
        .find(id='node_review_full_group_research') \
        .find_all('a')[0] \
        .get('href')
    return study_url


def _get_info_for_study(study_url):
    study_page = get_page(study_url)
    soup = BeautifulSoup(study_page.text)

    study_title = soup.find(class_='articleTitle').span.text

    abstract_html = soup.find(id='mrwFulltext').div.find_all(['p', 'div'])

    abstract_text = u''
    authors_conclusions = u''
    is_capturing = False
    for html in abstract_html:
        if is_capturing and html.name != 'p' and html.text != 'Authors\' conclusions':
            is_capturing = False
            break

        abstract_text += unicode(html.text)

        if is_capturing:
            authors_conclusions += unicode(html.text)

        if html.name != 'p' and html.text == 'Authors\' conclusions':
            is_capturing = True

    return (study_title, authors_conclusions, abstract_text)


def main(search_query=''):
    req = get_page(
        'http://summaries.cochrane.org/search/site/{}'.format(search_query),
    )

    soup = BeautifulSoup(req.text)

    results = soup.find_all(class_='search-result')

    studies = []
    for result in results:
        result_url = result.a.get('href')
        if result_url:
            study_url = _get_study_url(result_url)
            study_title, study_conclusion, study_abstract = \
                _get_info_for_study(study_url)
            studies.append([study_title, study_conclusion, study_abstract])

    filename = 'studies.csv'
    with open(filename, 'w') as csv_file:
        for study in studies:
            spamwriter = UnicodeWriter(csv_file)
            spamwriter.writerow(study)


class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """
    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)



main(TOPIC)
