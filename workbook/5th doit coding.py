#!/usr/bin/env python
# coding: utf-8

# # 11번

# In[1]:


n = int(input())
requirelist = []
nlist = []
alert = 0
currentlist = [0]
current = 0
for i in range(n):
    a = int(input())
    requirelist.append(a)
for j in range(len(requirelist)):
    while currentlist[len(currentlist)-1] != requirelist[j]:
        current += 1
        currentlist.append(current)
        print("+")
        if current > n:
            print("NO")
            alert = 1
    if alert == 0:
        currentlist.pop(len(currentlist)-1)
        print("-")


# # 12번

# In[8]:


n = int(input())
nlist = list(map(int, input().split()))
asdf = []
for i in range(n):
    large = []
    for j in range(i+1, n):
        if nlist[j] > nlist[i]:
            large.append(nlist[j])
    if len(large) == 0:
        asdf.append(-1)
    else:
        asdf.append(min(large))
for k in asdf:
    print(k, end=' ')


# # 13번

# In[11]:


n = int(input())
asdf = []
for i in range(n):
    asdf.append(i+1)
while len(asdf) != 1:
    asdf.pop(0)
    front = asdf[0]
    asdf.pop(0)
    asdf.append(front)
print(asdf[0])
    


# # 17번

# In[2]:


n = str(input())
asdf = []
nlist = []
for i in n:
    nlist.append(int(i))
while len(nlist) != 0:
    asdf.append(max(nlist))
    nlist.remove(max(nlist))
for j in asdf:
    print(j, end="")


# In[13]:




