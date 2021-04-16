#!bin/python3/
f = open('test.txt', 'w')
a = 'Abraсadabra'
for i in reversed(range(0,len(a),2)):
    print(end='')
    print(f.write(a[i]))
