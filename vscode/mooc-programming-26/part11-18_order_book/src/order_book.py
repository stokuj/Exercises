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
 
    
if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)
