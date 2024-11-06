def get_five_letters():
    five_letters = []
    with open('words.txt', 'r') as file:
        words_temp = file.readlines()

    words = []
    for word in words_temp:
        word = word.strip()
        these_words = word.split()
        words.extend(these_words)

    count = 0
    for word in words:
        if len(word) == 5:
            count += 1
            five_letters.append(word.lower())
            print("{} {}".format(count, word))

    with open('five_letter_words.txt', 'w') as file:
        file.write('\n'.join(five_letters) + '\n')

get_five_letters()
