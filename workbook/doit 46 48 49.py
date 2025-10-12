#!/usr/bin/env python
# coding: utf-8

# In[11]:


# 46
n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
distance = [0]*(n+1)
visited = [False]*(n+1)
def BFS(v):
    queue = [v]
    while len(queue) > 0:
        for i in graph[queue[0]]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
                distance[i] = distance[queue[0]] + 1
        queue.pop(0)
BFS(x)
cnt = 0
for j in range(len(distance)):
    if distance[j] == k:
        print(j)
        cnt += 1
if cnt == 0:
    print(-1)
    
#푼 방법:
#1. 노드 연결리스트와 방문 리스트, 거리 리스트를 생성한다
#2. BFS를 써서 시작 노드에서 거리를  한다.
#3. 새로운 노드의 거리는 그 전의 노드의 거리에서 +1을 한것이다. 그렇게 거리를 저장한다.
#4. 알맞게 출력.


# In[5]:


#48
def DFS_걍_집합_구분용(v):
    visited = [False for _ in range(node+1)]
    visited[v] = True
    stack = [v]
    count = 0
    while len(stack) > 0:
        current = stack[len(stack)-1]
        for i in connection[current]:
            if visited[i] == False:
                visited[i] = True
                stack.append(i)
        count += 1
        team[current] = count%2
        stack.remove(current)
def DFS(v):
    visited = [False for _ in range(node+1)]
    visited[v] = True
    order = []
    team_different = True
    stack = [v]
    while len(stack) > 0:
        current = stack[len(stack)-1]
        for i in connection[current]:
            if visited[i] == False:
                visited[i] = True
                stack.append(i)
                if team[i] == team[current]:
                    team_different = False
        stack.remove(current)
        order.append(current)
    return team_different
        
    
test = int(input())
for teacher_homework_veryvery_hard in range(test):
    node,edge = map(int, input().split())
    ok_list = []
    team = [0 for _ in range(node+1)]
    connection = [[] for _ in range(node+1)]
    for i in range(edge):
        a,b = map(int, input().split())
        connection[a].append(b)
        connection[b].append(a)
    DFS_걍_집합_구분용(1)
    for i in range(1, node+1):
        ok_list.append(DFS(i))
    for j in ok_list:
        result = 'YES'
        if j == False:
            result = 'NO'
            break
    print(result)
    
#푼 방법:
#1. DFS함수를 정의하고, DFS를 사용하기 전에 집합 구분용 함수를 하나 더 정의한다.
#2. 노드의 연결리스트와 각 수의 집합리스트를 만든다
#3. 집합 구분용 함수를 사용하여 집합리스트를 채워넣는다
#4. 각 수마다 DFS를 사용하고, 만약 한 집합에서 같은 집합의 원소와 연결되어 있는지 확인한다.
#5. 만약 같은 집합의 원소가 연결되어있으면 NO, 아니면 YES를 출력한다.


# In[ ]:




