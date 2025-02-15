#!/usr/bin/env python
# coding: utf-8

# # 18번

# In[9]:


n = int(input())
p = list(map(int, input().split()))
newp = []
time = 0
for i in range(n):
    newp.append(min(p))
    p.remove(min(p))
for i in range(n):
    time += newp[i]*(n-i)
print(time)


# # 19번

# In[10]:


n,k = map(int, input().split())
nlist = list(map(int, input().split()))
newlist = []
for i in range(n):
    newlist.append(min(nlist))
    nlist.remove(min(nlist))
print(newlist[k-1])


# # 20번

# In[ ]:


#병합 정렬이 기억이 안 납니다... ㅠㅠ

