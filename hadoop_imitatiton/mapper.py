import sys

for line in sys.stdin:
    # check for marked lines
    if line.startswith('BG:'):
        # remove marker, leading and trailing whitespace, and double spaces
        line = line[3:].replace('  ', ' ').strip()
        # split the line into words using space as tokenizer
        words = line.split()
        for word in words:
            print(word)
