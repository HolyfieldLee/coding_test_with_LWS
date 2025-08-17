#!/usr/bin/env python
# coding: utf-8

# In[18]:


m,n = map(int, input().split())
numbers = [0] * (n+1)
for i in range(2,n+1):
    numbers[i] = i
for j in range(2, n+1):
    if numbers[j] == 0:
        continue
    asdf = j
    for k in range(asdf, n+1, asdf):
        if k > asdf:
            numbers[k] = 0
for iiii in numbers:
    if iiii != 0 and iiii >= m:
        print(iiii)


# In[25]:


m,n_fake = map(int, input().split())
n = round(n_fake**0.5)+1
numbers = [0] * (n+1)
skibidi = []
result = 0
for i in range(2,n+1):
    numbers[i] = i
for j in range(2, n+1):
    if numbers[j] == 0:
        continue
    asdf = j
    for k in range(asdf, n+1, asdf):
        if k > asdf:
            numbers[k] = 0
for iiii in numbers:
    if iiii != 0 and iiii >= m:
        skibidi.append(iiii)

for dop in skibidi:
    exponent = 2
    while dop**exponent < n_fake:
        exponent += 1
        result += 1

result

