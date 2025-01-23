from business import Library
from catalog_items import Book, Movie, Periodical, Article, CoverType, FormatType

class LibraryApp:
    def __init__(self, library: Library):
        self.library = library

    def show_menu(self):
        print("\n" + "=" * 30)
        print("📚 Library Menu")
        print("=" * 30)
        print("1. Add Book")
        print("2. Add Movie")
        print("3. Add Periodical")
        print("4. Add Article")
        print("5. Remove Item by Catalog Number")
        print("6. Update Item by Catalog Number")
        print("7. Search by Catalog Number")
        print("8. Search by Title")
        print("9. Search by Subject")
        print("10. Search by Article Title")
        print("11. Get Books by Cover Type")
        print("12. Get Movies by Movie Format")
        print("13. List All Items")
        print("14. Exit")
        print("=" * 30 + "\n")

    def process_command(self):
        while True:
            self.show_menu()
            command = input("Enter your choice: ").strip()
            print("\n" + "-" * 30)
            if command == "1":
                self.add_book()
            elif command == "2":
                self.add_movie()
            elif command == "3":
                self.add_periodical()
            elif command == "4":
                self.add_article()
            elif command == "5":
                self.remove_item()
            elif command == "6":
                self.update_item()
            elif command == "7":
                self.search_by_catalog_num()
            elif command == "8":
                self.search_by_title()
            elif command == "9":
                self.search_by_subject()
            elif command == "10":
                self.search_by_article_title()
            elif command == "11":
                self.get_books_by_cover_type()
            elif command == "12":
                self.get_movies_by_movie_format()
            elif command == "13":
                self.list_all_items()
            elif command == "14":
                print("Goodbye! 👋")
                break
            else:
                print("❌ Invalid command. Please try again.")
            print("-" * 30 + "\n")

    # Methods to add items
    def add_book(self):
        print("📘 Add Book")
        catalog_num = int(input("Enter catalog number: "))
        title = input("Enter title: ")
        published_date = input("Enter published date: ")
        cover_type = input("Enter cover type: ")
        subject = input("Enter subject: ")
        author = input("Enter author: ")
        book = Book(catalog_num, title, published_date, cover_type, subject, author)
        self.library.add_item(book)
        print("✅ Book added successfully.")

    def add_movie(self):
        print("🎬 Add Movie")
        catalog_num = int(input("Enter catalog number: "))
        title = input("Enter title: ")
        published_date = input("Enter published date: ")
        subject = input("Enter subject: ")
        format_type = input("Enter format type: ")
        director = input("Enter director: ")
        actors = input("Enter actors: ")
        year = int(input("Enter year: "))
        length = int(input("Enter length in minutes: "))
        movie = Movie(catalog_num, title, published_date, subject, format_type, director, actors, year, length)
        self.library.add_item(movie)
        print("✅ Movie added successfully.")

    def add_periodical(self):
        print("📰 Add Periodical")
        catalog_num = int(input("Enter catalog number: "))
        title = input("Enter title: ")
        published_date = input("Enter published date: ")
        periodical_type = input("Enter periodical type: ")
        periodical = Periodical(catalog_num, title, published_date, periodical_type)
        self.library.add_item(periodical)
        print("✅ Periodical added successfully.")

    def add_article(self):
        print("📝 Add Article")
        title = input("Enter article title: ")
        author = input("Enter author: ")
        issue_date = input("Enter issue date: ")
        periodical_title = input("Enter periodical title: ")
        article = Article(title, author, issue_date, periodical_title)
        self.library.add_item(article)
        print("✅ Article added successfully.")

    # Method to remove item
    def remove_item(self):
        print("❌ Remove Item")
        catalog_num = int(input("Enter catalog number of the item to remove: "))
        self.library.remove_item(catalog_num)
        print("✅ Item removed successfully.")

    # Method to update item
    def update_item(self):
        print("🔄 Update Item")
        catalog_num = int(input("Enter catalog number of the item to update: "))
        item_type = input("Enter the type of item (Book, Movie, Periodical, Article): ").strip().lower()

        if item_type == "book":
            title = input("Enter new title: ")
            published_date = input("Enter new published date: ")
            print("Available cover types: ", [cover_type.value for cover_type in CoverType])
            cover_type = input("Enter new cover type: ")
            subject = input("Enter new subject: ")
            author = input("Enter new author: ")
            updated_book = Book(catalog_num, title, published_date, cover_type, subject, author)
            self.library.update_item(updated_book)
            print("✅ Book updated successfully.")
        elif item_type == "movie":
            title = input("Enter new title: ")
            published_date = input("Enter new published date: ")
            subject = input("Enter new subject: ")
            print("Available format types: ", [format_type.value for format_type in FormatType])
            format_type = input("Enter new format type: ")
            director = input("Enter new director: ")
            actors = input("Enter new actors: ")
            year = int(input("Enter new year: "))
            length = int(input("Enter new length in minutes: "))
            updated_movie = Movie(catalog_num, title, published_date, subject, format_type, director, actors, year, length)
            self.library.update_item(updated_movie)
            print("✅ Movie updated successfully.")
        elif item_type == "periodical":
            title = input("Enter new title: ")
            published_date = input("Enter new published date: ")
            periodical_type = input("Enter new periodical type: ")
            updated_periodical = Periodical(catalog_num, title, published_date, periodical_type)
            self.library.update_item(updated_periodical)
            print("✅ Periodical updated successfully.")
        elif item_type == "article":
            title = input("Enter new article title: ")
            author = input("Enter new author: ")
            issue_date = input("Enter new issue date: ")
            periodical_title = input("Enter new periodical title: ")
            updated_article = Article(title, author, issue_date, periodical_title)
            self.library.update_item(updated_article)
            print("✅ Article updated successfully.")
        else:
            print("❌ Invalid item type. Please try again.")

    # Search and display methods...
    def search_by_catalog_num(self):
        print("🔍 Search by Catalog Number")
        catalog_num = int(input("Enter catalog number to search: "))
        item = self.library.search_by_catalog_num(catalog_num)
        if item:
            print(item)
        else:
            print("❌ Item not found.")

    def search_by_title(self):
        print("🔍 Search by Title")
        title = input("Enter title to search: ")
        results = self.library.search_by_title(title)
        if results:
            for item in results:
                print(item)
        else:
            print("❌ No items found.")

    def search_by_subject(self):
        print("🔍 Search by Subject")
        subject = input("Enter subject to search: ")
        results = self.library.search_by_subject(subject)
        if results:
            for item in results:
                print(item)
        else:
            print("❌ No items found.")

    def search_by_article_title(self):
        print("🔍 Search by Article Title")
        title = input("Enter article title to search: ")
        results = self.library.search_by_article_title(title)
        if results:
            for article in results:
                print(article)
        else:
            print("❌ No articles found.")

    def get_books_by_cover_type(self):
        print("📘 Get Books by Cover Type")
        cover_type = input("Enter cover type: ")
        results = self.library.get_books_by_cover_type(cover_type)
        if results:
            for book in results:
                print(book)
        else:
            print("❌ No books found with the specified cover type.")

    def get_movies_by_movie_format(self):
        print("🎬 Get Movies by Movie Format")
        format_type = input("Enter movie format: ")
        results = self.library.get_movies_by_movie_format(format_type)
        if results:
            for movie in results:
                print(movie)
        else:
            print("❌ No movies found with the specified format.")

    def list_all_items(self):
        print("📜 List All Items")
        if not self.library.items:
            print("❌ No items in the library.")
        else:
            for item in self.library.items:
                print(item)

if __name__ == "__main__":
    filename = "catalog.csv"  # Path to your CSV file
    library = Library(filename)
    app = LibraryApp(library)
    app.process_command()
