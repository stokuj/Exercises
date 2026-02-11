# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()
        
    data_json = json.loads(data)
    for person in data_json:
        name = person['name']
        age = person['age']
        hobbies = ''
        for i in range(len(person['hobbies'])):
            hobbies += person['hobbies'][i] + ', '
        print(f'{name} {age} years ({hobbies[:-2]})')
        
if __name__ == "__main__":
    print_persons('file1.json')