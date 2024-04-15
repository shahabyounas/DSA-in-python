class Range:
    
    def __init__(self, start, stop=None, step=1) -> None:
        
        if step == 0:
            raise ValueError('step can not be 0')
        
        if stop is None:
            start, stop = 0, None
        
        self._length = max(0, stop - start + step - 1 // step)
        self._start = start
        self._step = step
    
    def __len__(self):
        return self._length
    
    def __getitem__(self, k):
        if k < 0:
            print(self, len(self))
            k += len(self)
        
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
    
        return self._start + k * self._step
    
for idx in Range(1, 100):
    pass