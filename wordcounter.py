"""
REQUIREMENTS FOR THE MINI-PROJECT
1. Print a welcome message to the user
2. Take a string(message) and a letter from the user
3.Count How many times the letter occurs
4. Calculate the percentage of the letter in the message
5. Print the output to the user
"""

print("Hello there! Welcome to the letter counter ")

#This will remove the whitespace and only consider actual characters
message = input("Please type your message here. ").lower().strip()

letter = input("What letter(s) would you like to count? ").lower()

#Count the letter selected by the user in the message
word_count = message.count(letter)
print(f"The number of {letter}'s is {word_count}")

#Calculating the percentage of the letter in the message
total_word_count = len(message)
percentage = (word_count/total_word_count) * 100

print(f"The letter is {percentage} percent of your message")