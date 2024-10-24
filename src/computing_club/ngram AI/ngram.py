from random import choice

class NgramAI:
    def __init__(self, length:int):
        self.length = length
        self.reference = self.load_reference()

    def load_reference(self):
        words = {}
        with open('input.txt', 'r') as f:
            paragraph = f.read()

        paragraph = paragraph.lower()

        # Removing all punctuation
        paragraph = paragraph.replace(',', '')
        paragraph = paragraph.replace('.', '')
        paragraph = paragraph.replace('!', '')
        paragraph = paragraph.replace('"', '')
        paragraph = paragraph.replace('?', '')
        paragraph = paragraph.replace(':', '')
        paragraph = paragraph.replace(';', '')
        paragraph = paragraph.replace('“', '')
        paragraph = paragraph.replace('”', '')
        paragraph = paragraph.replace('…', ' ')
        paragraph = paragraph.replace('—', ' ')
        paragraph = paragraph.replace('(', '')
        paragraph = paragraph.replace(')', '')
        paragraph = paragraph.replace('-', '')
        paragraph = paragraph.replace('\n', ' ')
        paragraph = paragraph.replace('  ', ' ')
        paragraph = paragraph.replace('  ', ' ')

        # Make sub-lists
        paragraph = paragraph.split()

        for index in range(len(paragraph)):
            try:
                lastN_words = ''
                for i in range(-1, -self.length-1, -1):
                    lastN_words += paragraph[index-i] + ' '

                lastN_words = lastN_words[:-1]

                if lastN_words in words.keys():
                    words[lastN_words].append(paragraph[index])
                else:
                    words[lastN_words] = [paragraph[index]]
            except IndexError:
                pass

        with open('output.txt', 'w') as f:
            f.write(str(words))

        return words

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


if __name__ == '__main__':
    b = NgramAI(3)
    b.generate_text(input('Provide an input: '))
