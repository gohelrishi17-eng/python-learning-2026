s=input("enter string:")

al=0
nm=0
sp=0
uc=0
lc=0
sc=0

for i in s:
    if i.isalpha():
        al=al+1
    elif i.isnumeric():
        nm=nm+1
    elif i.isspace():
        sp=sp+1
    else:
        sc=sc+1
    if i.isupper():
        uc=uc+1
    elif i.islower():
        lc=lc+1

print("total alfabet:",al)
print("total numeric:",nm)
print("total space:",sp)
print("total upper case:",uc)
print("total lower case:",lc)
print("total special character:",sc)

s=input("enter sting:")

