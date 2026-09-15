#1. Tuple — Deep Explanation
Tuple kya hota hai?

Tuple bhi List ki tarah multiple values ek variable me store karne ke liye use hota hai.

List:

a = [10,20,30,40]

Tuple:

a = (10,20,30,40)

Dono me values multiple hain.

Lekin main difference:

List → change kar sakte ho
a = [10,20,30]
a[0] = 100
print(a)

Output:

[100, 20, 30]
Tuple → change nahi kar sakte
a = (10,20,30)
a[0] = 100

Ye error dega.

👉 Isko yaad rakho:

List = mutable → change kar sakte hain
Tuple = immutable → change nahi kar sakte

🟢 Sir question de sakte hain
Q1. Tuple create karo
a = (10,20,30,40,50)
print(a)

Output:

(10, 20, 30, 40, 50)
Q2. Tuple ka first element print karo
a = (10,20,30,40,50)

print(a[0])

Output:

10

Kyun?

Python me indexing 0 se start hoti hai.

Value:     10   20   30   40   50
Index:      0    1    2    3    4
🟢 2. Set

Ye bhi next topic ho sakta hai.

Set ka main kaam hai unique values rakhna.

a = {10,20,20,30,30,40}

print(a)

Output roughly:

{10,20,30,40}

Notice karo:

20 do baar tha, lekin output me ek hi baar aaya.

Sir pooch sakte hain:

Q: Set ki khasiyat kya hai?

Answer:

Set unique values store karta hai aur duplicate values ko automatically remove karta hai.

🟢 3. Dictionary ⭐

Ye bahut important hai.

Dictionary me data key : value ke form me hota hai.

Example:

student = {
    "name": "Rishi",
    "age": 20,
    "marks": 75
}

Yahan:

"name"  → key
"Rishi" → value

"age"   → key
20      → value

Agar naam chahiye:

print(student["name"])

Output:

Rishi

Marks:

print(student["marks"])

Output:

75
Sir bol sakte hain:

"Dictionary me student ka naam Rishi, age 20 aur marks 75 store karo aur marks print karo."

Tum likhoge:

student = {
    "name": "Rishi",
    "age": 20,
    "marks": 75
}

print(student["marks"])
🟢 4. Function ⭐⭐⭐

Ye bahut important topic hai.

Maan lo tumhe baar-baar addition karna hai.

Without function:

a = 10
b = 20
print(a+b)

a = 50
b = 60
print(a+b)

Same logic baar-baar likhna padega.

Function se:

def add(a,b):
    return a+b

Ab use karo:

print(add(10,20))
print(add(50,60))

Output:

30
110
Isko line-by-line samjho:
def add(a,b):

def = function banane ke liye.

add = function ka naam.

a,b = parameters.

return a+b

Addition ka result wapas bhej raha hai.

add(10,20)

Yahan 10 → a

aur 20 → b

To:

10 + 20
= 30
🔥 Sir Function me aisa question de sakte hain
Question:

"Write a function to find square of a number."

Tum:

def square(n):
    return n*n

print(square(5))

Output:

25

Agar sir bole:

"Write a function to find whether number is even or odd."

Tum:

def check(n):
    if n%2 == 0:
        print("Even")
    else:
        print("Odd")

check(10)

Output:

Even
🟢 5. Uske baad Data Science wali Python

Yahan se tumhara actual Data Science connection strong hona start hoga.

NumPy

Example:

import numpy as np

a = np.array([10,20,30,40])

print(a)

Yahan array important concept hai.

Pandas ⭐⭐⭐

Ye tumhare course ka bahut important part hoga.

Example:

import pandas as pd

data = {
    "Name": ["Rishi", "Rahul", "Amit"],
    "Marks": [75, 80, 65]
}

df = pd.DataFrame(data)

print(df)

Output table jaisa dikhega:

    Name  Marks
0   Rishi   75
1   Rahul   80
2   Amit    65

Phir sir questions de sakte hain:

Column kaise select kare?
Row kaise select kare?
Data filter kaise kare?
CSV file kaise read kare?
Average kaise nikale?
Missing data kaise handle kare?
🎯 Tumhe abhi kya karna chahiye?

Abhi NumPy/Pandas pe jump mat karo.

Tumhara sequence:

LIST
 ↓
TUPLE
 ↓
SET
 ↓
DICTIONARY
 ↓
FUNCTION
 ↓
EXCEPTION HANDLING
 ↓
FILE HANDLING
 ↓
NUMPY
 ↓
PANDAS
 ↓
MATPLOTLIB
 ↓
DATA ANALYSIS

Aur main tumhe sirf theory nahi padhाऊँगा.

Har topic me hum ye karenge:

Concept → Example → Har line ka meaning → Output → Sir ka possible question → Tumhara practice question → Tumhara answer check

Isse class me sir achanak code/question denge to tum logic samajh ke answer kar paoge, ratta nahi.
