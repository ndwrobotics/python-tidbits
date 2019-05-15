#Accepts input as a string of 0s and 1s, and returns the ascii text corresponding to it.
binary_array = list(raw_input("binary (no spaces):"))

for j in range(len(binary_array) % 8):
    binary_array.pop()


bytes_array = []
while len(binary_array) >= 8:
    next_byte = 0
    for i in range(8):
        if int(binary_array.pop()) == 1:
            next_byte += 2**i
    bytes_array.append(chr(next_byte))

bytes_array.reverse()
print "".join(bytes_array)
