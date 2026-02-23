# Implement a class Mode with the following methods:

# add(x): add the number x on the list
# mode(): return the mode of the list, i.e., the most frequent number on the list
# The time complexity of each method should be 
# O( 1 )


class Mode:
    def __init__(self):
        self.count = {}
        self.status = (0, 0)
        
    def add(self, x):
        if x not in self.count:
            self.count[x] = 0
        self.count[x] += 1
        self.status = max(self.status, (self.count[x], x))
        
    def mode(self):
        return self.status[1]:
        
        
m = Mode()
m.add(1)
m.add(1)
m.add(2)
print(m.mode()) # 1
m.add(2)
m.add(2)
print(m.mode()) # 2