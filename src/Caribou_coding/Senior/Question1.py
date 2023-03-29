inpu = input()

inpu_lis = list(inpu)
output_lis = list(range(len(inpu_lis)))

index = len(inpu_lis) - 1

for item in inpu_lis:
    output_lis[index] = item
    index -= 1

output = ''
for item in output_lis:
    output += item
print(output)
