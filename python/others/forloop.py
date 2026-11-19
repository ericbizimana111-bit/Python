ledger = [
    {'amount': 2000, 'description': 'Initial deposit'},
    {'amount': 3000, 'description': 'Extra money'},
    {'amount': 1000, 'description': 'added money'}
]

balance = 0

for transaction in ledger:
    
    balance += transaction['amount']
    print(transaction['amount'], transaction['description'])

print(f"Current balance: {balance}")
