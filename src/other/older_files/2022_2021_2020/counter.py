count_type = input('What count type would you like to use?\n')
if count_type == 'with spaces':
    string = input('Paste what you want to count\n')
    string = list(string)

    print('Here is the length of your text:')
    print(len(string))
else:
    print('you have choosen not including spaces')
    string = input('Paste what you want to count\n')
    string = list(string)
    
    count = 0
    length = len(string)
    
    for i in range(len(string)):
        item = string[count]
        if item == ' ':
            del string[count]
            # print(string) # uncommenting this will make the current list print
        else:
            count += 1

    print('Here is the length of your text:')
    print(len(string))
    print()
    print('your text without spaces is:')
    
    stri = ''
    for item in string:
        stri += item
    
    print(stri)