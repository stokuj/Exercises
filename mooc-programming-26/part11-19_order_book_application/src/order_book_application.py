# Write your solution here:

class Task():
    next_id = 1
    
    def __init__(self, description: str, programmer: str, workload: int):
        self.id = Task.next_id  #  aktualne ID
        Task.next_id += 1       # +1 dla następnego obiektu
        
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self._is_finished = False
        
    def __str__(self):
        if self._is_finished == False:
            return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED'
        else:
            return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED'

    def is_finished(self):
        return self._is_finished
    
    def mark_finished(self):
        self._is_finished = True
    
    
class OrderBook():
    def __init__(self):
        self._all_orders = []
        self._programmers = []
        
    def add_order(self, description: str, programmer: str, workload: int):
        task = Task(description, programmer, workload)
        self._all_orders.append(task)
        
        if programmer not in self._programmers:
            self._programmers.append(programmer)
            
    def all_orders(self):
        return self._all_orders
            
    def programmers(self):
        return self._programmers
    
    def mark_finished(self, id: int):
        for task in self._all_orders:
            if task.id == id:
               task.mark_finished()
               return
        raise ValueError("No task with the given id")
    
    def finished_orders(self) -> list:
        return [task for task in self._all_orders if task.is_finished()]
        
    def unfinished_orders(self) -> list:
        return [task for task in self._all_orders if not task.is_finished()]
    
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("No programmer with the given name")
        
        tasks_of_programer = [task for task in self._all_orders if task.programmer == programmer]
        finished = [task for task in tasks_of_programer if task.is_finished()]
        unfinished = [task for task in tasks_of_programer if not task.is_finished()]
        
        # Count tasks
        finished_count = len(finished)
        unfinished_count = len(unfinished)
        
        # Sum workloads
        finished_hours = sum(task.workload for task in finished)
        unfinished_hours = sum(task.workload for task in unfinished)
        
        return (finished_count, unfinished_count, finished_hours, unfinished_hours)
 
    
class OrderBookApp():
    def __init__(self):
        self.__order_book = OrderBook()
    
    def help(self):
        print('commands:')
        print('0 exit')
        print('1 add order')
        print('2 list finished tasks')
        print('3 list unfinished tasks')
        print('4 mark task as finished')
        print('5 programmers')
        print('6 status of programmer')

    
    def run(self):
        self.help()
        
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished()
            elif command == "3":
                self.list_unfinished()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.list_programmers()
            elif command == "6":
                self.status_of_programmer()
            else:
                self.help()
                
    def add_order(self):
        description = input("description: ")
        line = input("programmer and workload estimate: ")
        parts = line.split()
        
        # Error handling for missing or invalid workload
        try:
            if len(parts) < 2:
                print("erroneous input")
                return
            
            programmer = parts[0]
            workload = int(parts[1])
            
            self.__order_book.add_order(description, programmer, workload)
            print('added!')
        except ValueError:
            print("erroneous input")
        
    def list_finished(self):
        if len(self.__order_book.finished_orders()) == 0:
            print('no finished tasks')
            return
        
        for task in self.__order_book.finished_orders():
            print(task)
            
    def list_unfinished(self):
        if len(self.__order_book.unfinished_orders()) == 0:
            print('no unfinished tasks')
            return
        
        for task in self.__order_book.unfinished_orders():
            print(task)
           
    def mark_finished(self):
        try:
            id = int(input("id: "))
            self.__order_book.mark_finished(id)
            print("marked as finished")
        except ValueError:
            print("erroneous input")
        
    def list_programmers(self):
        for programmer in self.__order_book.programmers():
            print(programmer)
    
    def status_of_programmer(self):
        programmer = input("programmer: ")
        try:
            a, b, c, d = self.__order_book.status_of_programmer(programmer)
            print(f'tasks: finished {a} not finished {b}, hours: done {c} scheduled {d}')
        except ValueError:
            print("erroneous input")
    
        
app = OrderBookApp()
app.run()