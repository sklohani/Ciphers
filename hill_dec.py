# Importing numpy and sympy libraries.
import numpy as np
from sympy import *

# Assuming length of key is less than length of cipher text.

cipher = input("Type the cipher text in small cases : ")
key = input("Type the key in small case Alphabets : ")
cipher_list = list(cipher)
key_list = list(key)
num_list = np.array([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])    # Assuming maximum length of key is 100.
for i in num_list:
    if i >= len(key):
        key_unit = i    # Total elements of Key Matrix.
        break

# Adding "z" as padding in key.
for i in range(int(key_unit)-len(key)):
    key_list.append('z')

size= int(np.sqrt(key_unit))   # Size of key Square Matrix.

# "block" is the number of parts of plaintext we need to divide as sub-matrix.
if len(cipher)%size == 0:
    block = int(len(cipher)/size)
else:
    block = int(len(cipher)/size) + 1

cipher_li = []
for i in range(len(cipher_list)):
    cipher_li.append(ord(cipher_list[i])-97)

key_li = []
for i in range(len(key_list)):
    key_li.append(ord(key_list[i])-97)

km = np.matrix(key_li)
key_matrix = km.reshape(size,size)

# Determinant of Key Matrix
key_det = np.linalg.det(key_matrix)
if key_det > int(key_det)+0.5:
    key_det = int(key_det)+1

# Multiplicative inverse of Key Determinant mod 26.
for i in range(1000):
    if (key_det*i)%26 == 1:
        key_mul_inv = i
        break
    else:
        key_mul_inv = -1

# Decryption.
if key_det == 0:
    print("Key-Matrix is not invertible, can not decrypt the message.")
elif(key_mul_inv == -1):
    print("Can not find Multiplicative Inverse of Determinant modulo 26 of Key-Matrix, can not decrypt the message.")
else:
    key_matrix = Matrix(key_matrix)
    key_cof = key_matrix.adjugate()
    key_cof = np.array(key_cof)
    key_cof = key_cof%26
    key_inv_matrix = (key_cof*key_mul_inv)%26
    key_inv_matrix = np.matrix(key_inv_matrix)

    print("The plane text is : ", end="")
    for i in range(block):
        cipher_temp_list = []
        for j in range(size):
            cipher_temp_list.append(cipher_li[j+(i*size)])
        cm = np.matrix(cipher_temp_list)
        cipher_matrix = cm.reshape(size,1)
        plain_matrix = key_inv_matrix*cipher_matrix
        plain_li = plain_matrix.ravel().tolist()
        for i in plain_li[0]:
            print(chr((int(i)%26)+97), end="")