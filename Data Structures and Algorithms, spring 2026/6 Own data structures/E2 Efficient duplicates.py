# Implement a class SuperStack with the following methods:

# push(x): add the element x to the top of the stack
# push_many(k, x): add k copies of the element x to the top of the stack
# top(): access the element at the top of the stack
# pop(): remove the element at the top of the stack


class SuperStack():
    def __init__(self):
        self._stack = []
        
    def push(self, x :int):
        self._stack.append((1, x ))
        
    def pop(self):
        last = self.stack[-1]
        if last[0] == 1:
            self.stack.pop()
        else:
            self.stack[-1] = (last[0] - 1, last[1])
        
    def top(self):
        return self._stack[-1][1]
    
    def push_many(self, copies: int, x: int):
        self._stack.append((copies, x))
            
            
            
s = SuperStack()
s.push_many(3, 8)
s.push(4)
s.push_many(2, 5)

