# Write your solution here
def squared(word, num):
    try:
        index = 0
        for i in range(0, num):
            for j in range(0, num):
                
                print(word[index % len(word)], end ='')
                index += 1
            print('')
    except:
        print("An exception occurred", index)

if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)