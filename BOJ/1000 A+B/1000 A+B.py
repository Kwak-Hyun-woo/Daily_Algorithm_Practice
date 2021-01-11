a = input()
a1 = a.split(' ')
for i in range(len(a1)):
    a1[i].strip()
    a1[i] = int(a1[i])

print(a1[0] + a1[1])