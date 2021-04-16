b=0
for i in 758, 483, 893, 393, 293, 292, 292, 485, 828, 182:
    b+=i
    pass
print(b)

b=0
for i in range(0, 9):
    b+=i
    pass
print(b)

n=int(input())
for i in range (1, n+1):
    for j in range (1, i + 1):
        print (j, end='')
    print()

    n=9
    b=9
    for i in range(1, n+1):
        print ((b-i)*' ', end="")
        for j in range (1, i+1):
           print(j, end="")
        print()
    for i in reversed(range (1, n+1)):
        print ((b)*' ', end=" ")
        for j in reversed(range (1,i+1)):
            print (j, end='')
        print()
#Ромбик
n=5
b=5
for i in range(1, n+1):
    print ((b-i)*' ', end=" ")
    for j in range (1, i+1):
       print(j, end=" ")
    print()
for i in reversed(range (1, n+1)):
    print ((b-i)*' ', end=" ")
    for j in (range (1,i+1)):
        print (j, end=' ')
    print()
