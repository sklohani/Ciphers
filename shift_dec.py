cipher = input("Type the cipher text : ")
key = input("Type the key : ")
cipher_li = list(cipher)
print("The Plain text is : ", end="")

for i in cipher_li:
    if i == " ":
        print(" ", end="")
    else:
        if 96 < ord(i) < 123:
            cipher_value = ord(i)-96

            if cipher_value-int(key) == 26:
                k = 26
            else:
                k = (cipher_value - int(key))%26
            print(chr(k+96), end="")
        elif 64< ord(i) < 91:
            cipher_value = ord(i)-64

            if cipher_value-int(key) == 26:
                k = 26
            else:
                k = (cipher_value - int(key))%26
            print(chr(k+64), end="")


