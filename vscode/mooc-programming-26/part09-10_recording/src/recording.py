# WRITE YOUR SOLUTION HERE:


class Recording():
    def __init__(self, size: int):
        if size < 0:
            raise ValueError("The lenght must not be below zero")
        self.__length = size

    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, size: int):
        if size < 0:
            raise ValueError("The lenght must not be below zero")
        self.__length = size
        
        
if __name__ == "__main__":
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)