import requests
import logging
from pages.all_books_page import AllBooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%m:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('scraping')
logger.info('Loading book lists...')

page_content = requests.get('http://books.toscrape.com').content
page = AllBooksPage(page_content)
books = page.books

logger.info('Adding page 2 to 50 books in the list')
for page in range(1, page.page_num):
    url = f'http://books.toscrape.com/catalogue/page-{page+1}.html'
    page_content = requests.get(url).content
    new_page = AllBooksPage(page_content)
    books.extend(new_page.books)

