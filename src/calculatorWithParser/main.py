from helper import *

expression = input('Type a mathimatical expression:\n')

p = Parser(expression)
tokens = p.make_tokens()
o = Order(tokens)
ordered_tokens = o.make_order()
print(ordered_tokens)
s = Solve(ordered_tokens)
print(s.expression)
