from itertools import zip_longest


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
        description = first_ledger_line["description"][:maximum_description_length]
        amount = f'{first_ledger_line["amount"]:.2f}'.rjust(Category._extract_width_length - len(description))
        return description + amount


def format_x_axis_labels(names):
    result = []
    for name in zip_longest(*names, fillvalue=' '):
        label_line = "".join(map(lambda c: f" {c} ", name))
        result.append(f"    {label_line} ")

    return "\n".join(result)


def create_spend_chart(categories):
    names = list(map(lambda c: c.name, categories))
    x_axis_line = "    " + "-" * (3 * len(categories) + 1)
    return f"""Percentage spent by category
100|          
 90|          
 80|          
 70|    o     
 60|    o     
 50|    o     
 40|    o     
 30|    o     
 20|    o  o  
 10|    o  o  
  0| o  o  o  
{x_axis_line}
{format_x_axis_labels(names)}"""
