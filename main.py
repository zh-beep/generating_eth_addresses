import random
import cffi 
#import pysha3 
import sha3
#this is for the keccak algo

from coincurve import PublicKey

full = ''
#generate private key
#better way is to make your own array/mapping and add it individually
hex_array = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
for i in range(64): 
    #generate random number between 0 & 15
    digit = random.randint(0,15)
    full = full + hex_array[digit]
    #convert to hex 
    #convert to string
#convert string to hexadecimal
hex_value = hex(int(full,16))
hex_bytes = bytearray.fromhex(full)
hex_char = ffi.new("char []", hex_value)
public_key = PublicKey.from_valid_secret(hex_char).format(compressed=False)[1:]
#string_digit = bytes.fromhex(hex_digit)
#concatenate

    #print string
