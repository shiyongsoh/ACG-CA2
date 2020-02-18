from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import PKCS1_OAEP, AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.PublicKey import RSA
from datetime import datetime
from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA256
import hashlib
import os
now = datetime.now()
time = now.strftime("%m-%d-%Y_%H+%M+%S")

class secure:        
    # def createTunnel():
    #     self.generate()
    def __init__(self):
        print('')
    
    def encrypting(self,encType, key,data):
        iv = key
        BLOCK_SIZE = 16
        encType = encType.upper()
        try:
            data = data.encode()

        except:
            pass

        if encType == "RSA": #Asymmetric encryption
            pub_key=RSA.import_key(key)
            cipher = PKCS1_OAEP.new(pub_key)
            encrypted = cipher.encrypt(data)
            return encrypted

        elif encType == "AES": #symmetric
            iv = key
            # encodediv=iv.encode()
            cipher = hashlib.sha256()
            cipher.update(iv)
            ivHash=cipher.hexdigest()
            
            # print("ivHash",ivHash)
            ivHash = ivHash.encode()
            cipher = AES.new(key, AES.MODE_CBC,ivHash[:16])  # new AES cipher using key generated
            cipher_text_bytes = cipher.encrypt(pad(data,BLOCK_SIZE)) # encrypt data
            return cipher_text_bytes

        else:
            print('Not supported')

    def decrypting(self,encType,key,data):
        encType = encType.upper() #detects the cipher to see if its AES or RSA
        if encType == "RSA":
            pri_key=RSA.import_key(key)
            keysize=pri_key.size_in_bytes()
            cipher = PKCS1_OAEP.new(pri_key)
            plain_text = cipher.decrypt(data)
            return plain_text

        elif encType == "AES": #Symmetric decryption
            iv = key
            cipher = hashlib.sha256()
            cipher.update(iv)
            ivHash=cipher.hexdigest()
            BLOCK_SIZE = 16  #  AES data block size 128 bits (16 bytes)
            ivHash = ivHash.encode()
            decipher = AES.new(key, AES.MODE_CBC,ivHash[:16])
            decryptString = unpad(decipher.decrypt(data),BLOCK_SIZE)
            decryptString = decryptString.decode()
            #print(decipher.decrypt(data))
            return decryptString

        else:
            print('Not supported')

    def generating(self,cipherType,clientOrServer):
        clientOrServer = clientOrServer.upper()
        if clientOrServer =="CLIENT" or "SERVER":
            #Generation of RSA key
            if cipherType == "RSA":
                publicKeyName = f'keys/{clientOrServer}_public.pem'
                privateKeyName = f'keys/{clientOrServer}_private.pem'

                #try to open file and read, if no contents, go to except.
                try:
                    with open(f"{filePath}/{privateKeyName}","rb") as f:
                        privateKey = f.read()
                    with open(f"{filePath}/{publicKeyName}","rb") as f:
                        publicKey = f.read()
                    print(f"RSA key pair generated:")
                    print(f"\n{'='*100}\npublicKey:\n{publicKey}\n\n{'='*100}")
                    print(f"\nprivateKey:\n{privateKey}\n{'='*100}")

                #If cannot find public/private keys 
                except:
                    print("placeholder for RSA")
                    print("placeholder for generate")
                    print("Generating an RSA key pair...")
                    # Generate a 1024-bit or 2024-bit long RSA Key pair.
                    keypair=RSA.generate(2048)
                    # store the private key to private.pem
                    # store the public key to public.pem
                    with open(f"{filePath}/{privateKeyName}","w") as f:
                        #print(keypair.exportKey().decode() ,file=f)
                        #decode private key to a string
                        privateKey = keypair.exportKey().decode()
                        print(keypair.exportKey().decode() ,file=f)
                    f.close()
                    print("Private Key stored on to" ,privateKeyName)
                    
                    #public key exported and decoded into a string.
                    with open(f"{filePath}/{publicKeyName}","w") as f:
                        publicKey = keypair.publickey().export_key()
                        print(keypair.publickey().export_key().decode() ,file=f)
                        # print('publicKey',publicKey)
                    f.close()
                    #print("Public Key stored on to", publicKeyName)
                return publicKey,privateKey

            #Generation of AES
            elif cipherType == "AES": #Symmetric
                
                aeskey=get_random_bytes(AES.block_size)

                return aeskey
            else:
                print('Not supported')
        else:
            print("not supported")
        #return result
        #return public, private, session

    def createCert(self,privateKey, publicKey):
        # print("Verification of contents:")
        # print(publicKey)
        rsa_private_key = RSA.importKey(privateKey)
        digest = SHA256.new(publicKey)
        # print(f'Original Digest: {digest}')
        rsa_signature = pkcs1_15.new(rsa_private_key).sign(digest)
        # print(f'RSA signature {rsa_signature}')
        return rsa_signature
        
    def verifying(self,publicKey,signature):
        #print(publicKey)
        key = RSA.import_key(publicKey)
        digest = SHA256.new(publicKey)
        #print(f'Client side: {digest}')
        result = pkcs1_15.new(key).verify(digest,signature)
        if result == None:
            result = True
        return result

#secure = secure()
#public, private =secure.generating("RSA","client")
# print(type(public))
# print(type(private))
#aeskey = secure.generating('AES','client')
#encrypted = secure.encrypting("RSA",public,"server")
#decrypt = secure.decrypting("RSA",private,encrypted)
#print(f'rsa decrypt{decrypt}')
#print('----------------------------------------------------------------')
#aes = secure.encrypting("AES",aeskey,"client")
#print(secure.decrypting("AES",aeskey,aes))
# cert = secure.createCert(private,public)
# print('cert',cert)
# print(secure.verifying(public, cert))

filePath = os.path.abspath(os.path.dirname(__file__)) #d:\Onedrive\OneDrive - Singapore Polytechnic\DISM Y1 S2\Programming In Security\Assignment\server
