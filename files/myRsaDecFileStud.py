#!/usr/bin/env python3
#ST2504 - ACG Practical - myRsaDecFileStud.py
import sys, traceback
 
from Cryptodome.Cipher import PKCS1_OAEP, PKCS1_v1_5  
from Cryptodome.PublicKey import RSA
# RKCS1_OAEP cipher is based on RSA - it is described in RFC8017
# It is a asymmetric cipher.
# Encryption requires the public key of the key pair
# Decription requires the private key of the key pair
# main program starts here
header="""A Simple Program using RSA to decrypt an encrypted text file.

Using a RSA private key.
""" 
fn="encrypted.dat"  # default encrypted file name
if len(sys.argv) == 2:
    fn=sys.argv[1]
try:
    print(header)
    pri_key_content=open("private.pem","r").read()
    pri_key=RSA.import_key(pri_key_content)
    print("Done importing the private key") 
    print(f"Private Key:\n{pri_key_content}") 
    print(f"keysize: {pri_key.size_in_bytes()}")
    print("Decrypting the file content with the private key")
    data=open(fn,"rb").read()
    print(f"data chunk size; {len(data)}")
    # can use either PKCS1_V1_5 or PKCS1_OAEP cipher (different in padding scheme)
    # recommend to use PKCS1_OAEP instead of PKCS1_V1_5 to avoid chosen_cipher_text_attack
    #cipher = PKCS1_v1_5.new(pub_key)
    cipher = PKCS1_OAEP.new(pri_key)
    plain_text = cipher.decrypt(data)
    # now save the encrypted file
    out_bytes=open("plain.dat","wb").write(plain_text)
    print(f"Total of {out_bytes} bytes written to plain.dat")
except:
    print("Opps")
    traceback.print_exc(file=sys.stdout)
 