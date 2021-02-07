''' 										
What is iterable ???
Iterable is an object, which one can iterate over (loop over). It generates an Iterator when passed to iter() method. 
which is used to iterate over an iterable object using __next__() method.

Define Iterator 
In computer programming, an iterator is an object that enables a programmer to traverse a container, particularly lists
iterator is an object with a state so that it remembers where it is during an iteration, it also knows how to get the next value by using __next__()
When there is StopIteration exception, it means that the iterator has been exhausted and has no more values.
											
Every iterable is not an iterator.
Every iterator is also an iterable.

__iter__() --> can be executed by using iter(), if present --> it is an iterable
__next__() --> can be executed by using next(), if present --> it is an iterator

dir(object) --> Returns all the attributes of that object.

Why list is iterable but not an iterator ??
List is iterable 
dir(list1) contains __iter__() and doesn't contain __next__()
'''
list1 = [1,2,3]
print("Only List with __iter__()[iterable]")
print(dir(list1))
# print(next(list1))  --> Error : List object is not an iterator
# Then how for loop works over the list

i_list = iter(list1)
print("List along with __next__()[iterator]")
print(dir(i_list))

print(next(i_list))
print(next(i_list))
print(next(i_list))
# print(next(i_list)) --> Will show StopIteration (indicating there are no further elements to iterate)

'''
But why for loop doesn't raise this exception???
A normal for loop knows how to handle the StopIteration exception
								For loop At background 
When a for loop is executed, for statement calls iter() on the object, which it is supposed to loop over. 
If this call is successful, the iter call will return an iterator object that defines the method __next__(),
which accesses elements of the object one at a time.The __next__() method will raise a StopIteration exception,
if there are no further elements available.The for loop will terminate as soon as it catches a StopIteration exception.
'''

i_list = iter(list1)  # i_list is an iterator object
while True:
	try:
		item = next(i_list)
		print(item)
	except StopIteration:
		break

## Creating own range function (range() is iterable not an iterator like list)
class MyRange:
	def __init__(self,start,end):
		self.start = start  # starting value 
		self.value = start  # Iterating value
		self.end = end      # end value
	
	def __iter__(self):  # Generally __iter__() must retrun an iterator object which contains __next__()
		return self    # So we are returning just the __iter__() and adding __next__() in this class itself

	def __next__(self):
		if self.value>=self.end:   # Should stop when it goes beyond the end-value
			raise StopIteration
		current    = self.value
		self.value = self.value+1
		return current

obj1 = MyRange(0,10)
for i in obj1:
    print(i)

print(next(obj1)) # Error 



