import random

#print(random.randint(1,100))
#print(random.coice(1,2,3,7,5))

l=[]
lucky=[]

for i in range(1,101):
    l.append(i)

for i in range(10):
    num=random.choice(l)
    lucky.append(num)


print(l)
print(lucky)
    