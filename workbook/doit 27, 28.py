#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 111# 27
n,m = map(int, input().split())
grid = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
move = [(0,1),(0,-1),(1,0),(-1,0)]

for i in range(n):
    num = str(input())
    for j in range(m):
        grid[i][j] = int(num[j])

def maze(x,y):
    queue = []
    queue.append((x,y))
    visited[x][y] = True
    while len(queue) != 0:
        current = queue[0]
        for asdf in range(4):
            i = current[0] + move[asdf][0]
            j = current[1] + move[asdf][1]
            if i >= 0 and j >= 0 and i < n and j < m:
                if grid[i][j] != 0 and visited[i][j] == False:
                    visited[i][j] = True
                    grid[i][j] = grid[current[0]][current[1]] + 1
                    queue.append((i,j))
        queue.pop(0)
maze(0,0)
for i in grid:
    print(i)
print(grid[n-1][m-1])


# In[9]:


#28
n = int(input())
queue = []
distance_out = []
distance_in = [[] for _ in range(n+1)]
node = [[] for _ in range(n+1)]
for i in range(n):
    a = list(map(int, input().split()))
    focus = a[0]
    for j in range(1, len(a)-1, 2):
        node[focus].append(a[j])
        distance_in[focus].append(a[j+1])

def BFS(v):
    distance = []
    queue = []
    visited = [False for _ in range(n)]
    queue.append(v)
    visited[v] = True
    d = 0
    while len(queue) != 0:
        for i in node[queue[0]]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
        d += distance_in[]
        queue.pop(0)
    distance_out.append(d)

for i in range(1, n+1):
    BFS(i)
print(max(distance))

#...결국 못 풀었따


# In[13]:


a = [0] * 2
a

