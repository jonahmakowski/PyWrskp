from math import sqrt

num = 1
correct = 0
wrong = 0
root = 0
round_correct = False

option = int(input('Which option would you like?'))
max_num = int(input('What is the highest number you would like to test?'))


if option == 1:
    while num < max_num:
        root1 = num * num
        root2 = root1 * 2
        num2 = num * 2
        if float(sqrt(root2)) == float(num2):
            round_correct = True
            correct += 1
        else:
            round_correct = False
            wrong += 1
        print(num, root1, num2, root2, round_correct)
        num += 1
        

elif option == 2:
    while num < max_num:
        root = num * num
        if (num % 2) == 0 and (root % 2) == 0:
            correct += 1
            round_correct = True
        elif (num % 2) != 0 and (root % 2) != 0:
            correct += 1
            round_correct = True
        else:
            wrong += 1
            round_correct = False
        print(num, root, round_correct)
        num += 1

elif option == 3:
    while num < max_num:
        root = num * num
        root2 = root + 100
        if float(sqrt(root2)) > float(num + 10) and float(sqrt(root2)) < float(num + 5):
            round_correct = True
            correct += 1
        else:
            round_correct = False
            wrong += 1
        
        print(num, root, root2, round_correct)
        num += 1

elif option == 4:
    diffrence = float(input('What is the diffrence you would like to check?'))
    while num < max_num:
        num1 = num + 1
        sqrt1 = sqrt(num)
        sqrt2 = sqrt(num1)
        if sqrt1 - diffrence < sqrt2 < sqrt1 + diffrence:
            round_correct = True
            correct += 1
        else:
            round_correct = False
            wrong += 1
        
        print(num, sqrt1, sqrt2, round_correct)
        num += 1

print('Amount Correct', correct)
print('Amiount Wrong', wrong)
