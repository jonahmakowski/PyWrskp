from random import randint
import os
if __name__ == '__main__':
    try:
        pyWrkspLoc = os.environ["PYWRKSP"]

    except KeyError:
        pyWrkspLoc = os.environ["HOME"] + input('Since you do not have the PYWRSKP env var '
                                                '\nPlease enter the pwd for the pyWrskp repo not including the '
                                                '"home" section')


def create(letter, num, sc, super_c, length, save, print_info, pyWrskp):
    chars = []
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    scs = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '~', '`', '{', '}', '[', ']', ';', ':',
           '"', "'", '<', '>', '?', ',', '.', '/', '|']
    super_s_c = ['←', '↑', '→', '↓', '·', '•', '●', '–', '‽', '‖', '«', '»', '‘', '„', '✅', '❤️', '⌘', '', '⌥', '⌫',
                 '∞', '™', '¼', '½', '¾', 'À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î',
                 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'æ', 'Ħ', 'ĳ', 'Œ',
                 'œ', '☚', '☛', '★', '☆', '♠', '♣', '♥', '♦', '♪', '♫', '♀']
    make = True
    if letter == 'y':
        chars += letters
    if num == 'y':
        chars += nums
    if sc == 'y':
        chars += scs
    if super_c == 'y':
        chars += super_s_c
    if (letter == 'n' and num == 'n') and (sc == 'n' and super_c == 'n'):
        make = False

    password = ''
    if make:
        for i in range(length):
            loc = randint(0, len(chars) - 1)
            password += chars[loc]
    elif not make:
        password = 'Sorry, you have put no in all the questions, so there are no options'
    if print_info:
        print(password)

    if save == 'y':
        website = input('what website will this password be used by?')
        from password_saver import add_password, save_passwords
        add_password(password, website)
        save_passwords(pyWrskp)
        if print_info:
            print('your password, {} has been added to your saved passwords!'.format(password))
    return password


if __name__ == "__main__":
    create(input('Would you like letters? (ex. A, b, c)'),
           input('Would you like numbers? (ex. 1, 2, 3)'),
           input('Would you like special chars? (ex. @, %, -)'),
           input('Would you like super special chars (ex. ←, ↑, →), '
                 '\nsome websites may not allow this, if it does not work turn this off'),
           int(input('how long would you like your password to be?')),
           input('Would you like to save your password to passwords.txt? (y/n)'),
           True,
           pyWrkspLoc)
