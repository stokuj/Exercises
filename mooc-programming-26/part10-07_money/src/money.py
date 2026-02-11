# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02} eur"

    def __eq__(self, another):
        if self._euros == another._euros and self._cents == another._cents:
            return True
        return False
    
    def __ne__(self, another):
        if self._euros == another._euros and self._cents == another._cents:
            return False
        return True
    
    def __lt__(self, another):
        x = self._euros + self._cents * 0.01
        y  = another._euros + another._cents * 0.01
        if x < y:
            return True
        return False
    
    def __gt__(self, another):
        x = self._euros + self._cents * 0.01
        y  = another._euros + another._cents * 0.01
        if x > y :
            return True
        return False
    
    def __add__(self, another):
        euros = self._euros + another._euros
        cents = self._cents + another._cents
        while cents >= 100:
            cents -= 100
            euros += 1
        m = Money(euros, cents)
        return m   
    
    def __sub__(self, another):

            total_cents1 = self._euros * 100 + self._cents
            total_cents2 = another._euros * 100 + another._cents
            
            diff_cents = total_cents1 - total_cents2
            
            if diff_cents < 0:
                raise ValueError("a money object cannot have a negative value")
            
            new_euros = diff_cents // 100
            new_cents = diff_cents % 100
            
            return Money(new_euros, new_cents)
    
    
if __name__ == "__main__":
    print(e1)
    e1.euros = 1000
    print(e1)