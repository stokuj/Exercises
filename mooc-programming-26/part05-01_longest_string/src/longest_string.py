# Write your solution here

def longest(strings: list) -> str:
    
    size, index = 0, 0
    for i, word in enumerate(strings):
        if len(word) > size:
            size = len(word)
            index = i
            
    return strings[index]

#print(longest(['trest', 'testee']))