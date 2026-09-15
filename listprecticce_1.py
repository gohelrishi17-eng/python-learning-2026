1fruits = ["Apple","banana","mango","Orange"]
print(fruits)

data=["rishi",20,58,12,True]
print(data)

print(fruits[0])

#list index possitive

print(fruits[2])

#nagative index

print(fruits[-1])

#len=list ki lenght

fruits = ["Apple","banana","mango","Orange"]
print(len(fruits))

#list ka item change karna ho!!

fruits = ["Apple","banana","mango"]
fruits[1]="orange"
print(fruits)

#append=list ke end me new item add karna!!

fruits = ["Apple","banana","mango"]
fruits.append("Orange")
print(fruits)

#insert=kisi perticuler position par item add karna!!

fruits = ["Apple","Banana","Mango"]
fruits.insert(1,"Orange")
print(fruits)

#remove=list mese value ko remove karna!!

fruits=["apple","banana","mango"]
fruits.remove("banana")
print(fruits)

#pop=index ke basis par item remove kaarna!!

fruits=["apple","banana","mango"]
fruits.pop()
print(fruits)

#clear=list ke sare item ko remove karna!!

fruits=["apple","banana","mango"]
fruits.clear()
print(fruits)

#del= perticuler item delet karna!!

fruits=["apple","banana","mango"]
del fruits[1]
print(fruits)

#sort= list ko ascending order me arenge karna!!

numbers = [5,2,8,1,3]
numbers.sort()
print(numbers)

#reverse=list ka order reverce karne ke liye!!

numbers = [1,2,3,4,5]
numbers.reverse()
print(numbers)

#count=koi value list me kitni bar he  pata karne ke liye!!

numbers = [10,20,10,30,10]
print(numbers.count(10))

#index=kisi value a index pata karne ke liye!!

fruits=["apple","banana","mango",]
print(fruits.index("mango"))

#in=check karna ho koi item list me he ki nai!!

fruits=["apple","banana","mango"]
print("apple" in fruits)
print("Orange" in fruits)

#list ke sath for loop

fruits=["apple","banana","mango"]
for i in fruits:
    print(i)

#list+input=user se multiple value lena ho!!

names = []
for i in range(3):
    name = input("Enter name: ")
    names.append(name)
print(names)






      
