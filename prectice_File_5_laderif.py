unit=int(input("enter electricity units:"))

if unit<=100:
    bill=unit*5
elif unit<=200:
    bill=unit*7
else:
    bill=unit*10
print("electricity bill=",bill)
