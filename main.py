import random 
#import pysha3 
import sha3
#this is for the keccak algo

full = ''
#generate private key
for i in range(10): 
    #generate random number between 0 & 15
    digit = random.randint(0,15)
    #convert to hex 
    hex_digit = hex(digit)
    full = full + hex_digit
    #convert to string
print(full)
#string_digit = bytes.fromhex(hex_digit)
#concatenate

    #print string
