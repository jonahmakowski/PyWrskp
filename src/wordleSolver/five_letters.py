def get_five_letters():
    invalid_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '_', '~', '.', '$', '[', ']', '{', '}', '%', '!', ',', '/', '(', ')', '\\', '#', '*']


    five_letters = []
    with open('words.txt', 'r') as file:
        words_temp = file.readlines()

    words = []
    for word in words_temp:
        word = word.strip()
        word = word.lower()
        these_words = word.split()
        words.extend(these_words)

    for word in words:
        word = word.lower()
        if len(word) == 5:
            valid = True

            for letter in word:
                if letter in invalid_chars:
                    valid = False
            
            if valid:
                five_letters.append(word.lower())
                print('Found {}'.format(word.lower()))

    five_letters = list(set(five_letters))
    five_letters.sort()

    print('Found {} words'.format(len(words)))

    with open('five_letter_words.txt', 'w') as file:
        file.write('\n'.join(five_letters) + '\n')

get_five_letters()
