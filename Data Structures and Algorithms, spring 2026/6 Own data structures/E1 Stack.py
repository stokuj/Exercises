class Stack():
    def __init__(self):
        self._stack = []
        
    def push(self, x :int):
        self._stack.append(x)
        
    def pop(self):
        self._stack.pop()
        
    def top(self):
        return self._stack[-1]
    
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.top()) # 3
print(s.top()) # 3
s.pop()
print(s.top()) # 2