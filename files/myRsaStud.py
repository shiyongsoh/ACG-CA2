#!/usr/bin/env python3
#ST2504 - ACG Practical - myRsaStud.py
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import PKCS1_OAEP, AES
from Cryptodome.PublicKey import RSA
# RKCS1_OAEP cipher is based on RSA - it is described in RFC8017
# It is a asymmetric cipher.
# Encryption requires the public key of the key pair
# Decription requires the private key of the key pair
# main program starts here
header="""A Simple Program using RSA to encrypt and decrypt a single AES symmetric key.

Generating a symmetric (AES) key...
""" 
print(header)
aeskey=get_random_bytes(AES.block_size)
print("AES Key:")
for b in aeskey:
    print("{0:02x}".format(b),end="")
print("\n")
print("Generating an RSA key pair...")
rsakey_pair=RSA.generate(2048)  
print("Done generating the key pair.")
print("Encrypting the AES Key with the public key of the RSA key pair")
cipher = PKCS1_OAEP.new(rsakey_pair.publickey())
encrypted = cipher.encrypt(aeskey)
print("Encrypted Key:")
for b in encrypted:
    print("{0:02x}".format(b),end="")
print("\n")
print("Decrypting the Encrypted Key with the private key of the RSA key pair")
cipher = PKCS1_OAEP.new(rsakey_pair)
decrypted = cipher.decrypt(encrypted)
print("Decrypted Key:")
for b in decrypted:
    print("{0:02x}".format(b),end="")
print("\n")
