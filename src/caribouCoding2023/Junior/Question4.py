amount = int(input())
nums = []
output = []


for i in range(amount):
    v1 = int(input())
    v2 = int(input())
    nums.append([v1, v2])

for item in nums:
    output.append(item[0] * item[1])

for item in output:
    print(item)
