inp1 = input()
inp2 = input()

inp1 = list(inp1)
inp2 = list(inp2)

inp1.sort()
inp2.sort()

if inp1 == inp2:
    print('yes')
else:
    print('no')