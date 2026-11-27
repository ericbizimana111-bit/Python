# nums = [3, 1, 4, 1, 5]
# nums.append(9)
# print(nums[0], nums[-1], len(nums))
# print(sorted(nums))

student = {"name": "Ada", "grades": [90, 85]} #dictionary
student["age"] = 25

for  key, value in student.items():
    print(key, value) # in python here ,(comma) separate multiple values passed to the print() function

    # .keys()   return all keys
    # .values() return all values
    # .items()  returns all keys and values


# squares = [n ** 2 for n in range(6)] # list comprehension
# print(squares)
