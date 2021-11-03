import sys; print(sys.version)
# def ret_value(v):
# 	for char in v:
# 		char.upper()
# 		char = v
# 	return v 
Hex = input("Enter Value: ")
for char in Hex:
	char.upper
dec = int(Hex, 16)
#hex1 = len(Hex)
print("length is", len(Hex))
print("Deciminal Value is", dec)
#print("total length is ", len(hex1))
#for 2's complement 

binary_number = int("{0:08b}".format(dec))

flipped_binary_number = ~ binary_number

flipped_binary_number = flipped_binary_number + 1

str_twos_complement = str(flipped_binary_number)

twos_complement = int(str_twos_complement, 2)

print("2's complement is: ", twos_complement)

def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val                         # return positive value as is
out = twos_comp(int(Hex,16), 32)

print("2's complement: ", out)