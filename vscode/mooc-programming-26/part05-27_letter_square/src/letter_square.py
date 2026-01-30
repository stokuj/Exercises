
# For layer 2 we have 3x3 so (n+1)x(n+1)
# For layer 3 we have 5x5
# For layer 4 we have 7x7

layers = int(input("Layers: "))
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 1. Zaczynamy od samego środka (warstwa 1 to zawsze 'A')
result = ["A"]

# 2. W pętli dodajemy kolejne warstwy od 2 do 'layers'
for i in range(1, layers):
    current_char = alphabet[i]
    
    new_width =  len(result[0]) + 2
    
    for j in range(len(result)):
        result[j] = current_char + result[j] + current_char
        
    new_row = current_char * new_width
    result.insert(0, new_row) # Wstaw na początek (góra)
    result.append(new_row)    # Dodaj na koniec (dół)


for row in result:
    print(row)