from helper import *

p = Parser('2*(5+10)')
tokens = p.make_tokens()
print(tokens)
o = Order(tokens)
o.make_order()
