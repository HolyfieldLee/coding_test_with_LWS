#!/usr/bin/env python
# coding: utf-8

# In[2]:


swap = 0
n = int(input())
array = list(map(int, input().split()))
for i in range(n):
    for j in range(n-i-1):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
            swap += 1
print(swap)


# In[3]:


node,link = map(int, input().split())
for i in range(link):
    x,y = map(int, input().split())
...

