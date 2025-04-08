from datetime import datetime
from collections import defaultdict

class ExpenseTracker:
    def __init__(self):
        self.expenses = defaultdict(list)

    def add_expense(self, category, amount, note=""):
        date = datetime.now().strftime("%Y-%m-%d")
        entry = {"amount": amount, "note": note, "date": date}
        self.expenses[category].append(entry)
        return f"[+] Added to '{category}': {entry}"

    def show_expenses(self, category):
        return self.expenses.get(category, [])

    def update_expense(self, category, index, new_amount=None, new_note=None):
        if category not in self.expenses or index >= len(self.expenses[category]):
            return "Expense not found."
        if new_amount is not None:
            self.expenses[category][index]["amount"] = new_amount
        if new_note is not None:
            self.expenses[category][index]["note"] = new_note
        return f"[~] Updated expense at index {index} in '{category}'."

    def remove_expense(self, category, index):
        if category not in self.expenses or index >= len(self.expenses[category]):
            return "Expense not found."
        removed = self.expenses[category].pop(index)
        return f"[-] Removed from '{category}': {removed}"

    def get_expense_by_id(self, category, index):
        if category in self.expenses and index < len(self.expenses[category]):
            return self.expenses[category][index]
        return "Expense not found."

    def get_expenses_by_category(self, category):
        return self.expenses.get(category, [])

    def total(self, category):
        return sum(entry["amount"] for entry in self.expenses.get(category, []))

    def list_categories(self):
        return list(self.expenses.keys())

    def get_today(self):
        return datetime.now().strftime("%Y-%m-%d")

    def group_by_month(self, category):
        grouped = defaultdict(list)
        for entry in self.expenses.get(category, []):
            month = entry["date"][:7]
            grouped[month].append(entry)
        return dict(grouped)
