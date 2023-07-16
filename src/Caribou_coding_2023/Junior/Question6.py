inp1 = int(input())
inp2 = input()
inp2 = inp2.split()
sum_ = 0

numbers = []

for item in inp2:
    numbers.append(int(item))

for item in numbers:
    sum_ += item

average = sum_ / inp1

for item in numbers:
    if item > average:
        print('higher')
    elif item < average:
        print('lower')
    else:
        print('equal')
