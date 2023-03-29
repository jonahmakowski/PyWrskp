colors = ['Red', 'White', 'Orange']
col_one = input()
col_two = input()

index = 0

while len(colors) > 1:
    if colors[index] == col_one or colors[index] == col_two:
        del colors[index]
    else:
        index += 1

print(colors[0])
