# write your solution here
def read_fruits() -> dict:
    
    fruits = {}
    with open('fruits.csv') as file:
        for line in file:
            line = line.replace('\n',"")
            parts = line.split(';')
            name = parts[0]
            price = float(parts[1])
            #print(line, name, price)
            fruits[name] = price
        
    return fruits

#read_fruits()