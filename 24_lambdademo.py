def cube(x):
    return x*x*x

print("cube:",cube(5))

y=lambda a:a*a*a
print("cube is :",y(5))

def oddeven(n):
    if n%2==0:
        print("even")
    else:
        print("odd")

oddeven(5)

z=lambda x:x%2==0
print(z(5))

ans=lambda x,y:x*y
print(ans(10,20))


        
