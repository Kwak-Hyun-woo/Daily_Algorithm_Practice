n, m = map(int, input().split())  # 높이, 너비
map = []
for i in range(n):
    map.append(input())

def count(map, wb):
    count = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0:
                    if map[i][j] != wb[0]:
                        count += 1
                else:
                    if map[i][j] != wb[1]:
                        count += 1
            else:
                if j % 2 == 0:
                    if map[i][j] != wb[1]:
                        count += 1
                else:
                    if map[i][j] != wb[0]:
                        count += 1
    return count
min_count = 64
for i in range(8, n + 1):
    for j in range(8, m + 1):
        map_64 = []   # 초기화
        for k in range(i - 8, i):
            map_64.append(map[k][j-8: j])

        count1 = count(map_64, ['W', 'B'])
        count2 = count(map_64, ['B','W'])
        count_64 = min(count1, count2)
        if min_count > count_64:
            min_count = count_64

print(min_count)