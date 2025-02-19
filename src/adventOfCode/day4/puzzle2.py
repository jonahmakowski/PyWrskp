import pyWrkspPackage

def do_diagnals(data):
    amount = 0
    for index, row in enumerate(data):
        for char_index, char in enumerate(row):
            valid = [False, False]
            if char == 'A':
                if index + 1 < len(data) and char_index + 1 < len(row) and index - 1 >= 0 and char_index - 1 >= 0:
                    if data[index+1][char_index+1] == 'M' and data[index-1][char_index-1] == 'S':
                        valid[0] = True
                    elif data[index+1][char_index+1] == 'S' and data[index-1][char_index-1] == 'M':
                        valid[0] = True
                if index - 1 >= 0 and char_index + 1 < len(row) and index + 1 < len(data) and char_index - 1 >= 0:
                    if data[index-1][char_index+1] == 'M' and data[index+1][char_index-1] == 'S':
                        valid[1] = True
                    elif data[index-1][char_index+1] == 'S' and data[index+1][char_index-1] == 'M':
                        valid[1] = True
                if valid == [True, True]:
                    amount += 1
    return amount

def main():
    data = pyWrkspPackage.load_from_file("input.txt").split('\n')
    
    amount = do_diagnals(data)

    return amount

print(main())
