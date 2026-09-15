import random

data=open("data.txt","w")
for i in range(10):
    data.write(str(random.randint(1,100))+",")
data.close()

data=open("data.txt","r")
even=open("even.txt","w")
odd=open("odd.txt","w")
prime=open("prime.txt","w")

l=data.read().split(",")[:-1]

for i in l:
    if int(i)%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")

    n=int(i)
    count=0

    for j in range(1,n+1):
        if n%j==0:
            count=count+1

    if count==2:
        prime.write(i+",")

data.close()
even.close()
odd.close()
prime.close()

print("data file content")
data=open("data.txt","r")
print(data.read())
data.close()

print("even file content")
data=open("even.txt","r")
print(data.read())
data.close()

print("odd? file content")
data=open("odd.txt","r")
print(data.read())
data.close()

print("prime file content")
data=open("prime.txt","r")
print(data.read())
data.close()
