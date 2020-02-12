#!/usr/bin/env python3
#ST2504 - ACG Practical - myDskeysStud.py
import sys,traceback
from Cryptodome.Random import get_random_bytes
from Cryptodome.Signature import pkcs1_15 
from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import SHA256
# Sample program to demonstrate the key pair export and import operations.
# main program starts here
header="A Simple Program for key pair export and import operations"
print(header)
secret_phrase = input("Type in a pass phrase please =>")
print("Generating an RSA key pair...")
rsakey_pair=RSA.generate(2048)  
print("Done generating the key pair.")
print("export the keypair to 'privatekey.der' with AES encryption in binary format")
prikey_in_der=rsakey_pair.export_key(format="DER", passphrase=secret_phrase, pkcs=8,protection="scryptAndAES128-CBC")
try:
    open("privatekey.der","wb").write(prikey_in_der)
    print("Export private key has been completed")
except:
    print("Opps! failed to export the private key")
    sys.exit(-1)
pubkey_in_pem=rsakey_pair.publickey().exportKey()
print("export the public key to 'publickey.der' with Base64 format")
try:
    open("publickey.pem","wb").write(pubkey_in_pem)
    print("Export public key has been completed")
except:
    print("Opps! failed to export the public key")
    sys.exit(-1)
# now try to import back the key pair (the private key)
print("now try to import back the key pair (the private key)")
prikey_bytes=open("privatekey.der","rb").read()
restored_keypair=RSA.import_key(prikey_bytes,passphrase=secret_phrase)
if restored_keypair == rsakey_pair:
    print("Restored the key pair successfully")
pubkey_bytes=open("publickey.pem","r").read()
restored_pubkey=RSA.import_key(pubkey_bytes)
if restored_pubkey == rsakey_pair.publickey():
    print("Restored the public key successfully")   
