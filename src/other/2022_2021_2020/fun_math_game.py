num = 1
money = 0
streak = 0
add = 1

while True:
    q = (str(num) + ' + ' + str(num))
    question = input('What is ' + q + '?\n')
    an = str(num + num)
    if question == an:
        print('good job\nyou earned $' + str(num))
        money += num
        streak += 1
        print('you have a streak of ' + str(streak))
        if int(streak / 5) >= 1:
            add = int(streak / 5)
        elif int(streak / 5) < 1:
            add = 1
    elif question != an:
        print('you got it incorrect the correct A is ' + an)
        print('you lost $' + str(int(num / 2)))
        print('you lost a streak of ' + str(streak))
        money -= int(num/2)
        streak = 0
    if streak >= 20:
        num += 10
    if streak >= 30:
        num += 10
    if streak >= 40:
        num += 10
    if streak >= 50:
        num += 10
    if money <= -1000:
        break
    if num >= 1:
        break
    print('you have $' + str(money) + '!')
    num += add
if money <= -1000:
    print('you have lost b/c you have $' + money + ' so you have gone bankrupt')
elif num >= 1:
    print('you have won as you just solved ' + q)
