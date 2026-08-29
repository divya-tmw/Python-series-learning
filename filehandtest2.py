fp = open("sample.txt","r")

data = fp.readlines()

for i in data:
    print(i,end="")

fp.close()