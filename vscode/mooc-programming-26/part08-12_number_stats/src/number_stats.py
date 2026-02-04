class NumberStats:
    def __init__(self):
        self._numbers = 0
        self._counter = 0
        self._sum_even = 0
        self._sum_odd = 0

    def add_number(self, number: int):
        self._numbers += number
        self._counter += 1
        if number % 2 == 0:
            self._sum_even += number
        else:
            self._sum_odd += number

    def get_sum(self):
        return self._numbers

    def get_sum_even(self): 
        return self._sum_even

    def get_sum_odd(self): 
        return self._sum_odd

    def average(self):
        if self._counter == 0:
            return 0
        return self._numbers / self._counter


stats = NumberStats()

print('Please type in integer numbers:')
while True:
    option = int(input(''))
    if option == -1:
        break
    
    stats.add_number(option)
print(f'Sum of numbers: {stats.get_sum()}')
print(f'Mean of numbers: {stats.average()}')
print(f'Sum of even numbers: {stats.get_sum_even()}')
print(f'Sum of odd numbers: {stats.get_sum_odd()}')
        
        
    