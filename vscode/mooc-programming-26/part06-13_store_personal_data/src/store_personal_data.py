# Write your solution here

def store_personal_data(person: tuple):
    with open('people.csv', 'a') as file: #appendd
        name, age, height = person
        line = f'{name};{age};{height}'
        file.write(line)
        pass
        
if __name__ == "__main__":  
    store_personal_data(("Paul Paulson", 37, 175.5))