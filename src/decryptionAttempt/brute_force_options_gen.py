import string
from itertools import permutations


def generate_permutations(x, y, file):
    for p in permutations(y, x):
        with open(file, "a") as f:
            f.writelines("".join(p) + '\n')


chars = list(string.ascii_letters)

for char in range(len(chars)):
    chars[char] = chars[char].lower()

chars = list(set(chars))
chars.sort()

threads = []
file_name = "brute_force_options.txt"

with open(file_name, "w") as f:
    f.writelines('')

for length in range(1, 11):
    generate_permutations(length, chars, file_name)
    print('Generated set {}'.format(length))
