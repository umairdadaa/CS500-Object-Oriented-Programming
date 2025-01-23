from abc import ABC, abstractmethod
import sqlite3

class Database:
    def __init__(self, dbname: str) -> None:
        self.__dbname = dbname
        self.__conn = sqlite3.connect(dbname)

    def run(self, query: str, params: list = []) -> list:
        """
        Executes a given SQL query with optional parameters and returns the result.
        """
        cursor = self.__conn.cursor()
        cursor.execute(query, params)
        self.__conn.commit()
        return cursor.fetchall()

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        """
        Abstract method to execute a command.
        """
        pass

class CreateCommand(Command):
    def __init__(self, db: Database, table_name: str, columns: dict) -> None:
        self.__db = db
        self.__table_name = table_name
        self.__columns = columns

    def execute(self) -> None:
        """
        Executes the command to create a table with specified columns and data types.
        """
        column_definitions = ", ".join([f"{column} {datatype}" for column, datatype in self.__columns.items()])
        query = f"CREATE TABLE IF NOT EXISTS {self.__table_name} ({column_definitions})"
        self.__db.run(query)
        print(f"Table '{self.__table_name}' created successfully.")

class SelectCommand(Command):
    def __init__(self, db: Database, table_name: str, columns: list = None) -> None:
        self.__db = db
        self.__table_name = table_name
        self.__columns = columns or ["*"]

    def execute(self) -> list:
        """
        Executes the command to select data from a table.
        """
        columns = ", ".join(self.__columns)
        query = f"SELECT {columns} FROM {self.__table_name}"
        results = self.__db.run(query)
        return results

class UpdateCommand(Command):
    def __init__(self, db: Database, table_name: str, updates: dict, condition: str) -> None:
        self.__db = db
        self.__table_name = table_name
        self.__updates = updates
        self.__condition = condition

    def execute(self) -> None:
        """
        Executes the command to update rows in a table.
        """
        updates = ", ".join([f"{column} = ?" for column in self.__updates.keys()])
        query = f"UPDATE {self.__table_name} SET {updates} WHERE {self.__condition}"
        self.__db.run(query, list(self.__updates.values()))
        print(f"Table '{self.__table_name}' updated successfully.")

class DeleteCommand(Command):
    def __init__(self, db: Database, table_name: str, condition: str) -> None:
        self.__db = db
        self.__table_name = table_name
        self.__condition = condition

    def execute(self) -> None:
        """
        Executes the command to delete rows from a table.
        """
        query = f"DELETE FROM {self.__table_name} WHERE {self.__condition}"
        self.__db.run(query)
        print(f"Records from table '{self.__table_name}' deleted successfully.")

def main():
    db = Database('testDB.db')
    # Create table
    create_table = CreateCommand(db, "users", {"id": "INTEGER PRIMARY KEY", "name": "TEXT", "age": "INTEGER"})
    create_table.execute()

    # Example of SelectCommand
    select_data = SelectCommand(db, "users")
    results = select_data.execute()
    print("Data:", results)

if __name__ == '__main__':
    main()
