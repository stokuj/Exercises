
def get_sub_strings(string) -> set:
    n = len(string)
    sub_strigns = set()
    for start in range(n):
        for end in range(start+1 , n +1):
            sub_strigns.add(string[start:end])
    return sub_strigns


def create_distribution(string):
    distribution = {}
    
    sub_strigns = get_sub_strings(string)
    for string in sub_strigns:
        n = len(string)
        if n not in distribution:
            distribution[n] = 0
        distribution[n] += 1
    
    return dict(sorted(distribution.items()))

if __name__ == "__main__":
    print(create_distribution("aaaa"))
    # {1: 1, 2: 1, 3: 1, 4: 1}
    
    print(create_distribution("abab"))
    # {1: 2, 2: 2, 3: 2, 4: 1}
    
    print(create_distribution("abcd"))
    #{1: 4, 2: 3, 3: 2, 4: 1}

    print(create_distribution("abbbbbb"))
    # {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 1}

    print(create_distribution("aybabtu"))
    # {1: 5, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1