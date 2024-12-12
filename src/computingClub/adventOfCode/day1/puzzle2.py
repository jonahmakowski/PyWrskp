def do_challange():
    with open('input.txt') as f:
        lines = f.readlines()
    
    list_one = []
    list_two = []

    for line in lines:
        spli = line.strip().split('   ')
        list_one.append(int(spli[0]))
        list_two.append(int(spli[1]))
    
    amounts = []

    for num in list_one:
        amount = 0
        for num2 in list_two:
            if num2 == num:
                amount += 1
        amounts.append(amount)
    
    sum = 0

    for index, num in enumerate(list_one):
        sum += num * amounts[index]
    
    return sum

if __name__ == '__main__':
    print(do_challange())