
def new_person(name: str, age: int):
    # Sprawdzamy warunki poprawności danych
    if name == "" or " " not in name or len(name) > 40:
        raise ValueError("Imię musi składać się z co najmniej dwóch słów i mieć max 40 znaków.")
    
    if age < 0 or age > 150:
        raise ValueError("Wiek musi być w przedziale od 0 do 150.")

    return (name, age)
        


        
        
#person = new_person('', 20)