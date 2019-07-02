# Documentation: https://passlib.readthedocs.io/en/stable/index.html
# Reference: https://pythonprogramming.net/password-hashing-flask-tutorial/
# pip3 install passlib
from passlib.hash import sha256_crypt

hashedPassword = sha256_crypt.hash("abc123")
# hashedPassword = sha256_crypt.using(rounds = 1000).hash("abc123")

print("Hashed and Salted Password:", hashedPassword, "\n")

while True:
    password = input("Enter your password: ")
    
    if sha256_crypt.verify(password, hashedPassword):
        print("That is your password. Welcome!")
        break
    else:
        print("That's not your password... please try again. \n")
