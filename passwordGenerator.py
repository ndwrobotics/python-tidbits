#Password generator
#Generates a "random" (as random as a computer can be) sequence of printable ASCII characters from the hard-coded characters string.
import random
random.seed()

while True:
    try:
        length = int(input("Length? "))
        break
    except ValueError:
        print("Enter a number.")

password = ''
characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*?"
for i in range(length):
	password += characters[random.randint(0, len(characters)-1)]

print(password)
