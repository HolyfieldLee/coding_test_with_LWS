#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#31 - 아마 시간 좀 오래 걸릴 거임..ㅠㅠ
n = int(input())
nlist = []
for i in range(1,n+1):
    for j in range(1,n+1):
        nlist.append(i*j)
nlist.sort()
k = int(input())
nlist[k]


# In[3]:


#32
n,k = map(int, input().split())
asdf = []
for i in range(n):
    sdf = int(input())
    asdf.append(sdf)
count = 0
currentindex = len(asdf)-1
asdf.sort()
while k != 0:
    if asdf[currentindex] > k:
        currentindex += -1
    else:
        while k >= asdf[currentindex]:
            k -= asdf[currentindex]
            count += 1
count

