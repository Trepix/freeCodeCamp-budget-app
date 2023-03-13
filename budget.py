class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total_amount = 0
        pass

    def deposit(self, amount, description="") -> None:
        self.ledger.append({"amount": amount, "description": description})
        self.total_amount += amount

    def withdraw(self, amount, description="") -> bool:
        if self.total_amount - amount < 0:
            return False
        
        self.ledger.append({"amount": -amount, "description": description})
        return True


def create_spend_chart(categories):
    pass
