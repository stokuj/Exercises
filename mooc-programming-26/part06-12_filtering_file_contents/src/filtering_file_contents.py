# Write your solution here

def write_file(filename:str, lines: list):
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)

def filter_solutions():
    
    correct, incorrect = [], []
    
    with open('solutions.csv') as file:
        for line in file:
            parts = line.split(';')
            calculated_value = 0
            name, equation, result = parts[0], parts[1], int(parts[2])
            
            if "+" in equation:
                operands = equation.split('+')
                calculated_value = int(operands[0]) + int(operands[1])
            elif "-" in equation:
                operands = equation.split('-')
                calculated_value = int(operands[0]) - int(operands[1])
                
            line = f'{name};{equation};{result}\n'
            
            if calculated_value == result:
                correct.append(line)
            else:
                incorrect.append(line)
    
    write_file('correct.csv', correct)      
    write_file('incorrect.csv', incorrect)
    
if __name__ == "__main__":
    filter_solutions()