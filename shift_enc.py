plain  = input("Type the plain text : ")
key = input("Type the key in the RANGE [1-25] : ")
plain_li = list(plain)
print("The Cipher text is : ", end="")

for i in plain_li:
    if i == " ":
        print(" ", end="")
    else:
        if 96 < ord(i) < 123:
            plain_value = ord(i)-96

            if plain_value+int(key) == 26:
                k = 26
            else:
                k = (plain_value + int(key))%26
            print(chr(k+96), end="")
        elif 64< ord(i) < 91:
            plain_value = ord(i)-64

            if plain_value+int(key) == 26:
                k = 26
            else:
                k = (plain_value + int(key))%26
            print(chr(k+64), end="")
