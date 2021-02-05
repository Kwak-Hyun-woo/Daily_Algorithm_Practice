n = int(input())

result = n
for i in range(n):
    check = input()
    checked_alphabets = []
    prev = check[0]

    for j in check:
        if prev != j and j in checked_alphabets:
            result -= 1
            break
        if j not in checked_alphabets:
            checked_alphabets.append(j)
        prev = j
print(result)