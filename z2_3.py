f=open('test.txt')
n=5
for i in range (1, n+1):
    for j in range (1, i + 1):
        for j in range (1, - 1):
            print(f.write(j, end=''))
    print()
