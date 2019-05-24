#Accepts input as a string of 0s and 1s, and returns the ascii text corresponding to it.
binary_array = list(raw_input("binary (no spaces):"))

#Truncate the input to have a number of characters divisible by 8
for j in range(len(binary_array) % 8):
    binary_array.pop()

bytes_array = []
while len(binary_array) >= 8:
    next_byte = 0
    for i in range(8):
        next_bit = binary_array.pop()
        try:
            if int(next_bit) == 1:
                next_byte += 2**i
            elif int(next_bit) == 0:
                continue
            else:
                raise ValueError
        except ValueError:
            print "input is not pure binary"
    bytes_array.append(chr(next_byte))

bytes_array.reverse()
print "".join(bytes_array)
