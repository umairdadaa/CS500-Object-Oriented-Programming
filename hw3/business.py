from base_catalog import Catalog
from typing import List
from catalog import CatalogRepository
from catalog_items import Book, Movie, Periodical, CoverType, FormatType, PeriodicalType, Article

class Library:
    def __init__(self, filename: str):
        self.items = []
        self.repository = CatalogRepository(filename)
        self.load_items()

    def load_items(self):
        self.items = self.repository.get_items()

    def add_item(self, item: Catalog):
        self.items.append(item)
        self.repository.save_items(self.items)

    def remove_item(self, catalog_num: int):
        self.items = [
            item for item in self.items
            if not (hasattr(item, 'catalog_num') and item.catalog_num == catalog_num)
        ]
        self.repository.save_items(self.items)

    def update_item(self, item):
        for index, current_item in enumerate(self.items):
            if hasattr(current_item, 'catalog_num') and current_item.catalog_num == item.catalog_num:
                self.items[index] = item
                break
        self.repository.save_items(self.items)


    def search_by_catalog_num(self, catalog_num: int) -> Catalog:
        for item in self.items:
            if item.catalog_num == catalog_num:
                return item
        return None

    def search_by_title(self, title: str) -> List[Catalog]:
        return [item for item in self.items if title.lower() in item.title.lower()]

    def search_by_subject(self, subject: str) -> List[Catalog]:
        return [item for item in self.items if hasattr(item, 'subject') and subject.lower() in item.subject.lower()]

    def search_by_article_title(self, title: str) -> List[Article]:
        articles = []
        for item in self.items:
            if isinstance(item, Article) and title.lower() in item.title.lower():
                articles.append(item)
        return articles

    def get_books_by_cover_type(self, cover_type: str) -> List[Book]:
        return [item for item in self.items if isinstance(item, Book) and item.cover_type.value.lower() == cover_type.lower()]

    def get_movies_by_movie_format(self, format_type: str) -> List[Movie]:
        return [item for item in self.items if isinstance(item, Movie) and item.format_type.value.lower() == format_type.lower()]
    
    def search_by_article_title(self, title: str) -> List[Article]:
        return [item for item in self.items if isinstance(item, Article) and title.lower() in item.title.lower()]

    def __str__(self):
        return "\n".join(str(item) for item in self.items)
