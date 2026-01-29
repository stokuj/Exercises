# Write your solution here

def most_common_character(word: str) -> str:
    my_list = []
    for char in word:
        my_list.append(word.count(f'{char}'))
    
    
    index = my_list.index(max(my_list))
    #print(index)
    return word[index]

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))