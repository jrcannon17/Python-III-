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
mod = len(Hex) % 2
print('mod is', mod)
#hex1 = len(Hex)
print("length is", len(Hex),"\nValue has", len(Hex)/2, "Databytes")
print("Decimal Value is", dec)
binary_number = int("{0:08b}".format(dec))
n = 2
count = -1

for i in range(0,len(Hex), n):
	count +=1
	print('Databyte',count,':',Hex[i:i+n], \
        '\t Decimal Value: ', str(int(Hex[i:i+n], base=16)), \
	    '\t Binary Value: ', str(bin(int(Hex[i:i+n], base=16)))[2:])


print("Binary: ", binary_number)

flipped_binary_number = ~ binary_number

flipped_binary_number = flipped_binary_number + 1

str_twos_complement = str(flipped_binary_number)

twos_complement = int(str_twos_complement, 2)

print("2's complement is: ", twos_complement)


'''
while True:
    x = input("ERD: ")
    y = input ("appliance: ")

    if x.lower() == "q":
        break
    else:
        if y == "espresso":
            print("espresso")
        else:
            returnAllTheThings(x)
'''
