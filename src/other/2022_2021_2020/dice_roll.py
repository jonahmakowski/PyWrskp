from random import randint as rand

print('Welcome to DICE SPIN!')
while True:
    try:
        sides = int(input('How many sides would you like your dice to have?     '))
        break
    except:
        print('you did not enter a number')
nums = []
tick = 1
nums = [*range(1, sides, 1)]
spin_nums = []
tick = 1
while True:
    try:
        spins = int(input('How many times would you like to spin your die?     '))
        break
    except:
        print('you did not enter a number')
while True:
    spin = nums[rand(0, len(nums) - 1)]
    spin_nums.append(spin)
    tick += 1
    if tick == spins + 1:
        break
print('Now displaying numbers!')

spin_nums = sorted(spin_nums)

dic_spin = {}

for num in spin_nums:
    try:
        dic_spin[str(num)].append(num)
    except:
        dic_spin[str(num)] = [num]
for item in range(sides):
    try:
        num = len(dic_spin[str(item + 1)])
        print('\n' + str(item + 1) + ', was rolled ' + str(num) + ' times!')
    except:
        pass
