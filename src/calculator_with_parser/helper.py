# Token Types #
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_ADD = 'ADD'
TT_SUB = 'SUB'
TT_INT = 'INT'
TT_FLO = 'FLO'
ALL_TTs = (TT_MUL, TT_DIV, TT_ADD, TT_SUB, TT_INT, TT_FLO)
###############

class Token:
    def __init__(self, tt, value=None):
        if tt in ALL_TTs: type = tt else: 
        self.value = value

class Parser:
    def __init__(self, text):
        self.text_str = text
        self.text = list(text)
        self.pos = -1
        self.index = None

    def advance(self):
        self.pos += 1
        self.index = self.text[self.pos]
