

def count_parts(songs):
    n = len(songs)
    
    pos = {}
    start = 0
    count = 0
    
    for i, song in enumerate(songs):
        if song in pos:
            start = max(start, pos[song] + 1)
        length = max(length, i - start + 1)
        
        pos[song] = i
        

    return count

def max_length(songs):
    n = len(songs)
    
    pos = {}
    start = 0
    length = 0
    
    for i, song in enumerate(songs):
        if song in pos:
            start = max(start, pos[song] + 1)
        length = max(length, i - start + 1)
        
        pos[song] = i
        
    return length


if __name__ == "__main__":
    print(count_parts([1, 1, 1, 1])) # 4
    print(count_parts([1, 2, 3, 4])) # 10
    print(count_parts([1, 2, 1, 2])) # 7
    print(count_parts([1, 2, 1, 3])) # 8
    print(count_parts([1, 1, 2, 1])) # 6

    songs = [1, 2] * 10**5
    print(count_parts(songs)) # 399999
    songs = list(range(1, 10**5 + 1)) * 2
    print(count_parts(songs)) # 15000050000