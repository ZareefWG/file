#list
#bazar = []
#for i in range(5):
 #   inputs = input()
 #   bazar.append(inputs)
#print(bazar)


numbers = [1,2,3,4,5,0.1]


bazar = ['mouse', [8,9,['p','y','t','h','o','n']], 8, 1.5,['a']]
print (bazar[0])

bazar = ['mouse', [8,9,['p','y','t','h','o','n']], 8, 1.5,['a']]
my_list = ['p','y','t','h','o','n']
print (my_list[0], " ",bazar[0])


my_list = ['p','y','t','h','o','n']
print (my_list[1], " ",my_list[5])

odd = [2,4,6,8]
odd[0] = 1
print (odd)


bazar[-1] =['B']
print (bazar)

odd[1:4] = [3,5,7]
print (odd)

odds = [7,9,11,13]
print (odd+odds)

print (['rain']*3)


print (bazar.pop(1))
print (bazar)
bazar.clear()
print (bazar)


h = "hello"
print (h[0])
print (h[0:1]) #both are same in case of strings

factors = [0,1,2,3,4,5]
print (factors[0])
print (factors[0:1]) #in lists the slice returns list where a singl eposition returns a value not a list 


nested = [[2,37],4,["hello",1],5]
print (nested[0])
print (nested[0:1])
print (nested[2] [0] [0:4])

h = "Hello"
H = "help"
print (H[0:5])


Numbers = [1,6,9,29,100]
Numbers[4] = 800
print (Numbers)


#Lists are mutable means that it can be changed in place
#strings are immutable means that it cannot be changed in place

