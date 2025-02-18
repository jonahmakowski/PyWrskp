def do_challange():
    with open('input.txt') as f:
        lines = f.readlines()
    
    list_one = []
    list_two = []

    for line in lines:
        spli = line.strip().split('   ')
        list_one.append(int(spli[0]))
        list_two.append(int(spli[1]))
    
    list_one.sort()
    list_two.sort()
    distances = []
    
    for index, num in enumerate(list_one):
        distances.append(abs(num - list_two[index]))
    
    sum = 0
    for num in distances:
        sum += num 
    
    return sum

if __name__ == '__main__':
    print(do_challange())
