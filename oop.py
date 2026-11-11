# class Category:
#     def __init__(self, name):
#         self.name = name

# food = Category('Food')
# clothing = Category('Clothing')

# print(food.name)
# print(clothing.name)


class category:
    def __init__(self,name = 'General'):

        self.name = name,
        self.ledger = []
        

    def deposit(self, amount, description = ''):
        self.ledger.append(
            {'amount': amount,'description': description},
        )
        print(f"I have deposited {amount} to {self.name} category")
       

food = category('Food')
other = category()
print(other.name)   
print(food.name)

other.deposit(2000, 'Initial deposit')
other.deposit(3000, 'Extra money')

food.deposit(1000, 'initial deposit')
food.deposit(5000, 'Extra money')


