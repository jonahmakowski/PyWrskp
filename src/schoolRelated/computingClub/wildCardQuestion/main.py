import itertools

def getPermutations(lis):
    return list(itertools.combinations(lis, 2))

def get_input():
    values = input().split()
    cards = input().split()
    return values[1], values[2], cards

def main():
    k, t, cards = get_input()
    possiblities = 0
    cards_copy = cards.copy()
    while True:
        permutations = getPermutations(cards_copy)
        found = False
        for perm in permutations:
            if int(perm[0]) + int(perm[1]) == int(k):
                possiblities += 1
                found = True
                cards_copy.pop(cards_copy.index(perm[0]))
                cards_copy.pop(cards_copy.index(perm[1]))
        
        if not found:
            break
    
    winner = (0 if t == '1' else 1) if possiblities % 2 == 0 else t
    print("aurpine" if winner == 0 else 'kushanzaveri', int((possiblities / 2) + 1))

if __name__ == "__main__":
    main()