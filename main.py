import random 
#import pysha3 
import sha3
#this is for the keccak algo

full = '0x'
#generate private key
#better way is to make your own array/mapping and add it individually
hex_array = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
for i in range(64): 
    #generate random number between 0 & 15
    digit = random.randint(0,15)
    full = full + hex_array[digit]
    #convert to hex 
    #convert to string
print(full)
print(len(full))
#string_digit = bytes.fromhex(hex_digit)
#concatenate

    #print string
