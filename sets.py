# Set. Sets are used to store multiple items in a single variable. Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage. A set is a collection which is both unordered and unindexed.


s = set()
print (type(s))
sFromList = set([1,2,3,4,5,6,7])
print (sFromList)
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add("a")
print (s)
#set only appends the unique values. Like the sets in maths.



s1 = {1,4,6}
s2 = {5,4,9}
L = s1.union(s2)
print (L)
V = (s1.intersection(s2))
print (V)
print (len(s1))
print (type(s1))
print (min(s1))
print (max(s1))


#Union (u) : The symbol is like a cup and the function of it is to print the numbers in the variables. But the same numbers will not be printed
#For example:
s1 = {1,4,6}
s2 = {5,4,9}
L = s1.union(s2)
print (L)
#In this Code 1,4,5,6 and 9 will be printed only. But the remaining number, 4 will not be printed because it is repeated

#Intersection (ꓵ) : The symbol is like a cap and the function of it is to print the common numbers in the variables. The numbers which don't come twice won't be printed.
#For Example:
s1 = {1,4,6}
s2 = {5,4,9}
L = s1.intersection(s2)
print (L)
#In this code the number 4 is common and it will be printed only. The other numbers: 1,5,6 and 9 are not common and therefore will not be printed.




s = set()
List = set([1,2,3,4,5,6,7,8])
print (List)
s.add(1)
s.add("Hello")
print (s)


