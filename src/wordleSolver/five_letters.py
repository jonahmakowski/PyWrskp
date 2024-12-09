def get_words(file='words.txt'):
    with open(file, 'r') as f:
        words_temp = f.readlines()

    words = []
    for word in words_temp:
        word = word.strip()
        word = word.lower()
        these_words = word.split()
        words.extend(these_words)
    
    return words

def get_five_letters(in_file='words.txt', out_file='five_letter_words.txt'):
    invalid_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '_', '~', '.', '$', '[', ']', '{', '}', '%', '!', ',', '/', '(', ')', '\\', '#', '*', "'", '"']


    five_letters = []

    words = get_words(file=in_file)

    for word in words:
        word = word.lower()
        if len(word) == 5:
            valid = True

            for letter in word:
                if letter in invalid_chars:
                    valid = False
            
            if valid:
                five_letters.append(word.lower())

    five_letters = list(set(five_letters))
    five_letters.sort()

    print('Loaded {} words'.format(len(words)))

    with open(out_file, 'w') as file:
        file.write('\n'.join(five_letters) + '\n')

if __name__ == '__main__':
    get_five_letters()
