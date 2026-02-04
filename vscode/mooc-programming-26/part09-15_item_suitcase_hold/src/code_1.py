
class Item():
    def __init__(self, name: str, weight: int):
        self._name = name
        self._weight = weight
    
    def name(self):
        return self._name
    
    def weight(self):
        return self._weight

    def __str__(self):
        return f'{self._name} ({self._weight} kg)'

class Suitcase():
    def __init__(self, max_w: int):
        self._max_weight = max_w
        self._items = []

    def weight(self):
        total_weight = 0
        for item in self._items:
            total_weight += item.weight()
        return total_weight
    
    def add_item(self, item: Item):
        if self.weight() + item.weight() <= self._max_weight:
            self._items.append(item)
        
    def __str__(self):
        if len(self._items) == 1:
            return f'{len(self._items)} item ({self.weight()} kg)'
        return f'{len(self._items)} items ({self.weight()} kg)'
    
    def print_items(self):
        for item in self._items:
            print(item)
            
    def heaviest_item(self):
        if not self._items:
            return None
        return max(self._items, key = lambda item: item.weight())
    
class CargoHold():
    def __init__(self, max_w: int):
        self._max_weight = max_w
        self._cargo_list = []
        self._weight = 0
    
    def add_suitcase(self, s: Suitcase):
        if self._weight + s.weight() > self._max_weight:
            return
        self._cargo_list.append(s)
        self._weight += s.weight()
        
    def __str__(self):
        size = len(self._cargo_list)
        space_left = self._max_weight - self._weight
        
        if size == 1:
            return f'{size} suitcase, space for {space_left} kg'
        return f'{size} suitcases, space for {space_left} kg'
    
    def print_items(self):
        for item in self._cargo_list:
            item.print_items()
    



if __name__ == "__main__":  
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()