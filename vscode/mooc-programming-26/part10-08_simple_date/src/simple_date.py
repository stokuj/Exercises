class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year
        
    def __str__(self):
        return f'{self._day}.{self._month}.{self._year}'

    def __eq__(self, value):
        return (self._year == value._year and 
                self._month == value._month and 
                self._day == value._day)
    
    def __ne__(self, value):
        return not self.__eq__(value)
    
    def __gt__(self, another):
        if self._year != another._year:
            return self._year > another._year
        if self._month != another._month:
            return self._month > another._month
        return self._day > another._day
    
    def __lt__(self, another):
        if self._year != another._year:
            return self._year < another._year
        if self._month != another._month:
            return self._month < another._month
        return self._day < another._day
    
    def __add__(self, days: int):
        y = self._year
        m = self._month
        d = self._day + days

        while d > 30:
            d -= 30
            m += 1
            
        while m > 12:
            m -= 12
            y += 1

        return SimpleDate(d, m, y)
    
    def __sub__(self, another: 'SimpleDate'):
        x1 = self._year * 360 + self._month * 30 + self._day
        x2 = another._year * 360 + another._month * 30 + another._day
        return abs(x1 - x2)

if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2 - d1) # Powinno być 28
    print(d1 - d2) # Powinno być 28
    print(d1 - d3) # Powinno być 12516