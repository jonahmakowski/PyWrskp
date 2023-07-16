i = 200
c = 100

num = int(input('What number are you looking for?\n'))

for i in range(num - 1):
    c -= i
    i -= 1
    c += i
    i -= 1

print(c)
