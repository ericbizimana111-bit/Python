# Dictionaries inside dictionaries
# This is the most important concept in this project: nested dictionaries.
# Suppose two different keys produce the same hash value.
# For example, "dear" and "read" both produce 412.
# Instead of replacing one value with the other, you store both inside another dictionary:

collection = {

    412: 
      {"dear": "friend",        
       "read": "book"    }
}



# Understand the structure:
# - 412 is the hash value.
# - "dear" and "read" are the original keys.
# - "friend" and "book" are their values.
# This is called collision handling.



# Collision handling with nested dictionaries means storing multiple items that share the same hash number inside a smaller inner dictionary so no data gets overwritten.

# Why Collisions Happen

# • Hash values can repeat: A hash function turns a word into a number. Sometimes, two different words (like "dear" and "read") end up with the exact same number (412).
# • The overwriting problem: In a normal dictionary, each key must be unique. If you save "dear" at 412 and then save "read" at 412, "read" would erase "dear".

# How Nested Dictionaries Fix It

# Instead of storing just one value at 412, you store an inner dictionary at 412.
# Think of collection like a building with numbered mailboxes:
# • Outer Key (412): This is the mailbox number (the hash value).
# • Inner Dictionary ({ ... }): This is the mailbox itself, which can hold multiple letters.
# • Inner Keys ("dear", "read"): These are the names on the letters (the original words).
# • Inner Values ("friend", "book"): These are the contents inside each letter.

# How Finding Data Works

# When your program looks up "read", it follows two quick steps:
# • Step 1 (Outer lookup): It calculates the hash of "read" (412) and goes straight to mailbox 412.
# • Step 2 (Inner lookup): It looks inside mailbox 412 for the exact word "read" and pulls out "book", leaving "dear": "friend" completely safe.
# Would you like to see how to write the Python code to add and retrieve items from this nested structure, or should we look at how to delete items from it?
