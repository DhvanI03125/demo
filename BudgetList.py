class BudgetList:
    def __init__(self):
        self.departments = {}

    def add_expense(self, dept, budget, amt, cat, desc):
        self.departments.setdefault(dept, {'budget': budget, 'expenses': []})
        self.departments[dept]['expenses'].append({
            'amount': amt,
            'category': cat,
            'desc': desc
        })
        return self.departments[dept]['expenses']

    def remove_expense(self, dept, index):
        if dept in self.departments and 0 <= index < len(self.departments[dept]['expenses']):
            return self.departments[dept]['expenses'].pop(index)
        return None

    def get_total_expense(self, dept):
        if dept not in self.departments:
            return 0
        return sum(exp['amount'] for exp in self.departments[dept]['expenses'])

    def get_expense_by_category(self, dept, category):
        if dept not in self.departments:
            return []
        return [exp for exp in self.departments[dept]['expenses'] if exp['category'] == category]

    def update_budget(self, dept, new_budget):
        if dept in self.departments:
            self.departments[dept]['budget'] = new_budget
            return True
        return False

    def get_budget_status(self, dept):
        if dept not in self.departments:
            return "Department not found"
        total = self.get_total_expense(dept)
        budget = self.departments[dept]['budget']
        return f"Budget: ₹{budget}, Spent: ₹{total}, Remaining: ₹{budget - total}"

    def list_departments(self):
        return list(self.departments.keys())

    def department_summary(self, dept):
        if dept not in self.departments:
            return {}
        return {
            "budget": self.departments[dept]['budget'],
            "total_expense": self.get_total_expense(dept),
            "expense_count": len(self.departments[dept]['expenses'])
        }

    def clear_expenses(self, dept):
        if dept in self.departments:
            self.departments[dept]['expenses'] = []
            return True
        return False

    def delete_department(self, dept):
        return self.departments.pop(dept, None)
