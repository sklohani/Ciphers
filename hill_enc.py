# Importing numpy library.
from numpy import *

# Assuming length of key is less than length of plaintext.

plain = input("Type the plain text in small cases : ")
key = input("Type the key in small cases Alphabets : ")
plain_list = list(plain)
key_list = list(key)
num_list = array([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])    # Assuming maximum length of key is 100.

for i in num_list:
    if i >= len(key):
        key_unit = i    # Total elements of Key Matrix.
        break

# Adding "z" as padding in key.
for i in range(int(key_unit)-len(key)):
    key_list.append('z')

size= int(sqrt(key_unit))   # Size of key Square Matrix.

# "block" is the number of parts of plaintext we need to divide as sub-matrix.
if len(plain)%size == 0:
    block = int(len(plain)/size)
else:
    block = int(len(plain)/size) + 1

# Adding "z" as padding in plaintext.
for i in range((size*block)-len(plain)):
    plain_list.append('z')

plain_li = []
for i in range(len(plain_list)):
    plain_li.append(ord(plain_list[i])-97)

key_li = []
for i in range(len(key_list)):
    key_li.append(ord(key_list[i])-97)

km = matrix(key_li)
key_matrix = km.reshape(size,size)

# Determinant of Key Matrix.
key_det = linalg.det(key_matrix)
if key_det > int(key_det)+0.5:
    key_det = int(key_det)+1

# Multiplicative inverse of Key Determinant mod 26.
for i in range(100000):
    if (key_det*i)%26 == 1:
        key_mul_inv = i
        break
    else:
        key_mul_inv = -1

# Encryption
def encryption():
    print("The cipher text is : ", end="")
    for i in range(block):
        plain_temp_list = []
        for j in range(size):
            plain_temp_list.append(plain_li[j+(i*size)])
        pm = matrix(plain_temp_list)
        plain_matrix = pm.reshape(size,1)
        cipher_matrix = key_matrix*plain_matrix
        cipher_li = cipher_matrix.ravel().tolist()
        for i in cipher_li[0]:
            print(chr((int(i)%26)+97), end="")

if key_det == 0:
    print("Key-Matrix is not invertible, can encrypt the message but can not decrypt the encrypted message with this key.")
    choice = input("Still want to Encrypt the message, TYPE '1' : ")
    if choice == "1":
        encryption()
elif(key_mul_inv == -1):
    print("Can not find Multiplicative Inverse of Determinant modulo 26 of Key-Matrix, can encrypt the message but can not decrypt the encrypted message with this key.")
    choice = input("Still want to Encrypt the message, TYPE '1' : ")
    if choice == "1":
        encryption()
else:
    encryption()
    