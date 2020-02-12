#!/usr/bin/env python3
#ST2504 - ACG Practical - myRsaAesEncFileStud.py
import sys, traceback
import pickle
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import PKCS1_OAEP, PKCS1_v1_5, AES  
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.PublicKey import RSA
# RKCS1_OAEP cipher is based on RSA - it is described in RFC8017
# It is a asymmetric cipher.
# Encryption requires the public key of the key pair
# Decription requires the private key of the key pair
# main program starts here


class ENC_payload:
    # A data class to store a encrypted file content.
    # The file content has been encrypted using an AES key.
    # The AES key is encrypted by a public key and stored in the enc_session_key instance attribute. 
    def __init__(self):
        self.enc_session_key=""
        self.aes_iv = ""
        self.encrypted_content=""
        
header="""A Simple Program using the combination of RSA and AES to encrypt a text file with the size larger than the key size.

Using a public key and a randomly generated AES key.
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
    # can use either PKCS1_V1_5 or PKCS1_OAEP cipher (different in padding scheme)
    # recommend to use PKCS1_OAEP instead of PKCS1_V1_5 to avoid chosen_cipher_text_attack
    # rsa_cipher = PKCS1_v1_5.new(pub_key)
    rsa_cipher = PKCS1_OAEP.new(pub_key)
    data=open(fn,"rb").read()
    print(f"data chunk size; {len(data)}")
    size_limit = pub_key.size_in_bytes() - RSA_OVERHEAD
    if len(data) > size_limit:
       # need to use AES to encrypt the file body.
       # The key being used will be encrypted by the RSA public key and store as part of the encrypted item
       aes_key = get_random_bytes(AES.block_size)
       aes_cipher = AES.new(aes_key,AES.MODE_CBC) #
       ciphertext = aes_cipher.encrypt(pad(data,AES.block_size))
       enc_payload = ENC_payload()
       enc_payload.enc_session_key = rsa_cipher.encrypt(aes_key) 
       enc_payload.aes_iv = aes_cipher.iv # retrieve the randomly generated iv value 
       enc_payload.encrypted_content=ciphertext
       encrypted=pickle.dumps(enc_payload) # serialize the enc_payload object into a byte stream.
    else:                 
        encrypted = rsa_cipher.encrypt(data)
        # now save the encrypted file
    
    out_bytes=open("encrypted.dat","wb").write(encrypted)
    print(f"Total of {out_bytes} bytes written to encrypted.dat")
except:
    print("Opps")
    traceback.print_exc(file=sys.stdout)
 