#!/usr/bin/env python
# coding: utf-8

# In[6]:


#29

m = int(input())
nlist = list(map(int, input().split()))
find = int(input())
flist = list(map(int, input().split()))

nlist.sort()

for i in range(find):
    left = 0
    right = m-1
    target = flist[i]
    tteokbokki_meokko_shipda = 0
    while left <= right:
        med = round((left + right)/2)
        if nlist[med] == target:
            tteokbokki_meokko_shipda = 1
            break
        if nlist[med] > target:
            right = med-1
            continue
        if nlist[med] < target:
            left = med+1
            continue
    
    print(tteokbokki_meokko_shipda)


# In[9]:


#30
l,br = map(int, input().split())
mlist = list(map(int, input().split()))
minutes = []

for i in range(max(mlist), sum(mlist)+1):
    minutes.append(i)

for i in minutes:
    left = 0
    right = len(minutes)-1
    
    while left <= right:
        med = round((left + right)/2)
        count = 0
        timesum = 0
        for i in range(l):
            if timesum + minutes[i] > med:
                count += 1
                timesum = 0
            timesum += minutes[i]
        if timesum != 0:
            count += 1
            
        if count > br:
            left = med + 1
        if count < br:
            right = med - 1
print(left)

