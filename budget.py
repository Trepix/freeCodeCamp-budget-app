class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        pass

    def deposit(self, amount, description="") -> None:
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description="") -> bool:
        self.ledger.append({"amount": -amount, "description": description})
        return True


def create_spend_chart(categories):
    pass
