# Create a program that prompts the user to input their name once.
# Then, the program repeatedly 10 times prints out the name with the first letter capitalized.

name = input('enter your name: ')
for x in range(10):
    print(name.capitalize())
