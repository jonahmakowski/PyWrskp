from fun_stuff import FunStuff
import strange_stuff_helper as helper
import time

fun = FunStuff()
fun.collect_info()

helper.white_black(5)

helper.clear_screen()

passcode = input('What is the passcode?')
passcode.encode('utf-8')

if not helper.check_password(passcode):
    exit()
