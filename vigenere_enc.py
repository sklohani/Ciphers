plain = input("Type the plain text in small cases : ")
key = input("Type the key in ALPHABETS : ")

plain_li = list(plain)
key_li = list(key)

key_list = []
j = 0
count = 0
for i in range(len(plain_li)):
    if plain_li[i] == " ":
        key_list.append(" ")
    else:
        key_list.append(key_li[j])

        if (count+1)%len(key_li) == 0:
            j = 0
        else:
            j += 1
        count += 1

print("The Cipher text is : ", end="")

for i in range(len(plain_li)):
    if plain_li[i] == " ":
        print(" ", end="")
    else:
        plain_value = ord(plain_li[i])-96
        key_value = ord(key_list[i])-96

        if plain_value + key_value == 26:
            k = 26
        else:
             k = (plain_value + key_value)%26
        print(chr(k+96), end="")
