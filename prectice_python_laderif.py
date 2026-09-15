rname=input("Enter student name : ")
rno=int(input("Enter roll no : "))
s1=int(input("Enter marks for subject 1 : "))
s2=int(input("Enter marks for subject 2 : "))
s3=int(input("Enter marks for subject 3 : "))

total=s1+s2+s3
per=total/3

print("student name : ",rname)
print("roll no ",rno)
print("total : ",total)
print("persentage : ",per)

if per>70:
    print("distriction")
elif per>60:
    print("first class")
elif per>50:
    print("second class")    
elif per>50:
    print("pass class")
else:
    print("Fail")

