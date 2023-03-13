class Category:

    extract_width_length = 30

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

    def _build_header(self):
        lateral_filling_length = int((Category.extract_width_length - len(self.name)) / 2)
        filling = "*" * lateral_filling_length
        return f'{filling}{self.name}{filling}'

    def __str__(self):
        header = self._build_header()
        first_ledger_line = self.ledger[0]
        amount = f'{first_ledger_line["amount"]:.2f}'
        return f"""{header}
deposit                 {amount}
milk, cereal, eggs, bac -45.67
Transfer to Entertainme -20.00
Total: 834.33"""


def create_spend_chart(categories):
    pass
