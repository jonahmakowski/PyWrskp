from random import randint

def main(input_list:list):
    accross = int(len(input_list) / 2)
    amount = 0
    for index, hat_num in enumerate(input_list):
        cur_accross = (accross + index) % len(input_list)
        if hat_num == input_list[cur_accross]:
            amount += 1

    return amount

def make_test_list(amount, m):
    lis = []
    for _ in range(amount):
        lis.append(randint(0, m))
    return lis

if __name__ == '__main__':
    lis = make_test_list(1000000, 100)
    #print(lis)
    print()
    print(main(lis))