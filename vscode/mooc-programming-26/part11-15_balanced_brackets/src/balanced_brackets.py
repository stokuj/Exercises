
def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True

    brackets = [ char for char in my_string if char in ['(', '[', ']', ')'] ]
    if len(brackets) == 0:
        return True
    if len(brackets) % 2 == 1:
        return False
    
    # Pierwszy znak musi być nawiasem otwierającym
    if brackets[0] not in ['(', '[']:
        return False
    
    # Ostatni znak musi być nawiasem zamykającym
    if brackets[-1] not in [')', ']']:
        return False
    
    # Sprawdź czy typy nawiasów pasują (pierwszy z ostatnim)
    if brackets[0] == '(' and brackets[-1] != ')':
        return False
    if brackets[0] == '[' and brackets[-1] != ']':
        return False
    
    # Usuń pierwszy i ostatni nawias, rekurencyjnie sprawdź środek
    middle = ''.join(brackets[1:-1])
    return balanced_brackets(middle)

# ok = balanced_brackets("([([])])")
# print(ok)

# ok = balanced_brackets("(python version [3.7]) please use this one!")
# print(ok)

# # this is no good, the closing bracket doesn't match    
# ok = balanced_brackets("(()]")
# print(ok)

# # different types of brackets are mismatched
# ok = balanced_brackets("([bad egg)]")
# print(ok)