import itertools

def getPermutations(lis):
    return list(itertools.combinations(lis, 2))

first = input().split()
second = input().split()

combos = 0

tsum = int(first[1])
who = int(first[2])

permuations = getPermutations(second)
for item in permuations:
    if int(item[0]) + int(item[1]) == tsum:
        combos += 1

if combos%2+who == 1:
    print("aurpine")
else:
    print("kushanzaveri" + str(int(combos/2)))