def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')

    # enumerate is used to get both the index (position) and the value of each item in an iterable.
    # we can also use enumerate(lines, start=1)  start at showing index(position) one then print starting from valuelines) at index 0
    for line_index, line in enumerate(lines, start=1):
        print(line_index, line)
        words = line.split()
        print(len(words[line_index]))

        # print(words) this prints arrays of words in every line in every iteration
        #  ['Stars', 'and', 'the', 'moon'] 
        #  ['shine', 'in', 'the', 'sky']
        #  ['white', 'and', 'bright']
        #  ['until', 'the', 'end', 'of', 'the', 'night']

    
poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)


