from bitcoin import *
from hashlib import sha256

def SHA256(text):
  return sha256(text.encode("ascii")).hexdigest()
  
MAX_NONCE=10000000        
def mine(block_number,transaction,previous_hash,prefix_zeros):
  prefix_str='0'*prefix_zeros
  for nonce in range(MAX_NONCE):
    text= str(block_number) + transaction + previous_hash + str(nonce)
    hash = SHA256(text)
    # print(hash)
    if hash.startswith(prefix_str):
      print("Bitcoin mined with nonce value :",nonce)
      print()
      return hash
  print("Could not find a hash in the given range of upto", MAX_NONCE)

#Generate private key
my_private_key = random_key()
#display private key
print("Private Key: %sn" % my_private_key)
print()
#Generate public key
my_public_key = privtopub(my_private_key)
print("Public Key: %sn" % my_public_key)
print()
#Create a bitcoin address
my_bitcoin_address = pubtoaddr(my_public_key)
print("Bitcoin Address: %sn" % my_bitcoin_address)
print()

transactions='''
A->B->10
B->c->5
'''
difficulty = 4
import time as t
begin=t.time()
new_hash = mine(684260,transactions,"000000000000000000006bd3d6ef94d8a01de84e171d3553534783b128f06aad",difficulty)
print("Hash value : ",new_hash)
print()
time_taken=t.time()- begin
print("The mining process took ",time_taken,"seconds")
print()