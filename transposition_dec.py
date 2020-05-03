cipher = input("Type the cipher text : ")
key  = input("Type the key : ")
cipher_li = list(cipher)
key_li = list(key)

for i in range(len(key)):
    key_li[i] = int(key_li[i])

block = len(cipher_li)/len(key)

print("The plain text is : ", end="")
for i in range(int(block)):
    for j in range(len(key)):
        print(cipher_li[int(key_li[j])-1+(len(key)*i)], end ="")
