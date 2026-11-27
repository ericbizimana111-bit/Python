# # nums = [3, 1, 4, 1, 5]
# # nums.append(9)
# # print(nums[0], nums[-1], len(nums))
# # print(sorted(nums))

# student = {"name": "Ada", "grades": [90, 85]} #dictionary
# student["age"] = 25

# for  key, value in student.items():
#     print(key, value) # in python here ,(comma) separate multiple values passed to the print() function

#     # .keys()   return all keys
#     # .values() return all values
#     # .items()  returns all keys and values


# squares = [n ** 2 for n in range(6)] # list comprehension
# print(squares)

# squares = [n ** 2 for n in range(6)] # n starts from 0
# print(squares) # [0, 1, 4, 9, 16, 25]



# for n in range(6):
#     squares = [] # Every time the loop repeats, Python creates a NEW empty list.The previous list is replaced.Each list stores only one number.
#     squared_number = n**2
#     squares.append(squared_number)
#     print(squares, end= " ") # output [0] [1] [4] [9] [16] [25]




#the ouput is different when squares list is declared outside the function
squares = []
for n in range(6):
    squared_number = n**2
    squares.append(squared_number)
print(squares) 
# [1, 4, 9, 16, 25]
# Why?
# - Python creates the list only once.
# - Every loop adds another number to the same list.
# - Previous values remain in the list.