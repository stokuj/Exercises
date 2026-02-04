# Write your solution here
import string


def init_values() -> dict:
    CHARS = string.ascii_uppercase
    dict_ = {}
    for i in range(26):
        dict_[CHARS[i]] = 0

    return dict_

def print_value_of_variable(char: str, values: dict, result: list) -> list:
    result.append(values[char])

def mov(char1: str, number: int, values: dict):
    values[char1] = number  

def add(char1: str, number: int, values: dict):
    values[char1] += number
   
def sub(char1: str, number: int, values: dict):
    values[char1] -= number
   
def mul(char1: str, number: int, values: dict):
    values[char1] *= number
     
def run(list_of_instructions: list):
    
    values_dict = init_values()
    result = []
    i = 0
    while i < len(list_of_instructions):
        parts = list_of_instructions[i].split()
        
        operation = parts[0]
        if operation == 'END':
            return result
        variable = parts[1]
        
        
        if operation == 'PRINT':
            print_value_of_variable(variable, values_dict, result)
        else:
            variable2, value = parts[2], 0
            
            if variable2 in values_dict:
                value = values_dict[variable2]
            else:
                value = int(variable2)
                
            if operation == 'MOV':
                mov(variable, value, values_dict)
            elif operation == 'ADD':
                add(variable, value, values_dict)  
            elif operation == 'SUB':
                sub(variable, value, values_dict)  
            elif operation == 'MUL':
                mul(variable, value, values_dict)  
        # else:
        #     if 'IF' in operation:
        #         print(parts)
        #         operand = parts[2]
        #         value = int(parts[3])
        #         label = parts[5]
        #         if  values_dict[variable] >= value:
        #             print(f'go {label}')
        i += 1
        #print(result)

    return result

if __name__ == "__main__":
    program1 = ['MOV A 10', 'PRINT A', 'MOV B A', 'SUB B 8', 'PRINT B', 'SUB A B', 'PRINT A'] 
    result = run(program1)
    print(result)