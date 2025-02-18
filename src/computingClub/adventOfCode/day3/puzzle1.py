import pyWrkspPackage

def main():
    """
    Reads data from "input.txt" and processes it to find and evaluate specific patterns.
    The function looks for occurrences of the pattern "mul(a,b)" in the data, where 'a' and 'b' 
    are numeric values. It then extracts these values, multiplies them, and sums the results.
    Returns:
        int: The sum of all evaluated "mul(a,b)" patterns found in the data.
    """
    data = pyWrkspPackage.load_from_file("input.txt")
    
    valid = []

    for index, character in enumerate(data):
        found_mul = False
        if (character == 'm' and data[index + 1] == 'u') and (data[index + 2] == 'l' and data[index + 3] == '('):
            found_mul = True
        
        number_valid = [False, False, False]
        if found_mul:
            for ind in range(4, 12):
                if not data[index+ind].isnumeric():
                    number_valid[0] = True
                if data[index+ind] == ',':
                    number_valid[1] = True
                if data[index+ind] == ')':
                    number_valid[2] = True
                    break
            if (number_valid[0] and number_valid[1]) and number_valid[2]:
                valid.append(data[index+4:index+11])
    
    s = 0

    for mul in valid:
        values = mul.split(',')
        a = int(values[0])
        temp = list(values[1])
        while not temp[-1].isnumeric():
            temp.pop(-1)
        b = int(pyWrkspPackage.list_to_str(temp))
        s += a * b
    
    return s

if __name__ == "__main__":
    print(main())
