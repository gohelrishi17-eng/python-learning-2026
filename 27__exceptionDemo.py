print("start code")
try:
    a=int(input("enter A:"))
    b=int(input("enter B:"))
    c=a/b
    print("division : ",c)
except ZeroDivisionError as e:
    print("exeception caught")
except ValueError as e:
    print("exception caught")
finally:
    print("finally block called")
print("end code")



