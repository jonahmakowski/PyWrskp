import matplotlib.pyplot as plt
import matplotlib as mpl

pattern = [1, 3, 5, 7, 9]
rule = pattern[1] - pattern[0]
formula = 'y={}x+{}'.format(rule, pattern[0])
print('The formula is {}'.format(formula))

ys = []

for i in range(11):
    ys.append((rule*i)+pattern[0])

for y in ys:
    print(y)