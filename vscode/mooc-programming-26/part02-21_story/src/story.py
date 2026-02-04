# Write your solution here

story = ""
last_word = ""

while True:
    current_word = input("Please type in a word: ")

    # Check for both exit conditions: "end" or a repeat
    if current_word == "end" or current_word == last_word:
        break
    
    # Add the word to the story with a space
    story += current_word + " "
    
    # Update last_word for the next comparison
    last_word = current_word
    
print(story)