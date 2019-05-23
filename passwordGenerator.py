#Password generator
#Generates a "random" (as random as a computer can be) sequence of printable ASCII characters
import random
random.seed()

length = int(raw_input("Length? "))
password = ''

for i in range(length):
	password += chr(random.randint(33,126))

print password
