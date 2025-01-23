from enum import Enum
from base_catalog import Catalog

# Enum for Cover Type
class CoverType(Enum):
    HARDCOVER = "Hardcover"
    PAPERBACK = "Paperback"
    CLOTHCOVER = "Clothcover"

# Enum for Format Type
class FormatType(Enum):
    DVD = "DVD"
    BLU_RAY = "Blu-ray"
    VCD = "VCD"

# Enum for Periodical Type
class PeriodicalType(Enum):
    JOURNAL = "Journal"
    MAGAZINE = "Magazine"
    NEWSPAPER = "Newspaper"

class Book(Catalog):
    def __init__(self, catalog_num: int, title: str, published_date: str, cover_type: str, subject: str, author: str):
        Catalog.__init__(self, catalog_num, title, published_date)
        self.cover_type = CoverType[cover_type.upper()]  # Convert string to CoverType enum
        self.subject = subject
        self.author = author

    def __str__(self):
        return f"Book: {Catalog.__str__(self)} - {self.cover_type.value} - {self.subject} - {self.author}"


class Movie(Catalog):
    def __init__(self, catalog_num: int, title: str, published_date: str, subject: str, format_type: str, director: str, actors: str, year: int, length: int):
        Catalog.__init__(self, catalog_num, title, published_date)
        self.subject = subject
        self.format_type = FormatType[format_type.upper().replace("-", "_")]  # Convert string to FormatType enum
        self.director = director
        self.actors = actors
        self.year = year
        self.length = length

    def __str__(self):
        return f"Movie: {Catalog.__str__(self)} - {self.subject} - {self.format_type.value} - Directed by {self.director} - Starring {self.actors} - {self.year} - {self.length} min"


class Periodical(Catalog):
    def __init__(self, catalog_num: int, title: str, published_date: str, periodical_type: str):
        Catalog.__init__(self, catalog_num, title, published_date)
        self.periodical_type = PeriodicalType[periodical_type.upper()]  # Convert string to PeriodicalType enum
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)

    def __str__(self):
        return f"Periodical: {Catalog.__str__(self)} - {self.periodical_type.value} - Articles: {len(self.articles)}"

class Article:
    def __init__(self, title: str, author: str, issue_date: str, periodical_title: str):
        self.title = title
        self.author = author
        self.issue_date = issue_date
        self.periodical_title = periodical_title

    def __str__(self):
        return f"Article: {self.title} by {self.author}, Published on {self.issue_date} in {self.periodical_title}"

