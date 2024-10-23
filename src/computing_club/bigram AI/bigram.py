from random import choice

class BigramAI:
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
        paragraph = paragraph.replace('…', '')
        paragraph = paragraph.replace('—', '')
        paragraph = paragraph.replace('(', '')
        paragraph = paragraph.replace(')', '')
        paragraph = paragraph.replace('\n', ' ')
        paragraph = paragraph.replace('  ', ' ')

        # Make sublists
        paragraph = paragraph.split()
        for index in range(len(paragraph)):
            if index != len(paragraph) - 1:
                if paragraph[index] in words.keys():
                    words[paragraph[index]].append(paragraph[index+1])
                else:
                    words[paragraph[index]] = [paragraph[index+1]]

        return words

    def generate_text(self, start, word_amount=100):
        cur_word = start.lower()
        words = 0
        while True:
            if words == word_amount:
                break
            print(cur_word, end=' ')
            cur_word = choice(self.reference[cur_word])
            words += 1


if __name__ == '__main__':
    b = BigramAI()
    b.generate_text(input())