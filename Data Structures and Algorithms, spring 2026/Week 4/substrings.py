def count_substrings(string):
    n = len(string)
    
    sub_str = set()
    for i in range(n):
        for j in range(i +1, n+1):
            sub_str.add(string[i:j])

    return len(sub_str)

if __name__ == "__main__":
    print(count_substrings("aaaa")) # 4
    print(count_substrings("abab")) # 7
    print(count_substrings("abcd")) # 10
    print(count_substrings("abbbbbb")) # 13
    print(count_substrings("aybabtu")) # 26
    print(count_substrings("saippuakauppias")) # 110