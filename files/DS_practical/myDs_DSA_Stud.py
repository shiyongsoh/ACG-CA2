#!/usr/bin/env python3
#ST2504 - ACG Practical - myDs_DSA_Stud.py
# Sample program to demonstrate the DSA key pair generation, signing and verifying operations. 
import sys, traceback
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa

# main program starts here
private_key = dsa.generate_private_key(
    key_size=1024,
    backend=default_backend()
)
data = b"this is some data I'd like to sign"
signature = private_key.sign(data,hashes.SHA256())
# Verify a signature against the data
public_key = private_key.public_key()
try:
    print("Verify with the orignal data")
    public_key.verify(
        signature,
        data,
        hashes.SHA256()
    )
    print("Verification is okay for the original data")
    print("Verify with the altered data")
    public_key.verify(
        signature,
        data+b"extended attack",
        hashes.SHA256()
    )
    print("Verification is okay for the altered data")
except:
    print("verification has been failed")
