poem = """
my names are bizimana eric
i live in the guinea country
and i love and respect my God"""

def split_all(poem):
    lines = poem.split('\n')

    for line in lines:
        words = line.split()
        print(words)
        print('\n')
        print(line)


print(split_all(poem))

