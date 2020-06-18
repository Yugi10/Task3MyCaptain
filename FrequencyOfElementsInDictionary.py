#!/usr/bin/env python
# coding: utf-8

# In[10]:


import operator

str = input("Please enter your string :\n")
output = {}

for i in str:
    output [i] = str.count(i)

Ascending = sorted (output.items(), key = operator.itemgetter(1))
Descending = sorted (output.items(), key = operator.itemgetter(1), reverse = True)

print ("\nThe given string as dictionatry of each element and it's frequency in Ascending order :\n", Ascending)
print ("\nThe given string as dictionatry of each element and it's frequency in Descending order :\n", Descending)

print ("\nFinal output in Ascending order of frequency of elements is :\n")
for i in Ascending:
    print (f"{i[0]}={i[1]}")
    
print ("\nFinal output in Descending order of frequency of elements is :\n")
for i in Descending:
    print (f"{i[0]}={i[1]}")


# In[ ]:




