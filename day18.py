# 9장 응용예제 2
# 가장 효율적인 해저 케이블망 구성하기

class graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g):
    global store_array
    print(' ', end='')
    for v in range(g.SIZE):
        print(store_array[v], end=' ')
    print()
    for row in range(g.SIZE):
        print(store_array[row], end=' ')
        for col in range(g.SIZE):
            print(g.graph[row][col], end='  ')
        print()
    print()


def findVertex(g, findVtx):
    stack = []
    visitedAry = []  # 방문한 노드

    current = 0  # 시작 정점
    stack.append(current)
    visitedAry.append(current)

    while len(stack) != 0:
        next = None
        for vertex in range(gSIZE):
            if g.graph[current][vertex] != 0:
                if vertex in visitedAry:
                    pass
                else:
                    next = vertex
                    break

        if next != None:
            current = next
            stack.append(current)
            visitedAry.append(current)

        else:
            current = stack.pop()

    if findVtx in visitedAry:
        return True
    else:
        return False


g1 = None
store_array = ['Seoul', 'New York', 'Beijing', 'Bangkok', 'London', 'Paris']
seoul, newyork, beijing, bangkok, london, paris = 0, 1, 2, 3, 4, 5

gSIZE = 6
g1 = graph(gSIZE)
g1.graph[seoul][newyork] = 80
g1.graph[seoul][beijing] = 10
g1.graph[newyork][seoul] = 80
g1.graph[newyork][beijing] = 40
g1.graph[newyork][bangkok] = 70
g1.graph[beijing][seoul] = 10
g1.graph[beijing][newyork] = 40
g1.graph[beijing][bangkok] = 50
g1.graph[bangkok][newyork] = 70
g1.graph[bangkok][beijing] = 50
g1.graph[bangkok][london] = 30
g1.graph[bangkok][paris] = 20
g1.graph[london][bangkok] = 30
g1.graph[london][paris] = 60
g1.graph[paris][bangkok] = 20
g1.graph[paris][london] = 60

stack = []
visited_array = []

print('BEFORE  ฅ^•ﻌ•^ฅ')
print_graph(g1)

current = 0
edge_array = []
for i in range(gSIZE):
    for k in range(gSIZE):
        if g1.graph[i][k] != 0:
            edge_array.append([g1.graph[i][k], i, k])

stack.append(current)
visited_array.append(current)

from operator import itemgetter

egde_array = sorted(edge_array, key=itemgetter(0), reverse=True)
new_array = []
for i in range(0, len(egde_array), 2):
    new_array.append(egde_array[i])

index = 0

while len(new_array) > gSIZE -1:
    start = new_array[index][1]
    end = new_array[index][2]
    save_way = new_array[index][0]

    startYN = findVertex(g1, start)
    endYN = findVertex(g1, start)



    if startYN and endYN:
        del(new_array[index])
    else:
        g1.graph[start][end] = save_way
        g1.graph[end][start] = save_way
        index += 1

print('AFTER ฅ^•ﻌ•^ฅ')
print_graph(g1)

