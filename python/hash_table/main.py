#A hash table works differently from a normal dictionary: it converts each key into a number called a hash value.
#A hash table is a data structure that stores key-value pairs and uses a hash function to compute an index
student = {
    "name": "Eric",
    "age": 20
}

#the ord function returns the unicode code point for a given character.
print(ord('a')) #97
print(ord('b')) #98 
print(ord('c')) #99

word = 'cart'

result = ord(word[0]) + ord(word[1]) + ord(word[2]) + ord(word[3])
print(result) # 97 + 97 + 114 + 116 = 424
