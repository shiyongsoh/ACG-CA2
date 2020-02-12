#!/usr/bin/env python3
#ST2504 - ACG Practical - myRsaEncFileStud_2.py
import sys, traceback
 
from Cryptodome.Cipher import PKCS1_OAEP, PKCS1_v1_5  
from Cryptodome.PublicKey import RSA
# RKCS1_OAEP cipher is based on RSA - it is described in RFC8017
# It is a asymmetric cipher.
# Encryption requires the public key of the key pair
# Decription requires the private key of the key pair
# main program starts here

header="""A Simple Program using RSA to encrypt a text file with the size larger than the key size.

Using a public key only.
""" 
RSA_OVERHEAD = 66 # assume there is a overhead of 66 bytes per RSA encrypted block. when using OAEP with sha256
fn="larger.txt"  # default text file name
if len(sys.argv) == 2:
    fn=sys.argv[1]
try:
    print(header)
    pub_key_content=open("public.pem","r").read()
    pub_key=RSA.import_key(pub_key_content)
    print("Done importing the public key") 
    print(f"Public Key:\n{pub_key_content}") 
    print(f"keysize: {pub_key.size_in_bytes()}")
    print("Encrypting the file content with the public key")
    cipher = PKCS1_OAEP.new(pub_key)
    data=open(fn,"rb").read()
    print(f"data chunk size; {len(data)}")
    size_limit = pub_key.size_in_bytes() - RSA_OVERHEAD
    if len(data) > size_limit:
        # need to encrypt the data in mulitple blocks
        encrypted = b""
        while len(data) > 0:
            block = data[:size_limit]
            data=data[size_limit:]
            encrypted = encrypted+cipher.encrypt(block)
    else:    
        # can use either PKCS1_V1_5 or PKCS1_OAEP cipher (different in padding scheme)
        # recommend to use PKCS1_OAEP instead of PKCS1_V1_5 to avoid chosen_cipher_text_attack
        #cipher = PKCS1_v1_5.new(pub_key)
        
        encrypted = cipher.encrypt(data)
        # now save the encrypted file
    
    out_bytes=open("encrypted.dat","wb").write(encrypted)
    print(f"Total of {out_bytes} bytes written to encrypted.dat")
except:
    print("Opps")
    traceback.print_exc(file=sys.stdout)
 