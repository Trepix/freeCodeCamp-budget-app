class Category:

    _extract_width_length = 30

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
        header = self._format_header()
        lines = "\n".join(map(Category._format_ledger_line, self.ledger))
        total = f'Total: {self._total_amount:.02f}'

        return "\n".join([header, lines, total])

    def _format_header(self):
        lateral_filling_length = int((Category._extract_width_length - len(self.name)) / 2)
        filling = "*" * lateral_filling_length
        return f'{filling}{self.name}{filling}'

    @staticmethod
    def _format_ledger_line(first_ledger_line):
        maximum_description_length = 23
        amount = f'{first_ledger_line["amount"]:.2f}'
        description = first_ledger_line["description"][:maximum_description_length]
        spaces = " " * (Category._extract_width_length - len(description) - len(amount))
        return description + spaces + amount




def create_spend_chart(categories):
    pass
