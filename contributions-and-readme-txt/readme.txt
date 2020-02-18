Owner will start a server.
User will start the client.

Client user authentication:
Username1: bryan
Password1: bryan

Username2: bye
Password2: bryan

Process:

1. Server starts by generating an RSA public and private key.
2. Client starts by sending a query to the server.
3. Client will receive a public and digital signature of the
public key for verification.
4. Client acknowledges the public key and starts to generate
a symmetric key.
5. Client encrypts the symmetric key using the server's
public key and sends it over to the server.
6. Server receives clients' symmetric key and decrypts the
key.
7. Secure channel has been established.
8. Server sends encrypted response back to the client.
9. Client decrypts menu with the symmetric key.
10. Client encrypts with symmetric key and sends back
day_end file over to the server.
11. Server receives the day_end file and decrypts the file
with a symmetric key.
12.Client ends connection.

