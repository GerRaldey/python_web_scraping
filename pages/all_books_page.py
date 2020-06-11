import re

from bs4 import BeautifulSoup
from locators.all_books_pages import AllBooksPageLocator
from parser.book_parser import BookParser

class AllBooksPage:
    def __init__(self, book_page):
        self.soup = BeautifulSoup(book_page, 'html.parser')

    @property
    def books(self):
        locator = AllBooksPageLocator.Books
        return [BookParser(e) for e in self.soup.select(locator)]

    @property
    def page_num(self):
        content = self.soup.select_one(AllBooksPageLocator.PAGER).string
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        return int(matcher.group(1))
