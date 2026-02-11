# Write your solution here
def first_word(sentence):
    index = sentence.find(' ')
    return sentence[:index]

def second_word(sentence):
    first_space = sentence.find(' ')
    rest = sentence[first_space+1 :]
    second_space = rest.find(' ')
    if second_space == -1:
        return rest
    return rest[:second_space]

def last_word(sentence):
    index = 0
    while True:
        index = sentence.find(' ')
        sen_tmp = sentence[index+1:]
        if sentence == sen_tmp:
            break
        else:
            sentence = sen_tmp

    return sentence
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
    
    sentence = 'first second'
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))