
# # This is a single-line comment
# x = 25;
# y = 17;
# X = 46;
# #python varibles are case sensitive it means age is different from Age

# print(X)
# print('Hello world!')  # Hello world!

# # function to show multiple values, or arguments, at once by separating them with commas. For example
# print('My favorite colors are','blue','green','red');


# # . A data type describes the kind of value a variable holds, for example, a number or a piece of text. Programming languages use data types so they know how to store and work with different kinds of information.

# my_integer_var = 10
# print("integer:", my_integer_var);

# num = 39;
# print(num)

# number= 10;
# print(type(number));The output of <class 'int'> means that developer is a string type.

# developer = 'kim'
# print(type(developer)); The output of <class 'str'> means that developer is a string type.

# my_int_var = 10
# print(type(my_int_var))

# my_float_var = 21.290
# print(type(my_float_var))

# my_string_var = 'hello'
# print(type(my_string_var))

# my_boolean_var = True
# print(type(my_boolean_var))  # <class 'bool'>

# --- use of isinstance -----------  #

# account_balance = '12'
# account_balance / 2  # this will give the error

# The isinstance() function also allows you to check for multiple types at once.
# account_balance  = 12;
# print(isinstance(account_balance, (int,float,bool,str)));

# type() and isinstance() functions to ensure your variables contain the correct data types before performing operations on them.


# isinstance is used to check the datatype fo the varible


# A string is a sequence of characters surrounded by either single or double quotation marks. Python treats both forms as strings, so you can use either one. Here are some examples:

# my_str_1 = 'Hello'  //  this is  the snake case
# my_str_2 = "World"

# Multiline string  using """"""  helps to write the string and go on the second line  the same to this ''''''
# my_str_1 = """My names
# are Bizimana Eric"""

# my_str_2 = '''My names
# are Bizimana eric'''


# msg = "It's a sunny day"
# quote = 'She said, "Hello World!"'  #this will help you to get Hello, World wrapped in double quotes

# msg = 'It\'s a sunny day'
# quote = "She said, \"Hello!\""
# print(msg);
# print(quote);

'''
#------- To check whether the character or characters exist in the string or not.--------- #
my_str = 'Hello world';

print('Hello' in my_str);
print('world' in my_str);
print('hi' in my_str);
print('e' in my_str);
print('h' in my_str);
print('H' in my_str);
print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False
'''


# Getting the length og the string using the built-in len() function.
# my_str = "Hello World"
# print(len(my_str))
# print(my_str[0])
# print(my_str[2])
# print(my_str[5])
# # use the -1 to get the last character of any string
# # second to last character with -2 and so on

# print(my_str[-1])  # d
# print(my_str[-2])  # l
# print(my_str[-3])  # r

# . A mutable value can be changed after it is created, while an immutable value cannot.

# You can point a variable at a new value, which is called reassignment, but you can't change an immutable value itself by adding, removing, or replacing any of its elements.

# 2. Immutable

# Immutable = cannot be changed after creation.

# For example, a string is immutable:

# name = "Eric"

# name[0] = "B"

# This produces an error because you cannot change an individual character of an existing string.

# Instead, Python creates a new string:

# name = "Eric"

# name = "Bizimana"

# print(name)


# # direct modification of the string is not allowed
# greeting = 'hi';
# greeting[0] = 'H';

# print(greeting);


###############  Common immutable types  :##################

# int
# float
# bool
# str
# tuple
# frozenset
# bytes

# Easy way to remember

# Type     	Mutable?	Example
# list     	✅         Yes[1, 2, 3]
# dict     	✅         Yes	{"name": "Eric"}
# set     	✅         Yes	{1, 2, 3}
# str	      ❌         No	"Eric"
# tuple	    ❌         No(1, 2, 3)
# int	      ❌         No	25
# float     ❌         No	3.14
# bool	    ❌         No	True


################ -----------  String Concatentaion ------------------------- #########################
# : This is the act of combining multiple strings with the plus (+) operator

# my_str_1 = 'Hello';
# my_str_2 = "World";

# str_plus_str = my_str_1 + " " + my_str_2;
# print(str_plus_str);

# Repeating Strings
# You can also repeat a string by multiplying it with an integer using the * operator. The string is repeated the specified number of times:

# sound = "ha";
# repated_str = sound * 5;
# print(repated_str);

# name = 'John Doe'
# age = 26

# # TypeError: can only concatenate str (not "int") to str
# name_and_age = name + age # this give the typo error


# name = 'John Doe'
# age = 26

# # TypeError: can only concatenate str (not "int") to str
# name_and_age = name + " " + str(age)  # this give the typo error

# print(name_and_age)


# the use of the augmented assignement operator represented by +=
# name = 'John Doe'
# age = 26

# name_and_age = name  # Start with the name
# name_and_age += str(age)  # Append the age as string

# print(name_and_age)  # John Doe26


############# ========== String Interpolation ============== ############### :
#  The process of inserting variables and expressions into a string is called String interpolation

# python has the category called f-strings ( short for formatted string literals) which allows you to handle interpolation with an compact and readable sysntax

# F-strings start with f(either lowercase or uppercase) before the quotes 

# name = 'John Doe';
# age = 26;

# name_and_age = (f'My names is {name} and I am {age} years old')
# print(name_and_age);


num1 = 3;
num2 = 10;
num1_and_num2 = (f'{num1} + {num2} is qual to {num1+num2}');
print(num1_and_num2);