from random import choice

class TrigramAI:
    def __init__(self):
        self.reference = self.load_reference()

    @staticmethod
    def load_reference():
        words = {}
        with open('input_harry.txt', 'r') as f:
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
        paragraph = paragraph.replace('\n', ' ')
        paragraph = paragraph.replace('  ', ' ')

        # Make sublists
        paragraph = paragraph.split()
        for index in range(len(paragraph)):
            try:
                if "{} {}".format(paragraph[index-2], paragraph[index-1]) in words.keys():
                    words[paragraph[index-2]+' '+paragraph[index-1]].append(paragraph[index])
                else:
                    words[paragraph[index-2]+' '+paragraph[index-1]] = [paragraph[index]]
            except IndexError:
                pass

        with open('output.text', 'w') as f:
            f.write(str(words))

        return words

    def generate_text(self, start, word_amount=100):
        word_before = start.lower().split()[0]
        cur_word = start.lower().split()[1]
        print(word_before, cur_word, end=' ')
        words = 0
        while True:
            if words == word_amount:
                break

            active_word = choice(self.reference[word_before + ' ' + cur_word])
            word_before = cur_word
            cur_word = active_word
            print(cur_word, end=' ')
            words += 1


if __name__ == '__main__':
    b = TrigramAI()
    b.generate_text(input())
