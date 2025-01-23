import csv
from typing import List
from catalog_items import Book, Movie, Periodical, Article

class CatalogRepository:
    def __init__(self, filename: str):
        self.filename = filename

    def get_items(self) -> List:
        items = []
        with open(self.filename, 'r') as file:
            reader = csv.reader(file, delimiter=',', quotechar='"')
            for row in reader:
                if row[0].strip() == "BOOK":
                    items.append(Book(
                        int(row[1].strip()),  # catalog_num
                        row[2].strip(),       # title
                        row[3].strip(),       # published_date
                        row[4].strip(),       # cover_type
                        row[5].strip(),       # subject
                        row[6].strip()        # author
                    ))
                elif row[0].strip() == "MOVIE":
                    items.append(Movie(
                        int(row[1].strip()),  # catalog_num
                        row[2].strip(),       # title
                        row[3].strip(),       # published_date
                        row[4].strip(),       # subject
                        row[5].strip(),       # format_type
                        row[6].strip(),       # director
                        row[7].strip(),       # actors
                        int(row[8].strip()),  # year
                        int(row[9].strip())   # length
                    ))
                elif row[0].strip() == "PERIODICAL":
                    items.append(Periodical(
                        int(row[1].strip()),  # catalog_num
                        row[2].strip(),       # title
                        row[3].strip(),       # published_date
                        row[4].strip()        # periodical_type
                    ))
                elif row[0].strip() == "ARTICLE":
                    items.append(Article(
                        row[1].strip(),       # title
                        row[2].strip(),       # author
                        row[3].strip(),       # issue_date
                        row[4].strip()        # periodical_title
                    ))
        return items

    def save_items(self, items: List) -> None:
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for item in items:
                if isinstance(item, Book):
                    writer.writerow([
                        "BOOK",
                        item.catalog_num,
                        item.title,
                        item.published_date,
                        item.cover_type.value,
                        item.subject,
                        item.author
                    ])
                elif isinstance(item, Movie):
                    writer.writerow([
                        "MOVIE",
                        item.catalog_num,
                        item.title,
                        item.published_date,
                        item.subject,
                        item.format_type.value,
                        item.director,
                        item.actors,
                        item.year,
                        item.length
                    ])
                elif isinstance(item, Periodical):
                    writer.writerow([
                        "PERIODICAL",
                        item.catalog_num,
                        item.title,
                        item.published_date,
                        item.periodical_type.value
                    ])
                elif isinstance(item, Article):
                    writer.writerow([
                        "ARTICLE",
                        item.title,
                        item.author,
                        item.issue_date,
                        item.periodical_title
                    ])
