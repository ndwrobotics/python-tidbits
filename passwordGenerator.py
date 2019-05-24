#Password generator
#Generates a "random" (as random as a computer can be) sequence of printable ASCII characters
import random
random.seed()

while True:
    try:
        length = int(raw_input("Length? "))
        break
    except ValueError:
        print "Enter a number."

password = ''

for i in range(length):
	password += chr(random.randint(33,126))

print password
