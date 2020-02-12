#!/usr/bin/env python3
#ST2504 - ACG Practical - myRsaKeysToFiles.py
from Cryptodome.Random import get_random_bytes
from Cryptodome.PublicKey import RSA
# Generate a RSA key pair.
# Store the private key and public key to two seperate files. 
# main program starts here
 
print("Generating an RSA key pair...")
# Generate a 1024-bit or 2024-bit long RSA Key pair.
keypair=RSA.generate(2048)
# store the private key to private.pem
# store the public key to public.pem
with open("private.pem","w") as f:
    print(keypair.exportKey().decode() ,file=f)
f.close()
print("Private Key stored on to  'private.pem'")
with open("public.pem","w") as f:
    print(keypair.publickey().exportKey().decode() ,file=f)
f.close()
print("Public Key stored on to  'public.pem'")
