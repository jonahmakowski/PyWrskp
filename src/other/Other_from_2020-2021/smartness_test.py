a = []
print('WELCOME TO MY SMARTNESS TEST')


def q(qu, ae):
    qe = input(qu + '\n')
    if qe == ae:
        return True
    if qe != ae:
        return False


c = ''  # question
d = ''  # question (3 * 3)


def q_idea():
    from random import randint as r
    num = r(2, 3)
    nums = []
    if num == 2:
        num_1 = r(10, 100)
        num_2 = r(50, 150)
        nums.append(num_1)
        nums.append(num_2)
    if num == 3:
        num_1 = r(10, 100)
        num_2 = r(50, 150)
        num_3 = r(100, 200)
        nums.append(num_1)
        nums.append(num_2)
        nums.append(num_3)

    def question_def(opr):
        if len(nums) == 2:
            questionr = ('What is ' + str(nums[0]) + opr + str(nums[1]) + '?')
        if len(nums) == 3:
            questionr = ('What is ' + str(nums[0]) + opr + str(nums[1]) + opr + str(nums[2]) + '?')
        return questionr
    op = r(1, 4)
    if op == 1:
        question = question_def(' + ')
    elif op == 2:
        question = question_def(' - ')
    elif op == 3:
        question = question_def(' * ')
    elif op == 4:
        question = question_def(' / ')
    global c
    global d
    c = question
    if len(nums) == 2:
        if op == 1:
            d = nums[0] + nums[1]
        if op == 2:
            d = nums[0] - nums[1]
        if op == 3:
            d = nums[0] * nums[1]
        if op == 4:
            d = nums[0] / nums[1]
    elif len(nums) == 3:
        if op == 1:
            d = nums[0] + nums[1] + nums[2]
        if op == 2:
            d = nums[0] - nums[1] - nums[2]
        if op == 3:
            d = nums[0] * nums[1] * nums[2]
        if op == 4:
            d = nums[0] / nums[1] / nums[2]


for i in range(9):
    q_idea()
    a.append(q(c, d))
i = 0
for item in a:
    if item:
        i += 1
rank = 'terrible.'
if i >= 1:
    rank = 'bad.'
if i >= 3:
    rank = 'ok.'
if i >= 5:
    rank = 'pretty good.'
if i >= 7:
    rank = 'good.'
if i >= 8:
    rank = 'great!'
if i >= 9:
    rank = 'Outstanding!!'
print('you ranked ' + rank)
