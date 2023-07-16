def printCombination(arr, n, r):
    data = [0]*r;
    combinationUtil(arr, data, 0,
                    n - 1, 0, r);
def combinationUtil(arr, data, start,
                    end, index, r):
                         
    # Current combination is ready
    # to be printed, print it
    if (index == r):
        for j in range(r):
            print(data[j], end = " ");
        print();
        return;
    i = start;
    while(i <= end and end - i + 1 >= r - index):
        data[index] = arr[i];
        combinationUtil(arr, data, i + 1,
                        end, index + 1, r);
        i += 1;
 
arr = [];
while True:
    add = input('what would you like to add?')
    if add == '':
        break
    arr.append(add)
r = int(input('size of possiblities'));
n = len(arr);
printCombination(arr, n, r);