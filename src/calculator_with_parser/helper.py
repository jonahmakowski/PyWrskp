# Token Types #
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_ADD = 'ADD'
TT_SUB = 'SUB'
TT_NUM = 'NUM'
TT_RPAREN = '('
TT_LPAREN = ')'
TT_EXPRESION = 'EXPERESION'
ALL_TTs = (TT_MUL, TT_DIV, TT_ADD, TT_SUB, TT_NUM, TT_RPAREN, TT_LPAREN, TT_EXPRESION)
###############

DIGITS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
OPS = ('+', '-', '*', '/')


class Token:
    def __init__(self, tt, value=None):
        if tt in ALL_TTs:
            self.tt = tt
        else:
            raise TypeError("Must be one of the Token Types")
        self.value = value

    def __repr__(self):
        return '{}:{}'.format(self.tt, self.value) if self.value is not None else '{}'.format(self.tt)


class Expression:
    def __init__(self, expression):
        self.expression = expression
        self.tt = TT_EXPRESION

    def copy(self):
        return Expression(self.expression)

    def __repr__(self):
        return str(self.expression)


class Parser:
    def __init__(self, text):
        self.text_str = text
        self.text = list(text)
        self.pos = -1
        self.index = None
        self.advance()

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.index = self.text[self.pos]
            return False
        else:
            return True

    def make_tokens(self):
        tokens = []
        while True:
            num = False
            if self.index != ' ':
                if self.index in OPS:
                    if self.index == '*':
                        tokens.append(Token(TT_MUL))
                    elif self.index == '/':
                        tokens.append(Token(TT_DIV))
                    elif self.index == '+':
                        tokens.append(Token(TT_ADD))
                    elif self.index == '-':
                        tokens.append(Token(TT_SUB))
                elif self.index in ('(', ')'):
                    if self.index == '(':
                        tokens.append(Token(TT_RPAREN))
                    elif self.index == ')':
                        tokens.append(Token(TT_LPAREN))
                elif self.index in DIGITS:
                    num = True
                    tokens, stop = self.make_numbers(tokens)
                    if stop:
                        break
                else:
                    raise Exception("Char {} not allowed".format(self.index))

            if not num:
                if self.advance():
                    break

        return Expression(tokens)

    def make_numbers(self, tokens):
        stop = False
        value = ''

        while True:
            if self.index in DIGITS:
                value += self.index
                stop = self.advance()
                if stop:
                    break
            else:
                break

        tokens.append(Token(TT_NUM, value=float(value)))

        return tokens, stop


class Order:
    def __init__(self, expression):
        self.expression = expression
        self.result = []
        self.pos, self.index = None, None
        self.reset()

    def reset(self):
        self.pos = -1
        self.index = None
        self.advance()

    def advance(self):
        self.pos += 1
        if self.pos < len(self.expression.expression):
            self.index = self.expression.expression[self.pos]
            return False
        else:
            return True

    def make_order(self):
        self.error_catching()
        self.parentheses()
        return self.expression

    def parentheses(self):
        while True:
            right_found = []
            left_found = []
            pairs = []
            while True:
                if self.index.tt == TT_LPAREN:
                    left_found.append(self.pos)
                elif self.index.tt == TT_RPAREN:
                    right_found.append(self.pos)

                if self.advance():
                    break
            self.reset()

            while True:
                if len(right_found) == 0:
                    break
                pairs.append((right_found[0], left_found[len(left_found)-1]))
                del right_found[0]
                del left_found[len(left_found)-1]
            
            if len(pairs) == 0:
                break
            
            pair = pairs[len(pairs)-1]
            temp = self.expression.expression
            temp1 = self.expression.expression[pair[0]+1:pair[1]]
            temp_expression = Expression(temp1)
            del temp[pair[0]:pair[1]+1]
            temp.insert(pair[0], temp_expression)
            self.expression = Expression(temp)

    def error_catching(self):
        left_parentheses = 0
        right_parentheses = 0
        while True:
            if self.index.tt in (TT_MUL, TT_DIV, TT_SUB, TT_ADD):
                if (self.pos + 1 < len(self.expression.expression)
                        and self.expression.expression[self.pos+1].tt not in (TT_NUM, TT_RPAREN, TT_LPAREN)):
                    raise Exception('A Number or parentheses must come before and after a operation')
                elif self.pos > 0 and self.expression.expression[self.pos-1].tt not in (TT_NUM, TT_RPAREN, TT_LPAREN):
                    raise Exception('A Number or parentheses must come before and after a operation')
            elif self.index.tt in (TT_RPAREN, TT_LPAREN):
                if (self.pos + 1 < len(self.expression.expression) and self.index.tt == TT_RPAREN
                        and self.expression.expression[self.pos+1].tt != TT_NUM):
                    raise Exception('A Number or parentheses must happen within parentheses')
                elif ((self.pos > 0 and self.index.tt == TT_LPAREN) and
                      (self.expression.expression[self.pos-1].tt != TT_NUM
                       and self.expression.expression[self.pos-1].tt != TT_LPAREN)):
                    raise Exception('A Number or parentheses must happen within parentheses')
                elif self.index.tt == TT_LPAREN:
                    left_parentheses += 1
                elif self.index.tt == TT_RPAREN:
                    right_parentheses += 1
            elif self.index.tt == TT_NUM:
                if self.pos > 0 and self.expression.expression[self.pos-1].tt == TT_NUM:
                    raise Exception('Numbers can not come directly after other numbers')
                elif (self.pos + 1 < len(self.expression.expression)
                      and self.expression.expression[self.pos+1].tt == TT_NUM):
                    raise Exception('Numbers can not come directly after other numbers')
                elif self.pos > 0 and self.expression.expression[self.pos-1].tt == TT_LPAREN:
                    raise Exception("Numbers can not come directly after left (')') parentheses")
                elif (self.pos + 1 < len(self.expression.expression)
                      and self.expression.expression[self.pos+1].tt == TT_RPAREN):
                    raise Exception("Numbers can not come directly before right ('(') parentheses")

            if self.advance():
                break

        if left_parentheses != right_parentheses:
            raise Exception('The number of left and right parentheses must be the same')
        self.reset()

