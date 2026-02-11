# Write your solution here
import string


def init_values() -> dict:
    CHARS = string.ascii_uppercase
    dict_ = {}
    for i in range(26):
        dict_[CHARS[i]] = 0

    return dict_

def print_value_of_variable(char: str, values: dict, result: list) -> list:
    if char in values:
        result.append(values[char])
    else:
        result.append(int(char))

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

    # 1) First pass: collect label -> line index
    labels = {}
    for idx, line in enumerate(list_of_instructions):
        parts = line.split()
        if not parts:
            continue
        if parts[0].endswith(':'):
            label = parts[0][:-1]
            labels[label] = idx

    def resolve_value(token: str) -> int:
        return values_dict[token] if token in values_dict else int(token)

    def eval_condition(var: str, op: str, rhs_token: str) -> bool:
        left = values_dict[var]
        right = resolve_value(rhs_token)
        if op == '==':
            return left == right
        if op == '!=':
            return left != right
        if op == '<':
            return left < right
        if op == '<=':
            return left <= right
        if op == '>':
            return left > right
        if op == '>=':
            return left >= right
        raise ValueError(f'Unknown operator: {op}')

    # 2) Execute
    i = 0
    while i < len(list_of_instructions):
        parts = list_of_instructions[i].split()
        if not parts:
            i += 1
            continue

        # label-only or label+instruction line
        if parts[0].endswith(':'):
            parts = parts[1:]
            if not parts:
                i += 1
                continue

        operation = parts[0]

        if operation == 'END':
            return result

        if operation == 'JUMP':
            label = parts[1]
            i = labels[label]
            continue

        if operation == 'IF':
            # IF [var] [op] [value] JUMP [label]
            var = parts[1]
            op = parts[2]
            rhs = parts[3]
            label = parts[5]
            if eval_condition(var, op, rhs):
                i = labels[label]
                continue
            i += 1
            continue

        variable = parts[1]

        if operation == 'PRINT':
            print_value_of_variable(variable, values_dict, result)
        else:
            variable2 = parts[2]
            value = resolve_value(variable2)

            if operation == 'MOV':
                mov(variable, value, values_dict)
            elif operation == 'ADD':
                add(variable, value, values_dict)
            elif operation == 'SUB':
                sub(variable, value, values_dict)
            elif operation == 'MUL':
                mul(variable, value, values_dict)

        i += 1

    return result


if __name__ == "__main__":
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)
