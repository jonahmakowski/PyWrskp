import random
import time


class IDK:
    def __init__(self):
        self.loading('Starting Systems')

    def loading(self, loading):
        self.clear_screen()
        print('Loading {}:'.format(loading))
        print('▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯')
        time.sleep(random.randint(1, 3))
        self.clear_screen()
        print('Loading {}:'.format(loading))
        print('█ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯')
        time.sleep(random.randint(1, 3))
        self.clear_screen()
        print('Loading {}:'.format(loading))
        print('█ █ ▯ ▯ ▯ ▯ ▯ ▯ ▯ ▯')
        time.sleep(random.randint(1, 3))
        self.clear_screen()
        print('Loading {}:'.format(loading))
        print('█ █ █ ▯ ▯ ▯ ▯ ▯ ▯ ▯')
        time.sleep(random.randint(1, 3))
        self.clear_screen()
        print('Loading {}:'.format(loading))
        print('█ █ █ █ ▯ ▯ ▯ ▯ ▯ ▯')
        time.sleep(random.randint(1, 3))
        self.clear_screen()
        print('Loading {}:'.format(loading))
        print('█ █ █ █ █ ▯ ▯ ▯ ▯ ▯')
        time.sleep(random.randint(1, 3))
        self.clear_screen()
        print('Loading {}:'.format(loading))
        print('█ █ █ █ █ █ ▯ ▯ ▯ ▯')
        time.sleep(random.randint(1, 3))
        self.clear_screen()
        print('Loading {}:'.format(loading))
        print('█ █ █ █ █ █ █ ▯ ▯ ▯')
        time.sleep(random.randint(1, 3))
        self.clear_screen()
        print('Loading {}:'.format(loading))
        print('█ █ █ █ █ █ █ █ ▯ ▯')
        time.sleep(random.randint(1, 3))
        self.clear_screen()
        print('Loading {}:'.format(loading))
        print('█ █ █ █ █ █ █ █ █ ▯')
        time.sleep(random.randint(1, 3))
        self.clear_screen()
        print('Loading {}:'.format(loading))
        print('█ █ █ █ █ █ █ █ █ █')
        self.clear_screen()
        print('{} is loaded!'.format(loading))

    def clear_screen(self):
        for i in range(100):
            print()
