
class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def get_balance(self):
        balance = 0

        for transaction in self.ledger:
            balance += transaction["amount"]

        return balance

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True

        return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True

        return False

    def __str__(self):
        title = self.name.center(30, "*")

        output = title + "\n"

        for transaction in self.ledger:
            description = transaction["description"][:23]
            amount = f'{transaction["amount"]:.2f}'

            output += f"{description:<23}{amount:>7}\n"

        output += f"Total: {self.get_balance():.2f}"

        return output


def create_spend_chart(categories):

    # Calculate total withdrawals for each category
    total_spent = 0
    category_spending = []

    for category in categories:
        spent = 0

        for transaction in category.ledger:
            if transaction["amount"] < 0:
                spent += abs(transaction["amount"])

        category_spending.append(spent)
        total_spent += spent

    # Calculate percentages rounded down to nearest 10
    percentages = []

    for spent in category_spending:
        if total_spent == 0:
            percentage = 0
        else:
            percentage = int((spent / total_spent) * 100)

        percentage = (percentage // 10) * 10
        percentages.append(percentage)

    # Start the chart
    chart = "Percentage spent by category\n"

    # Create the vertical bars
    for level in range(100, -1, -10):
        chart += f"{level:>3}|"

        for percentage in percentages:
            if percentage >= level:
                chart += " o "
            else:
                chart += "   "

        chart += " \n"

    # Create the horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Find the longest category name
    max_length = max(len(category.name) for category in categories)

    # Display category names vertically
    for i in range(max_length):
        chart += "     "

        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "

        chart += "\n"

    # Remove the final newline
    return chart.rstrip("\n")
