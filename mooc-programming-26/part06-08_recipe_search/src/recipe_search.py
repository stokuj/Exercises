# write your solution here

# Struktura listy:
# Nazwa; Minuty; Skladnik1; Skladnik2 ... {n składników}
# [' '] - są miedzy listami
def load_recipes(file_name: str) -> list:
    with open(file_name) as file:
        recipes = []
        
        dish = []
        for line in file:
            line = line.strip()
            
            if line:
                dish.append(line)
            else:
                recipes.append(dish)
                dish = []
                
        # To check if last recipe was added to recipes.        
        if dish:
            recipes.append(dish)
                       
    return recipes

def search_by_name(filename: str, word: str) -> list:
    recipes = load_recipes(filename)
    found_recipes_names = []    
    
    for recipe in recipes:
        if word in recipe[0].lower():
            found_recipes_names.append(recipe[0])
    
    return found_recipes_names

def search_by_time(filename: str, prep_time: int) -> list:
    recipes = load_recipes(filename)
    found_recipes = []    
    name_time = ()
    for recipe in recipes:
        if prep_time >= int(recipe[1]):
            found_recipes.append(f'{recipe[0]}, preparation time {recipe[1]} min')

    return found_recipes # List of *str* that contains expected output

def search_by_ingredient(filename: str, ingredient: str) -> list:
    recipes = load_recipes(filename)
    found_recipes = []    
    
    for recipe in recipes:
        for word in recipe:
            if word.lower() == ingredient:
                #print(recipe, ingredient,'yess')
                found_recipes.append(f'{recipe[0]}, preparation time {recipe[1]} min')
    
    return found_recipes

if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)






