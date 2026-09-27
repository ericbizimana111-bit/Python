
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
account_balance  = 12;
print(isinstance(account_balance, (int,float,bool,str))); 

# type() and isinstance() functions to ensure your variables contain the correct data types before performing operations on them.


#isinstance is used to check the datatype fo the varible 


# A string is a sequence of characters surrounded by either single or double quotation marks. Python treats both forms as strings, so you can use either one. Here are some examples:

# my_str_1 = 'Hello'  //  this is  the snake case 
# my_str_2 = "World"

#Multiline string 
my_str_1 = """My names
are Bizimana Eric"""

my_str_2 = '''My names
are Bizimana eric'''
