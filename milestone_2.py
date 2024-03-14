import random


word_list= ["apple", "banana", "orange", "grape", "kiwi"] 

word = random.choice(word_list)
guess = input("Enter a single letter: " )
print(word_list) 
print(word)


'''
In this task, you are required to take user input. As you now know, the print() function in Python displays output on the screen. Conversely
, Python has an input() function that takes input from the screen. Note that the input function returns the user input in form of a string.


Step 1:
Using the input function, ask the user to enter a single letter.


Step 2:
Assign the input to a variable called guess.

'''