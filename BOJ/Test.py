a = input()
count = 0
for i in a:
    if count % 10 == 0:
        print()
    print(i, end = '')
    count += 1
