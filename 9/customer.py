class Customer:
    def __init__(self, first_name: str, last_name: str, account_number: str, balance: float) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        self.balance = balance

    def __str__(self) -> str:
        return f"Customer[first name={self.first_name}, last name={self.last_name}, account number={self.account_number}, balance={self.balance}]"

    def tolist(self) -> list[str]:
        return [self.first_name, self.last_name, self.account_number, str(self.balance)]
