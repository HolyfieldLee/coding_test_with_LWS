#!/usr/bin/env python
# coding: utf-8

# 

# In[29]:


# 33
from queue import PriorityQueue

n = int(input())
cards = PriorityQueue()
for i in range(n):
    asdf = int(input())
    cards.put(asdf)
cardsum = 0
while cards.qsize() > 1:
    first = cards.get()
    second = cards.get()
    sdf = first + second
    cards.put(sdf)
    cardsum += sdf
print(cardsum)


# In[41]:


#34
#음수는 최대한 절대값이 큰 애들부터 묶기
#양수도 마찬가지
#0은 음수 남는 거 있으면 묶어주기, 없으면 걍 더하기
#1은 더하는게 이득이니 남기기


nums = []
n = int(input())
for i in range(n):
    asdf = int(input())
    nums.append(asdf)
negative = PriorityQueue()
positive = PriorityQueue()
ones = 0
zeros = 0
for i in nums:
    if i < 0:
        negative.put(i)
    if i > 1:
        positive.put(i * -1)
    if i == 1:
        ones += 1
nsum = 0
while positive.qsize() > 1:
    sdf = positive.get()
    df = positive.get()
    nsum += sdf*df

while negative.qsize() > 1:
    sdf = negative.get()
    df = negative.get()
    nsum += sdf*df

if positive.qsize() > 0:
    nsum += positive.get() * -1

nsum += ones

nsum


# In[46]:


#36
asdf = list(map(str, input().split("-")))
numbers_to_calculate = []
for i in asdf:
    small_shik = str(i).split("+")
    small_sum = 0
    for j in small_shik:
        small_sum += int(j)
    numbers_to_calculate.append(small_sum)
real_sum = numbers_to_calculate[0]
for k in range(1, len(numbers_to_calculate)):
    real_sum -= numbers_to_calculate[k]
real_sum

