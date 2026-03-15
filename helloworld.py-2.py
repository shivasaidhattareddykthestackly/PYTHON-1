print("Hello","World","Welcome","Python")
print("Laptop","Mouse","Keyboard",sep=" | ")

name="Ravi"
age=22
city="Chennai"
print(name,age,city,sep="-")

name,age,student="Meena",20,True
print(name,age,student)

word="Python"
print(word[0])
print(word[2])
print(word[-1])

print(25+10)
print(50-20)
print(8*5)
print(100/10)
print(10%3)
print(2**4)
print(20//3)

print(3+2*5**2)

num=50
num+=25
print(num)

num=100
num/=10
print(num)

print(10>5)
print(20<15)
print(5==5)
print(10!=8)
print(7>=7)
print(6<=2)

a="apple"
b="Apple"
print(a==b)

print(10>5 and 5==5)
print(5>10 or 10==10)
print(not(5>2))

numbers=[10,20,30,40,50]
print(20 in numbers)
print(60 in numbers)
print(30 not in numbers)

a=10
b=20
a,b=b,a
print("a =",a)
print("b =",b)

a=6
b=3
print(a^b)

# 1
a = 10
b = 6
print(a & b)

# 2
x = 12
y = 5
print(x | y)

# 3
num = 8
print(~num)

# 4
a = 15
b = 9
print(a ^ b)

# 5
num = 7
print(num << 2)

# 6
num = 20
print(num >> 1)

# 7
a = int(input())
b = int(input())
print(a & b)

# 8
a = int(input())
b = int(input())
print(a ^ b)

# 9
s = "hi"
print(s * 4)

# 10
s = "python"
print(s * 3)

# 11
a = "super"
b = "man"
print(a + b)

# 12
a = "hello"
b = " "
c = "world"
print(a + b + c)

# 13
name = input()
print(name * 5)

# 14
a = input()
b = input()
print(a + b)

# 15
name = input()
print(type(name))

# 16
age = int(input())
print(age)

# 17
a = int(input())
b = int(input())
print(a + b)

# 18
m1 = float(input())
m2 = float(input())
print((m1 + m2) / 2)

# 19
a = int(input())
b = int(input())
print(3 * a * 2 + b - 2)

# 20
num = input()
print(type(num))
num = int(num)
print(type(num))

# 21
num = input()
print(num[-1])

# 22
num = int(input())
print(num % 10)

# 23
num = int(input())
print(num // 10)

# 24
num = int(input())
print((num // 10) % 10)

# 25
num = int(input())
print(num % 10)

# 26
if 10 >= 5:
    print("10 is greater than or equal to 5")

# 27
num = int(input())
if num > 50:
    print("Greater than 50")

# 28
age = int(input())
if age >= 18:
    print("Eligible")

# 29
num = int(input())
if num > 100:
    print("Greater than 100")

# 30
num = int(input())
if num >= 0:
    print("Non negative")

# 31
num = int(input())
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 32
marks = int(input())
if marks >= 35:
    print("Pass")
else:
    print("Fail")

# 33
num = int(input())
if num >= 0:
    print("Positive")
else:
    print("Negative")

# 34
num = int(input())
if num > 10:
    print("Greater than 10")
else:
    print("Not greater than 10")

# 35
age = int(input())
height = int(input())
weight = int(input())

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")

# 36
marks = int(input())
age = int(input())

if marks >= 60:
    if age >= 17:
        print("Admission Granted")
    else:
        print("Admission Denied")
else:
    print("Admission Denied")

# 37
age = int(input())
height = int(input())
weight = int(input())

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")

# 38
day = int(input())

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

# 39
num = int(input())

match num:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")

# 40
num = int(input())

match num:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")