class Stack: 
    
    def __init__(self):
        self.list = []
    
    
    def push(self, val):
        self.list.append(val)
        
    def pop(self):
        
        if self.isEmpty():
            return 'List is Empty'
        
        return self.list.pop()
    
    def peak(self):
        
        if self.isEmpty():
            return 'List is Empty'
        
        return self.list[-1]
    
    def isEmpty(self):
        if len(self.list) == 0:
            return 'list is Empty'


    