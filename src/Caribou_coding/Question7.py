inp1 = input().split(':')
inp2 = input().split(':')

print(inp1, inp2)

min1 = int(inp1[1]) + int(inp1[0] * 60)
min2 = int(inp2[1]) + int(inp2[0] * 60)

print(min1, min2)

print(min1 - min2)
