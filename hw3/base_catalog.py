class Catalog:
    def __init__(self, catalog_num: int, title: str, published_date: str):
        self.catalog_num = catalog_num
        self.title = title
        self.published_date = published_date

    def __eq__(self, other):
        if not isinstance(other, Catalog):
            return False
        return self.catalog_num == other.catalog_num

    def __str__(self):
        return f"{self.catalog_num} - {self.title} ({self.published_date})"
