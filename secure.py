from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import PKCS1_OAEP, AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.PublicKey import RSA
from datetime import datetime
from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA256
now = datetime.now()
time = now.strftime("%m-%d-%Y_%H+%M+%S")

class secure:        
    # def createTunnel():
    #     self.generate()
    def __init__(self):
        print('')

    def encrypting(self,encType, key,data):
        BLOCK_SIZE = 16
        encType = encType.upper()
        try:
            data = data.encode()
        except:
            pass
        print('plaintext:',data)
        print('-------------')
        if encType == "RSA": #Asymmetric
            pub_key=RSA.import_key(key)
            cipher = PKCS1_OAEP.new(pub_key)
            #print('cipher',cipher)
            encrypted = cipher.encrypt(data)
            #print('encrypted',encrypted)
            #encrypted = encrypted.decode()
            #sprint(encrypted)
            return encrypted
        elif encType == "AES": #symmetric
            
            print('done importing')
            cipher = AES.new(key, AES.MODE_ECB)  # new AES cipher using key generated
            cipher_text_bytes = cipher.encrypt(pad(data,BLOCK_SIZE)) # encrypt data
            #print('encrypted data',cipher_text_bytes)
            return cipher_text_bytes
        else:
            print('Not supported')
    def decrypting(self,encType,key,data):
        encType = encType.upper()
        print(encType)
        print('secure class decrypt data',data)
        if encType == "RSA":
            print("placeholder for RSA")
            pri_key=RSA.import_key(key)
            keysize=pri_key.size_in_bytes()
            cipher = PKCS1_OAEP.new(pri_key)
            print('decrypting',data)
            plain_text = cipher.decrypt(data)
            print('secure class decrypt plain_text',plain_text)
            return plain_text
        elif encType == "AES": #Symmetric
            #print('data',data)
            BLOCK_SIZE = 16  #  AES data block size 128 bits (16 bytes)
            decipher = AES.new(key, AES.MODE_ECB)
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
                try:
                    with open(privateKeyName,"rb") as f:
                        privateKey = f.read()
                    with open(publicKeyName,"rb") as f:
                        publicKey = f.read()
                    print("publicKey",publicKey)
                    print("privateKey",privateKey)
                except:
                    print("placeholder for RSA")
                    print("placeholder for generate")
                    print("Generating an RSA key pair...")
                    # Generate a 1024-bit or 2024-bit long RSA Key pair.
                    keypair=RSA.generate(2048)
                    # store the private key to private.pem
                    # store the public key to public.pem
                    with open(privateKeyName,"w") as f:
                        #print(keypair.exportKey().decode() ,file=f)
                        privateKey = keypair.exportKey().decode()
                        print(keypair.exportKey().decode() ,file=f)
                    f.close()
                    print("Private Key stored on to" ,privateKeyName)
                    
                    with open(publicKeyName,"w") as f:
                        publicKey = keypair.publickey().export_key()
                        print(keypair.publickey().export_key().decode() ,file=f)
                        print('publicKey',publicKey)
                    f.close()
                    #print("Public Key stored on to", publicKeyName)
                return publicKey,privateKey
            #Generation of AES
            elif cipherType == "AES": #Symmetric
                aeskey=get_random_bytes(AES.block_size)
                print("AES Key:")
                for b in aeskey:
                    print("{0:02x}".format(b),end="")
                print("\n")
                return aeskey
            else:
                print('Not supported')
        else:
            print("not supported")
        #return result
        #return public, private, session
    def createCert(self,privateKey, publicKey):
        print("placeholder for verification")
        print(publicKey)
        rsa_private_key = RSA.importKey(privateKey)
        digest = SHA256.new(publicKey)
        print(f'Original Digest: {digest}')
        rsa_signature = pkcs1_15.new(rsa_private_key).sign(digest)
        print(f'RSA signature {rsa_signature}')
        return rsa_signature
    def verifying(self,publicKey,signature):
        print(publicKey)
        key = RSA.import_key(publicKey)
        digest = SHA256.new(publicKey)
        print(f'Client side: {digest}')
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