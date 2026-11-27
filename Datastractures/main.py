# Structure        Example              Use

# list             [1, 2, 3]         Ordered, changeable collection
# tuple            (1, 2)            Ordered, cannot change
# dict             {'a': 1}          Key-value pairs (like a real dictionary)
# set              {1, 2, 3}         Unique items, fast membership check     

# Structure	            Python syntax	           Example

# List	                list_name = [ ]	           numbers = [1, 2, 3]
# Tuple	                tuple_name = ( )	       numbers = (1, 2, 3)
# Dictionary	        dict_name = {key: value}   student = {"name": "Eric", "age": 18}
# Set	                set_name = { }	           numbers = {1, 2, 3}            

# 1. List
numbers = [1, 2, 3]
numbers.append(4)

# 2. Tuple
numbers = (1, 2, 3)

# 3. Dictionary
student = {"name": "Eric", "age": 18}
print(student["name"])

# 4. Set
numbers = {1, 2, 3}
numbers.add(4)