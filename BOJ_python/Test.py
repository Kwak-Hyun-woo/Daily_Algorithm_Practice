n, m, cab_num = map(int, input().split())
graph = []
for i in range(cab_num):
    graph.append(tuple(map(int, input().split())))

print(graph)