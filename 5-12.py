x1 = {1,2,3,4,5,6}
x2 = {2,3,4,5,1,2}
print(x1.intersection(x2))
print("x1 : ",x1)
x1.intersection_update(x2)
print("x1 : ",x1)

type({}) # dictionary
type({2}) # set

# subset vs supersubset in sets

# Iterator (vs) Genearator 
iter()  --> 
yield() --> 
## Iterator  --> lazy evaluation --> Save in the memory and after-wards calling that we will get the values
a=iter([1,2,3,4,5,6])  
print(a)

next(a)  # the pointer is in 1

# We can interate through an iterator.
for i in a:  # the pointer will go from 2
    print(i)

a[2] # will through error