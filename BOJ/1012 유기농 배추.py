test_num = int(input())

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if (x, y) in graph:
        graph.remove((x, y))

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

for k in range(test_num):
    n, m, cab_num = map(int, input().split())
    graph = []
    for i in range(cab_num):
        graph.append(tuple(map(int, input().split())))
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
    print(result)