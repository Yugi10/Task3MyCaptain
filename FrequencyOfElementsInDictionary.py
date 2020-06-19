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
    
"""
OUTPUT :

Please enter your string :
mississippi

The given string as dictionatry of each element and it's frequency in Ascending order :
 [('m', 1), ('p', 2), ('i', 4), ('s', 4)]

The given string as dictionatry of each element and it's frequency in Descending order :
 [('i', 4), ('s', 4), ('p', 2), ('m', 1)]

Final output in Ascending order of frequency of elements is :

m=1
p=2
i=4
s=4

Final output in Descending order of frequency of elements is :

i=4
s=4
p=2
m=1

"""

