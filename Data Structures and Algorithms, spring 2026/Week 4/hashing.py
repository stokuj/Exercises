

def letter_to_int(letter: str) -> int:
    return ord(letter) - ord('a')


def hash_value(string):
    result = 0
    n = len(string)
    for index, char in enumerate(string):
        result += letter_to_int(char) * 23**(n-index-1)
        #print(index, char, result, n, n-index-1)
    return result % 2**32

if __name__ == "__main__":
    print(hash_value("abc")) # 25
    print(hash_value("kissa")) # 2905682
    print(hash_value("aybabtu")) # 154753059
    print(hash_value("tira")) # 235796
    print(hash_value("zzzzzzzzzz")) # 2739360440