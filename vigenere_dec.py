cipher = input("Type the cipher text : ")
key = input("Type the key : ")

cipher_li = list(cipher)
key_li = list(key)

key_list = []
j = 0
count = 0
for i in range(len(cipher_li)):
    if cipher_li[i] == " ":
        key_list.append(" ")
    else:
        key_list.append(key_li[j])

        if (count+1)%len(key_li) == 0:
            j = 0
        else:
            j += 1
        count += 1

print("The plain text is : ", end="")

for i in range(len(cipher_li)):
    if cipher_li[i] == " ":
        print(" ", end="")
    else:
        cipher_value = ord(cipher_li[i])-96
        key_value = ord(key_list[i])-96

        if cipher_value - key_value == 26:
            k = 26
        else:
             k = (cipher_value - key_value)%26
        print(chr(k+96), end="")
