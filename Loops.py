variable = input ()
for x in variable:
    print (x)

fruits = ["apple","banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
print (x)

for x in "Nazrul":
    print (x)

for x in range (20,41,2):
    print (x)

for x in "Nazrul":
    print (x)
    if x== "z":
        break

for x in "Nazrul":
    if x== "z":
        break
    print (x)

for x in range (0,100,5):
    if x== 80:
        break
    print (x)

for num in range (20,100,2): 
    if num == 81:
        break
    print (num)

    n = 0

for x in "Nazrul":
    print (x)
    if x== "z":
        break


for i in range(20, 100, 2):
    break
    print(i)

for x in range(0,101,10):
    if x > 10 and x <100:
        continue
    print (x)


for x in range (11):
    print (x)

num = int(input())
for x in range (num):
    print (x)
if x == num - 1:
    print ("Its done")


num = int(input())
for x in range (num):
    print (x)
else:
    print ("Its done")

num = int(input())
for x in range (num):
    print (x)
else:
    print (x+1)
 
for x in ("ABCEFGHIJKLMNOPQRSTUVWXYZ"):
    for y in range (1,11):
        print (y,x)


for x in range(0,101,10):
    if x > 10 and x <100:
        continue
    print (x)


i = 0
while i < 7:
    print (i)

i = 0
while i < 7:
    i = i + 1
    print (i)



i = 0
while i < 7:
    i = i + 1
    print (i)



i = 0
while i < 7:
    print (i)
    if i == 4:
        break
    i = i + 1


i = 0
while i < 7:
    i = i + 1
    if i == 4:
        continue
    print (i)