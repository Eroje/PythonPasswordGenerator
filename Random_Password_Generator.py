# Mini Project - Random Password Generator

# Import the relevant modules
from random import randint

# All uppercase password
password = ""
for i in range(10):
    i = chr(randint(65, 90)) # Python chr within 65-90 are alphabets A-Z in uppercase
    password = str(password) + i
print(password)

# Upper and lowercase passwords
password = ""
for i in range(5):
    i = chr(randint(65, 90))
    for j in range(5):
        j = chr(randint(65, 90)).lower()
    password = str(password) + i + j
print(password)

