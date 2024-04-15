from abc import ABCMeta, abstractmethod

class Sequence(metaclass = ABCMeta):
    
    @abstractmethod
    def __len__(self):
        """ Return the length of sequence"""
    
    @abstractmethod
    def __getitem__(self,j):
        """Return the element at index j of sequence"""
        
    def __contains__(self, val):
        for j in range(len(self)):
            if self[j] == val:
                return True
        
        return False
    
    def index(self, val):
        
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')
    
    def count(self, val):
        
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k
    

seq = Sequence() # Should error, abstract class can not be instantiated