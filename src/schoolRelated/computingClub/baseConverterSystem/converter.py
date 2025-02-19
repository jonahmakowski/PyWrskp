abcs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$', '%', '^', '&', '*',
        '(', ')', '-', '_', '+', '=', '.', ',', '[', ']', '{', '}', ':', ';', "'", '"', '?']

def float_to_base_n(abcs, flo:int, base:int):
    result_lis = []
    while flo != 0:
        result_lis.append(flo % base)
        flo = int(flo / base)

    result_str = ''

    result_lis.reverse()

    for num in result_lis:
        if num <= 9:
            result_str += str(num)
        else:
            if num-10 > len(abcs)-10:
                print('The base value of {} is too large'.format(base))
                return
            else:
                result_str += abcs[num-10]


    return result_str

if __name__ == '__main__':
    print(float_to_base_n(abcs, int(input('Input the number: ')), int(input('Input the base: '))))
