#!/usr/bin/env python
# coding: utf-8

# In[31]:


#39 
def deching(n):
    asdf = []
    for i in str(n):
        asdf.append(i)
    result = True
    for j in range(len(str(n))//2):
        if asdf[j] != asdf[len(str(n))-1-j]:
            result = False
    return result
nums = [0] * (round(10000001**0.5) + 1)
for i in range(2, len(nums)):
    nums[i] = i
n = int(input())
for j in range(2, len(nums)):
    if nums[j] == 0:
        continue
    for sdf in range(2*j, len(nums)-1, j):
        nums[sdf] = 0
for l in nums:
    if deching(l) == True and l >= n:
        print(l)
        break


# In[13]:


#40
left, right = map(int, input().split())
nums = []
for i in range(left, right+1):
    nums.append(i)
for j in range(2, round(len(nums)**0.5)+1):
    for k in range(len(nums)):
        if nums[k] % j**2 == 0:
            nums[k] = 0
cnt = 0
for l in nums:
    if l != 0:
        cnt += 1
print(cnt)


# In[28]:


#42
n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    asave, bsave = a,b
    while not a*b == 0:
        if a > b:
            a = a%b
            continue
        if a < b:
            b = b%a
            continue
    print(asave * bsave // max(a,b))


# In[30]:


a,b = map(int, input().split())
asave, bsave = a,b
while not a*b == 0:
    if a > b:
        a = a%b
        continue
    if a < b:
        b = b%a
        continue
for asdf in range(max(a,b)):
    print('1', end='')

