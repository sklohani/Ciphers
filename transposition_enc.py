plain = input("Type the plain text without spaces : ")
key  = input("Type the key : ")
plain_li = list(plain)
key_li = list(key)

for i in range(len(key)):
    key_li[i] = int(key_li[i])

var = len(key)-(len(plain)%len(key))
for i in range(var):
    plain_li.append('z')
block = len(plain_li)/len(key)

print("The cipher text is : ", end="")
for i in range(int(block)):
    for j in range(len(key)):
        print(plain_li[key_li.index(j+1)+(len(key)*i)], end ="")
