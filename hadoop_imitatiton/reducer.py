import sys


def print_res():
    print('\t'.join([current_word, str(current_count)]))


# initial values
current_word = None
current_count = 0

for line in sys.stdin:
    word = line.rstrip()  # clean \n
    if current_word == word:
        current_count += 1
    else:
        if current_word:
            print_res()
        current_count = 1
        current_word = word
# print last word when loop ends
print_res()
