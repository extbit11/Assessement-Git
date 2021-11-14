#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random

class Random:
    def __init__(self,n,seeda,seedb):
        self.amount=n
        self.minRange=seeda
        self.maxRange=seedb

    def myfunc(self):
        if self.maxRange <= 0:
            print("maxRange should be greater than 0")
        elif self.maxRange >0 and self.minRange < 0:
            print("minRange should be greater or equal than 0")
        elif self.maxRange > 0 and self.minRange >= 0 and self.minRange >= self.maxRange:
            print("minRange should be lesser than maxRange")
        elif self.maxRange > 0 and self.minRange >= 0 and self.minRange < self.maxRange:

            numbers = []
            while len(numbers) != self.amount:
                a = self.maxRange
                b = self.maxRange
                while a == 0 or a == self.maxRange:
                    a = random.randint(0, self.maxRange)
                while b < 0 or b == self.maxRange:
                    b = random.randint(0, self.maxRange)

                rn = (a * self.minRange + b) % self.maxRange
                if rn >=self.minRange and rn <= self.maxRange :
                    numbers.append(rn)
            print(numbers)
x = Random(7,15,50)
x.myfunc()


# In[ ]:




