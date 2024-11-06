from random import choice
import json

class NgramAI:
    def __init__(self, length:int, file_load=True, making_lists=0):
        self.length = length
        self.reference = None
        if making_lists == 0:
            if not file_load: self.load_reference()
            else: self.load_reference_from_file()
        else:
            self.length = 2
            while self.length <= making_lists:
                self.load_reference()
                print('Made list for {}'.format(self.length))
                self.length += 1
        self.length = length

    def load_reference(self):
        words = {}

        with open('input.txt', 'r') as f:
            input_text = f.read()

        input_text = input_text.lower()

        # Removing all punctuation
        input_text = input_text.replace(',', '')
        input_text = input_text.replace('.', '')
        input_text = input_text.replace('!', '')
        input_text = input_text.replace('"', '')
        input_text = input_text.replace('?', '')
        input_text = input_text.replace(':', '')
        input_text = input_text.replace(';', '')
        input_text = input_text.replace('“', '')
        input_text = input_text.replace('”', '')
        input_text = input_text.replace('…', ' ')
        input_text = input_text.replace('—', ' ')
        input_text = input_text.replace('(', '')
        input_text = input_text.replace(')', '')
        input_text = input_text.replace('-', '')
        input_text = input_text.replace('~', '')
        input_text = input_text.replace('*', '')
        input_text = input_text.replace('’', '')
        input_text = input_text.replace("'", '')
        input_text = input_text.replace('\n', ' ')
        for i in range(10):
            input_text = input_text.replace('  ', ' ')

        with open('formated_paragraph.txt', 'w') as f:
            f.write(input_text)

        # Make sub-lists
        input_text = input_text.split()

        for index in range(len(input_text)):
            try:
                last_n_words = ''
                for i in range(self.length-1, 0, -1):
                    last_n_words += input_text[index - i] + ' '

                last_n_words = last_n_words[:-1]

                if last_n_words in words.keys():
                    words[last_n_words].append(input_text[index])
                else:
                    words[last_n_words] = [input_text[index]]
            except IndexError:
                pass

        with open('cache/output_{}.txt'.format(self.length), 'w') as f:
            json.dump(words, f)

        self.reference = words

    def load_reference_from_file(self):
        with open('cache/output_{}.txt'.format(self.length), 'r') as f:
            self.reference = json.load(f)

    @staticmethod
    def make_list_into_str(lis):
        output = ''
        for item in lis:
            output += str(item) + ' '

        output = output[:-1]

        return output

    def generate_text(self, start, word_amount=100):
        cur_words = start.lower().split()
        for word in cur_words: print(word, end=' ')

        words = 0
        while True:
            if words == word_amount:
                break

            active_word = choice(self.reference[self.make_list_into_str(cur_words)])
            del cur_words[0]
            cur_words.append(active_word)
            print(active_word, end=' ')
            words += 1
        print()


if __name__ == '__main__':
    b = NgramAI(4, making_lists=0)
    inp = input('Provide an input: ')
    for r in range(1, 6):
        print('\t\t{}: '.format(r), end='')
        b.generate_text(inp, word_amount=1000)
