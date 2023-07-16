import time

def clear_screen():
    for i in range(100):
        print()
def black_screen():
    for i in range(20):
        print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
        
def white_black(length):
    while length >= 0:
        clear_screen()
        time.sleep(length)
        black_screen()
        time.sleep(length)
        if length >= 4:
            length -= 1
        if length >= 3:
            length -= 0.75
        if length >= 2:
            length -= 0.5
        if length >= 1:
            length -= 0.25
        if length < 1:
            length -= 0.1

def check_password(password):
    password.decode('utf-8')
    
    if password == '118':
        return True
    else:
        return False
    
