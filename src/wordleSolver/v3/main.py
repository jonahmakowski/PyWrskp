import sys
sys.path.append('../')
from five_letters import get_five_letters, get_words
import multiprocessing


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
            if word_lis[index] not in word_wrong and (word_lis[index] not in word_correct or word_lis[index] in word_wrong_place.keys()):
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

def make_copies(word_list, word_correct, word_wrong_place, word_wrong):
    word_list_copy = word_list.copy()
    word_correct_copy = word_correct.copy()
    word_wrong_copy = word_wrong.copy()
    word_wrong_place_copy = {}
    for letter in word_wrong_place.keys():
        word_wrong_place_copy[letter] = word_wrong_place[letter].copy()
    
    return word_list_copy, word_correct_copy, word_wrong_copy, word_wrong_place_copy

def give_rank_central(word_list, word_correct, word_wrong_place, word_wrong, splits):
    split_amount = int(len(word_list) / splits)
    threads = []
    ranks_raw = [None] * splits
    for id in range(splits-1):
        x = multiprocessing.Process(target=give_rank, args=(word_list[split_amount*id:(split_amount*id+1)-1], word_list, word_correct, word_wrong_place, word_wrong, id, ranks_raw,))
        x.start()
        threads.append(x)
        print('Started distributer {}'.format(id))

    x = multiprocessing.Process(target=give_rank, args=(word_list[split_amount*splits], word_list, word_correct, word_wrong_place, word_wrong, id, ranks_raw,))
    x.start()
    threads.append(x)
    print('Started distributer {}'.format(splits))

    for thread in threads:
        thread.join()
    
    ranks = []
    for ranks_set in ranks_raw:
        ranks.extend(ranks_set)

def give_rank(words, word_list, word_correct, word_wrong_place, word_wrong, id, ranks_out):
    ranks = [None] * len(words)
    threads = []
    for index, word in enumerate(words):
        thread = multiprocessing.Process(target=give_one_rank, args=(word, word_list, word_correct, word_wrong_place, word_wrong, index, ranks,))
        thread.start()
        threads.append(thread)
        if index % 10 == 0:
            print('Started thread {}/{} in id {}'.format(index, len(word_list), id))
    
    print('--------------------- Started All Threads ---------------------')

    for i, thread in enumerate(threads):
        thread.join()
        print('Merged Thread {}'.format(i))

    ranks_out[id] = ranks

def give_one_rank(word, word_list, word_correct, word_wrong_place, word_wrong, index, ranks):
    if len(word) != 5:
        try:
            raise ValueError('Word {} at index {} is shorter than five'.format(word, word_list.index(word)))
        except ValueError:
            raise ValueError("Word {} is shorter than five, and isn't in word list".format(word))
    word_list_copy, word_correct_copy, word_wrong_copy, word_wrong_place_copy = make_copies(word_list, word_correct, word_wrong_place, word_wrong)
    word_correct_copy, word_wrong_place_copy, word_wrong_copy = parse_input('sssss', word, word_correct_copy, word_wrong_place_copy, word_wrong_copy)
    rank = abs(len(find_all_valid(word_list_copy, None, word_correct_copy, word_wrong_place_copy, word_wrong_copy)) - len(word_list))
    ranks[index] = rank
        

def find_all_valid(words:list, ranks, word_correct:list, word_wrong_place:dict, word_wrong:list):
    index = 0
    while index < len(words):
        word = words[index]
        if not check_valid_word(word, word_correct, word_wrong_place, word_wrong):
            words.pop(index)
            if ranks is not None: ranks.pop(index)
        else:
            index += 1
    return words, ranks

def find_highest_points(words, ranks):
    high = 0
    high_index = -1
    for index, _ in enumerate(words):
        if ranks[index] > high:
            high = ranks[index]
            high_index = index

    return high_index

def remove_invalid_word_from_file(word, file='../words.txt'):
    words = get_words(file=file)
    words.pop(words.index(word))
    
    while word in words:
        words.pop(words.index(word))
    
    with open(file, 'w') as f:
        f.write('\n'.join(words) + '\n')
    print('Removed file from words.txt, will be saved for next time.')


def solver(starting_word="crane", splits=5):
    with open('../five_letter_words.txt', 'r') as file:
        words_temp = file.readlines()

    words = []
    for word in words_temp:
        words.append(word.strip())

    word_correct = ['', '', '', '', ''] # Letters in correct place
    word_wrong_place = {} # Give letter, and then a list of places with incorrect location
    word_wrong = [] # Letters that aren't in the word at all
    ranks = give_rank_central(words, word_correct, word_wrong_place, word_wrong, splits)

    if starting_word in words:
        index = words.index(starting_word)
        words.pop(index)
        ranks.pop(index)

    print('Correct (in correct place): C, semi-correct (in wrong place): S, Wrong (not in word): W')

    print('Guess 1: {}'.format(starting_word))
    (word_correct,
     word_wrong_place,
     word_wrong) = parse_input(input(), starting_word, word_correct, word_wrong_place, word_wrong)


    guess = 2
    while True:
        words, ranks = find_all_valid(words, ranks, word_correct, word_wrong_place, word_wrong)

        print('There are {} words left'.format(len(words)))

        if len(words) == 0:
            print("Unfortunatly, we've run out of words.")
            break

        word = words[find_highest_points(words, ranks)]

        print('Guess {}: {}'.format(guess, word))
        inp = input()
        if inp == 'n':
            words.pop(words.index(word))
            remove_invalid_word_from_file(word)
            continue
        
        (word_correct,
         word_wrong_place,
         word_wrong) = parse_input(inp, word, word_correct, word_wrong_place, word_wrong)

        if word_correct == list(word):
            print('{} is the correct word. Worked at guess {}'.format(word, guess))
            break
        guess += 1

if __name__ == '__main__':
    get_five_letters(in_file='../words.txt', out_file='../five_letter_words.txt')
    solver()
