for i in range(1,10):
    if i==5 or i==8:
        continue
    else:
        print("I:",i)

even_sum=0
odd_sum=0
for i in range(1,11):
    if i%2==0:
        even_sum=even_sum+i
    else:
        odd_sum=odd_sum+i
print("even sum:",even_sum)
print("odd sum:",odd_sum)
