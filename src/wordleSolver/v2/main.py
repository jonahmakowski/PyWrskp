import sys
sys.path.append('../')
from five_letters import get_five_letters, get_words


def parse_input(inp, word, word_correct, word_wrong_place, word_wrong):
    """
    Parses the input string and updates the word_correct, word_wrong_place, and word_wrong lists/dictionaries
    based on the input.

    Args:
        inp (str): A string where each character represents the status of the corresponding letter in the word.
                   'c' or 'C' indicates the letter is correct and in the correct place.
                   's' or 'S' indicates the letter is correct but in the wrong place.
                   'w' or 'W' indicates the letter is incorrect.
        word (str): The word being evaluated.
        word_correct (list): A list where the correct letters in the correct positions are stored.
        word_wrong_place (dict): A dictionary where the keys are letters that are correct but in the wrong place,
                                 and the values are lists of indices where these letters appear.
        word_wrong (list): A list of letters that are incorrect.

    Returns:
        tuple: A tuple containing the updated word_correct list, word_wrong_place dictionary, and word_wrong list.
    """
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
    """
    Checks if a given word is valid based on the provided constraints.

    Args:
        word (str): The word to be checked.
        word_correct (list): A list where each index contains the correct letter for that position or an empty string if the position is unknown.
        word_wrong_place (dict): A dictionary where keys are letters and values are lists of indices where the letter should not be.
        word_wrong (list): A list of letters that should not be in the word.

    Returns:
        bool: True if the word is valid based on the constraints, False otherwise.
    """
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

def give_rank(word_list):
    """
    Assigns a rank to each word in the given list based on the presence of specific letters.

    The function uses predefined letter rankings to calculate a rank for each word. 
    Each letter has a specific rank value, and the rank of a word is the sum of the 
    rank values of the letters it contains.

    Parameters:
    word_list (list of str): A list of words to be ranked.

    Returns:
    list of int: A list of ranks corresponding to the words in the input list.
    """
    rank1 = ['q', 'j', 'x']
    rank2 = ['z', 'w', 'k']
    rank3 = ['v', 'f', 'y']
    rank4 = ['b', 'h', 'm']
    rank5 = ['p', 'g', 'u']
    rank6 = ['d', 'c', 'l']
    rank7 = ['t', 'n']
    rank8 = ['r', 'i', 'o']
    rank9 = ['s', 'e', 'a']

    ranks = []

    for word in word_list:
        cur_rank = 0
        for letter in rank1:
            if letter in word:
                cur_rank += 1
        for letter in rank2:
            if letter in word:
                cur_rank += 2
        for letter in rank3:
            if letter in word:
                cur_rank += 3
        for letter in rank4:
            if letter in word:
                cur_rank += 4
        for letter in rank5:
            if letter in word:
                cur_rank += 5
        for letter in rank6:
            if letter in word:
                cur_rank += 6
        for letter in rank7:
            if letter in word:
                cur_rank += 7
        for letter in rank8:
            if letter in word:
                cur_rank += 8
        for letter in rank9:
            if letter in word:
                cur_rank += 9
        ranks.append(cur_rank)

    return ranks

def find_all_valid(words:list, ranks:list, word_correct:list, word_wrong_place:dict, word_wrong:list):
    """
    Filters out invalid words from the given list of words based on the provided criteria.

    Args:
        words (list): List of words to be filtered.
        ranks (list): List of ranks corresponding to the words.
        word_correct (list): List of characters that are correct and in the correct position.
        word_wrong_place (dict): Dictionary where keys are positions and values are lists of characters that are correct but in the wrong position.
        word_wrong (list): List of characters that are incorrect and should not be in the word.

    Returns:
        tuple: A tuple containing the filtered list of words and their corresponding ranks.
    """
    index = 0
    while index < len(words):
        word = words[index]
        if not check_valid_word(word, word_correct, word_wrong_place, word_wrong):
            words.pop(index)
            ranks.pop(index)
        else:
            index += 1
    return words, ranks

def find_highest_points(words, ranks):
    """
    Finds the index of the word with the highest rank.

    Args:
        words (list of str): A list of words.
        ranks (list of int): A list of ranks corresponding to each word.

    Returns:
        int: The index of the word with the highest rank. If no words are provided, returns -1.
    """
    high = 0
    high_index = -1
    for index, _ in enumerate(words):
        if ranks[index] > high:
            high = ranks[index]
            high_index = index

    return high_index

def remove_invalid_word_from_file(word, file='../words.txt'):
    """
    Removes all occurrences of a specified word from a file containing a list of words.
    Args:
        word (str): The word to be removed from the file.
        file (str, optional): The path to the file containing the list of words. Defaults to '../words.txt'.
    Returns:
        None
    Side Effects:
        Modifies the specified file by removing all occurrences of the given word.
        Prints a confirmation message after the word has been removed.
    """
    words = get_words(file=file)
    words.pop(words.index(word))
    
    while word in words:
        words.pop(words.index(word))
    
    with open(file, 'w') as f:
        f.write('\n'.join(words) + '\n')
    print('Removed file from words.txt, will be saved for next time.')


def solver(starting_word="crane"):
    """
    Solves the Wordle puzzle by making guesses and refining the list of possible words based on feedback.
    Args:
        starting_word (str): The initial word to start the guessing process. Default is "crane".
    The function reads a list of five-letter words from a file, ranks them, and iteratively makes guesses based on the feedback provided by the user. The feedback should be in the form of:
        - 'C' for letters in the correct place,
        - 'S' for letters in the word but in the wrong place,
        - 'W' for letters not in the word at all.
    The function continues to make guesses until the correct word is found or there are no more words left to guess.
    Returns:
        None
    """
    with open('../five_letter_words.txt', 'r') as file:
        words_temp = file.readlines()

    words = []
    for word in words_temp:
        words.append(word.strip())

    ranks = give_rank(words)

    word_correct = ['', '', '', '', ''] # Letters in correct place
    word_wrong_place = {} # Give letter, and then a list of places with incorrect location
    word_wrong = [] # Letters that aren't in the word at all

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
