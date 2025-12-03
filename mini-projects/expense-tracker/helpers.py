def add_expense(expenses, amount, category):
    expense = {
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    return expenses


def get_total(expenses):
    total = 0
    for exp in expenses:
        total += exp["amount"]
    return total


def get_by_category(expenses, category):
    result = []
    for exp in expenses:
        if exp["category"].lower() == category.lower():
            result.append(exp)
    return result


def delete_expense(expenses, index):
    if 0 <= index < len(expenses):
        del expenses[index]
        return True
    return False


def highest_expense(expenses):
    if not expenses:
        return None
    return max(expenses, key=lambda x: x["amount"])


def lowest_expense(expenses):
    if not expenses:
        return None
    return min(expenses, key=lambda x: x["amount"])
