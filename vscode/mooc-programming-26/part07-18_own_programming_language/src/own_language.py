# Write your solution here
import string

CHARS = string.ascii_uppercase

def init_values() -> dict:
    dict_ = {}
    for i in range(26):
        dict_[CHARS[i]] = 0

    return dict_

def mov(char1: str, number: int, values: dict):
    values[char1] = number  

def print_value_of_variable(char: str, values: dict):
    print(values[char])

def add(char1: str, number: int, values: dict):
    values[char1] += number  
   
def sub(char1: str, number: int, values: dict):
    values[char1] -= number  
   
def mul(char1: str, number: int, values: dict):
    values[char1] -= number  
     
def run(list_of_instructions: list):
    
    values_dict = init_values()
    i = 0
    while i < len(list_of_instructions):
        parts = list_of_instructions[i].split()
        operation, variable = parts[0], parts[1]
        if operation == 'PRINT':
            print_value_of_variable(variable, values_dict)
        elif operation == 'MOV':
            value = parts[2]
            mov(variable, value, values_dict)
        i += 1
    pass


if __name__ == "__main__":
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    #program1.append("END")
    result = run(program1)
    print(result)