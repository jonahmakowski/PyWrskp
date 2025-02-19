from random import choice

abcs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z',]

def main(inp):
    values = []
    indexs = {}
    for ind, char in enumerate(inp):
        if char in indexs.keys():
            indexs[char].append(ind)
            values.append(True)
            for index in indexs[char]:
                values[index] = True
        else:
            indexs[char] = [ind]
            values.append(False)

    last = None

    result = True
    for statement in values:
        if statement is last:
            result = False
        last = statement

    print('T' if result else 'F')


def make_test(length):
    result = ''

    for _ in range(length):
        result += choice(abcs)

    return result

if __name__ == '__main__':
    LENGTH = 10
    AMOUNT = 5
    for i in range(LENGTH):
        lis = make_test(AMOUNT)
        print(lis)
        main(lis)