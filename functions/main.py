numbers = [1,1,1,1,1]

def average(numbers):

    """Return the avarage of list of numbers"""
    return sum(numbers)//len(numbers)

print(average(numbers));


def greeting(name , greet = 'Hello'):

    print(f"{greet} {name}!")
    
greeting('Eric')
