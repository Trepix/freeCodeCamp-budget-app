from itertools import zip_longest
from math import ceil


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

    def expenses(self):
        return filter(lambda entry: entry["amount"] < 0, self.ledger)

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


def _part_over_10(part, total):
    return int(ceil(part * 10 / total))


def _format_bar_graph(values):
    y_label_width = (4 - len("|"))
    y_labels = list(map(lambda n: f'{" " * (y_label_width - len(str(n)))}{n}|', range(0, 101, 10)))
    graph = [y_labels] + [[" o "] * _part_over_10(value, sum(values)) for value in values]

    result = []
    for bar_line in zip_longest(*graph, fillvalue='   '):
        result.append(f'{"".join(bar_line)} ')
    return "\n".join(reversed(result))


def _format_x_axis_labels(names):
    result = []
    for name in zip_longest(*names, fillvalue=' '):
        label_line = "".join(map(lambda c: f" {c} ", name))
        result.append(f"    {label_line} ")

    return "\n".join(result)


def create_spend_chart(categories):
    expenses = [sum(map(lambda entry: entry["amount"], category.expenses())) for category in categories]
    bars = _format_bar_graph(expenses)

    x_axis_line = "    " + "-" * (3 * len(categories) + 1)

    names = list(map(lambda c: c.name, categories))
    labels = _format_x_axis_labels(names)

    return f"""Percentage spent by category
{bars}
{x_axis_line}
{labels}"""
