from stack import Stack
class BalanceParentheses:
    
    def __init__(self, str = "{[()]}"):
        self.str = str
        self.stack = Stack()
        
    
    def insertString(self):
        str = self.str
        openingTags = "{[("
        
        for k in str:
            if k in openingTags:
                self.stack.push(k)

    