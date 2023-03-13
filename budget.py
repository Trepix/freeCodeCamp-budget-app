class Category:

    x = 0

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self._total_amount = 0
        pass

    def deposit(self, amount, description="") -> None:
        self.ledger.append({"amount": amount, "description": description})
        self._total_amount += amount

    def withdraw(self, amount, description="") -> bool:
        if not self.check_funds(amount):
            return False

        self._total_amount -= amount
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self):
        return self._total_amount

    def transfer(self, amount, category) -> bool:
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')
        return True

    def check_funds(self, amount):
        return self._total_amount - amount >= 0

    def __str__(self):
        return """*************Food*************
deposit                 900.00
milk, cereal, eggs, bac -45.67
Transfer to Entertainme -20.00
Total: 834.33"""


def create_spend_chart(categories):
    pass
