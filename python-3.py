# 1
for i in range(1,51):
 print(i)

# 2
for i in range(1,101):
  if i%2==0:
   print(i)

# 3
for i in range(1,101):
 if i%2!=0:
  print(i)

# 4
for i in range(1,11):
 print(7*i)

# 5
s=0
for i in range(1,101):
 s = s + i
print(s)

# 6
for i in range(50,0,-1):
 print(i)

# 7
c =0
for i in range(1,101):
 if i%3==0:
  c+=1
print(c)

# 8
for i in range(1,11):
 print(i*i)

# 9
for i in range(1,11):
 print(i**3)

# 10
n=int(input())
for i in range(1,n+1):
 print(i)

# 11
i=1
while i<=20:
 print(i)
 i+=1

# 12
n=int(input())
f=1
i=1
while i<=n:
 f = f*i
 i+=1
print(f)

# 13
n=int(input())
rev=0
while n>0:
 d=n%10
 rev=rev*10+d
 n//=10
print(rev)

# 14
n=int(input())
c=0
while n>0:
 n//=10
 c+=1
print(c)

# 15
while True:
 a=input()
 if a=="stop":
  break

# 16
for i in range(1,5):
 for j in range(i):
  print("*",end="")
 print()

# 17
for i in range(1,5):
 for j in range(1,i+1):
  print(j,end="")
 print()

# 18
for i in range(1,6):
 for j in range(1,11):
  print(i*j,end=" ")
 print()

# 19
for i in range(3):
 for j in ["A","B","C"]:
  print(j,end=" ")
 print()

# 20
num=1
for i in range(3):
 for j in range(3):
  print(num,end=" ")
  num+=1
 print()

# 21
s=input()
c=0
for i in s:
 c+=1
print(c)

# 22
s=input()
v="aeiouAEIOU"
c=0
for i in s:
 if i in v:
  c+=1
print(c)

# 23
s=input()
v="aeiouAEIOU"
c=0
for i in s:
 if i.isalpha() and i not in v:
  c+=1
print(c)

# 24
s=input()
r=""
for i in s:
 r=i+r
print(r)

# 25
s=input()
if s==s[::-1]:
 print("Palindrome")
else:
 print("Not Palindrome")

# 26
s=input()
print(s[:5])

# 27
s=input()
print(s[-3:])

# 28
s=input()
print(s[::-1])

# 29
s=input()
print(s[::2])

# 30
s=input()
print(s[1:-1])

# 31
l=[10,20,30,40,50]
s=0
for i in l:
 s+=i
print(s)

# 32
l=[5,8,2,10,3]
m=l[0]
for i in l:
 if i>m:
  m=i
print(m)

# 33
l=[5,8,2,10,3]
m=l[0]
for i in l:
 if i<m:
  m=i
print(m)

# 34
l=[1,2,3,4,5]
c=0
for i in l:
 c+=1
print(c)

# 35
l=[2,4,6,8,10]
x=int(input())
if x in l:
 print("Exists")
else:
 print("Not Exists")

# 36
l=[]
l.append(10)
l.append(20)
l.append(30)
print(l)

# 37
l=[1,2,4,5]
l.insert(2,3)
print(l)

# 38
l=[10,20,30,40]
l.remove(30)
print(l)

# 39
l=[1,2,3,4,5]
r=[]
for i in l:
 r=[i]+r
print(r)

# 40
l=[5,3,1,4,2]
for i in range(len(l)):
 for j in range(i+1,len(l)):
  if l[i] > l[j]:
   l[i],l[j] = l[j],l[i]
print(l)