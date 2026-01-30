def histogram(word : str):
    
    hashMap = {}
     
    for char in word:
        if char in hashMap:
            hashMap[char] += 1
        else:
            hashMap[char] = 1

    for x in hashMap:
        row = x + ' ' + '*' * hashMap[x]
        print(row)
        
        
# histogram("abba")
# histogram("statistically")