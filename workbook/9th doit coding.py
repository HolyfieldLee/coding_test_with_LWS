#!/usr/bin/env python
# coding: utf-8

# In[8]:


#26번
n,m,s = map(int, input().split())
A = [[] for _ in range(n+1)]
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)
queue = []
dfs = []
bfs = []

for _ in range(m):
    x,y = map(int, input().split())
    A[x].append(y)
    A[y].append(x)

def DFS(v):
    visited_dfs[v] = True
    dfs.append(v)
    for i in A[v]:
        if not visited_dfs[i]:
            DFS(i)

def BFS(v):
    bfs.append(v)
    queue.append(v)
    visited_bfs[v] = True
    while len(queue) != 0:
        for i in A[queue[0]]:
            if visited_bfs[i] == False:
                queue.append(i)
                bfs.append(i)
                visited_bfs[i] = True
        queue.pop(0)

DFS(s)
BFS(s)
print(dfs)
print(bfs)

