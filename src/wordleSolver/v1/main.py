from random import choice

def parse_input(inp, word, word_correct, word_wrong_place, word_wrong):
    word_lis = list(word)
    index = 0
    for letter in inp:
        if letter.lower() == "c":
            word_correct[index] = word_lis[index]
        elif letter.lower() == "s":
            if word_wrong_place.get(word_lis[index]) is not None:
                word_wrong_place[word_lis[index]].append(index)
            else:
                word_wrong_place[word_lis[index]] = [index]
        elif letter.lower() == "w":
            if word_lis not in word_wrong:
                word_wrong.append(word_lis[index])
        else:
            print('There was an invalid input, terminating')
            exit()
        index += 1
    return word_correct, word_wrong_place, word_wrong

def check_valid_word(word, word_correct, word_wrong_place, word_wrong):
    word_lis = list(word)
    index = 0

    for letter in word_lis:
        if letter.lower() != word_correct[index] and word_correct[index] != '':
            #print("Word {} doesn't work at letter {} for not being in correct list, correct was {}"
                  #.format(word, letter, word_correct[index]))
            #print(word_correct, word_wrong_place, word_wrong)
            return False
        elif letter.lower() in word_wrong:
            #print("Word {} doesn't work at letter {} for letter in wrong list".format(word, letter))
            return False
        elif word_wrong_place.get(word_lis[index]) is not None:
            if index in word_wrong_place[word_lis[index]]:
                #print("Word {} doesn't work at letter {} for having letter in wrong spot".format(word, letter))
                return False
        index += 1

    for letter in word_wrong_place.keys():
        if letter not in word_lis:
            # print("Word {} doesn't work at letter {} for not having a letter in the semi wrong list".format(word,letter))
            return False

    return True

def solver(starting_word="crane"):
    with open('../five_letter_words.txt', 'r') as file:
        words_temp = file.readlines()

    words = []
    for word in words_temp:
        words.append(word.strip())

    word_correct = ['', '', '', '', ''] # Letters in correct place
    word_wrong_place = {} # Give letter, and then a list of places with incorrect location
    word_wrong = [] # Letters that aren't in the word at all

    if starting_word in words:
        words.pop(words.index(starting_word))

    print('Correct (in correct place): C, semi-correct (in wrong place): S, Wrong (not in word): W')

    print('Guess 1: {}'.format(starting_word))
    (word_correct,
     word_wrong_place,
     word_wrong) = parse_input(input(), starting_word, word_correct, word_wrong_place, word_wrong)


    guess = 2
    while True:
        if len(words) == 0:
            print("The word isn't on the list")
            break
        word = choice(words)
        if not check_valid_word(word, word_correct, word_wrong_place, word_wrong):
            words.pop(words.index(word))
            continue
        print('Guess {}: {}'.format(guess, word))
        inp = input()
        if inp == 'n':
            words.pop(words.index(word))
            continue
        (word_correct,
         word_wrong_place,
         word_wrong) = parse_input(inp, word, word_correct, word_wrong_place, word_wrong)

        if word_correct == list(word):
            print('{} is the correct word. Worked at guess {}'.format(word, guess))
            break
        guess += 1

solver()