class Solve:
    def __init__(self, expression):
        self.expression = expression
        self.solve()
    
    def solve(self):
        while len(self.expression.expression) > 1:
            cur_expression = self.expression
            index = 0
            expression_found = True
            while expression_found:
                expression_found = False
                for item in cur_expression.expression:
                    if item.tt == TT_EXPRESION:
                        expression_found = True
                        break
                if not expression_found:
                    break
                for item in cur_expression.expression:
                    if type(item) == type(Expression([])):
                        cur_expression = item
                        break
                    index += 1
            print(cur_expression)
            new_expression = self.simple_solve_mul_div(cur_expression)
            new_expression = self.simple_solve_add_sub(new_expression)
            del self.expression.expression[index]
            self.expression.expression.insert(index, new_expression)
    
    def simple_solve_mul_div(self, expression):
        found = False
        for item in expression.expression:
            if item.tt == TT_DIV:
                found = True
                break
            elif item.tt == TT_MUL:
                found = True
                break
        
        while found:
            found = False
            for item in expression.expression:
                if item.tt == TT_DIV:
                    found = True
                    break
                elif item.tt == TT_MUL:
                    found = True
                    break
            if not found:
                break
            index = 0
            for item in expression.expression:
                if item.tt == TT_DIV:
                    prev_val = expression.expression[index-1]
                    next_val = expression.expression[index+1]
                    solve = prev_val.value / next_val.value
                    del expression.expression[index+1]
                    del expression.expression[index]
                    del expression.expression[index-1]
                    expression.expression.insert(index-1, Token(TT_NUM, value=solve))
                    found = True
                    break
                elif item.tt == TT_MUL:
                    prev_val = expression.expression[index-1]
                    next_val = expression.expression[index+1]
                    solve = prev_val.value * next_val.value
                    del expression.expression[index+1]
                    del expression.expression[index]
                    del expression.expression[index-1]
                    expression.expression.insert(index-1, Token(TT_NUM, value=solve))
                    found = True
                    break
                index += 1
            return expression

    def simple_solve_add_sub(self, expression):
        found = False
        for item in expression.expression:
            if item.tt == TT_SUB:
                found = True
                break
            elif item.tt == TT_ADD:
                found = True
                break
        
        while found:
            found = False
            for item in expression.expression:
                if item.tt == TT_SUB:
                    found = True
                    break
                elif item.tt == TT_ADD:
                    found = True
                    break
            if not found:
                break
            index = 0
            for item in expression.expression:
                if item.tt == TT_SUB:
                    prev_val = expression.expression[index-1]
                    next_val = expression.expression[index+1]
                    solve = prev_val.value - next_val.value
                    del expression.expression[index+1]
                    del expression.expression[index]
                    del expression.expression[index-1]
                    expression.expression.insert(index-1, Token(TT_NUM, value=solve))
                    found = True
                    break
                elif item.tt == TT_ADD:
                    prev_val = expression.expression[index-1]
                    next_val = expression.expression[index+1]
                    solve = prev_val.value + next_val.value
                    del expression.expression[index+1]
                    del expression.expression[index]
                    del expression.expression[index-1]
                    expression.expression.insert(index-1, Token(TT_NUM, value=solve))
                    found = True
                    break
                index += 1
            return expression
                    