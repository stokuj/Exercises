
# Write your solution here:
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            #self.__persons[name] = []
            self.__persons[name] = Person(name)     #person_obj = Person(name)

        self.__persons[name].add_number(number)     #person_obj.add_number(number)
        
        
    def add_address(self, name: str, address: str):
        if not name in self.__persons:
            #self.__persons[name] = []
            self.__persons[name] = Person(name)     #person_obj = Person(name)

        self.__persons[name].add_address(address)   #person_obj.add_number(number)

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]                 ##person_obj

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def add_address(self):
        name = input("name: ")
        address = input("number: ")
        self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        person_obj = self.__phonebook.get_entry(name)
        if person_obj== None:
            print('address unknown')
            print("number unknown") 
            return
        address = person_obj.address()
        numbers = person_obj.numbers()

        if address == None:
            print('address unknown')
        else:
            print(address)
            
        if not numbers: 
            print("number unknown")
        else:
            for number in numbers:
                print(number)       

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()

class Person:
    def __init__(self, name):
        self._name = name
        self._numbers = []
        self._address = None
     
    def name(self):
        return self._name
      
    def numbers(self):
        return self._numbers
      
    def address(self):
        return self._address

    def add_number(self, n: int):
        if n not in self._numbers:
            self._numbers.append(n)
            
    def add_address(self, a: str):
        self._address = a
        
#when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()
