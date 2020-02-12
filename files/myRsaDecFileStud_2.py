#!/usr/bin/env python3
#ST2504 - ACG Practical - myRsaDecFileStud_2.py
import sys, traceback
 
from Cryptodome.Cipher import PKCS1_OAEP, PKCS1_v1_5  
from Cryptodome.PublicKey import RSA
# RKCS1_OAEP cipher is based on RSA - it is described in RFC8017
# It is a asymmetric cipher.
# Encryption requires the public key of the key pair
# Decription requires the private key of the key pair
# main program starts here
header="""A Simple Program using RSA to decrypt an encrypted text file with the size larger than key size.

Using a RSA private key only.
""" 
RSA_OVERHEAD = 66 # assume there is a overhead of 66 bytes per RSA encrypted block. when using OAEP with sha256
fn="encrypted.dat"  # default encrypted file name
if len(sys.argv) == 2:
    fn=sys.argv[1]
try:
    print(header)
    pri_key_content=open("private.pem","r").read()
    pri_key=RSA.import_key(pri_key_content)
    print("Done importing the private key") 
    print(f"Private Key:\n{pri_key_content}") 
    keysize=pri_key.size_in_bytes()
    print(f"keysize: {keysize}")
    print("Decrypting the file content with the private key")
    data=open(fn,"rb").read()
    print(f"data chunk size; {len(data)}")
    # can use either PKCS1_V1_5 or PKCS1_OAEP cipher (different in padding scheme)
    # recommend to use PKCS1_OAEP instead of PKCS1_V1_5 to avoid chosen_cipher_text_attack
    #cipher = PKCS1_v1_5.new(pub_key)
    cipher = PKCS1_OAEP.new(pri_key)
    if len(data) > keysize:   # encrypted file will be in the mulitples of the keysize.
        # need to encrypt the data in mulitple blocks
        plain_text = b""
        while len(data) > 0:
            block = data[:keysize]
            data=data[keysize:]
            plain_text = plain_text+cipher.decrypt(block)
    else:
        plain_text = cipher.decrypt(data)
        # now save the encrypted file
    out_bytes=open("plain.dat","wb").write(plain_text)
    print(f"Total of {out_bytes} bytes written to plain.dat")
except:
    print("Opps")
    traceback.print_exc(file=sys.stdout)
 