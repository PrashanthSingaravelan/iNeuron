string="Hello"
num=upper=lower=0

for i in string:
	if i.islower():lower+=1
	elif i.isupper(): upper+=1

##########################################################################################

# Difference between list.append() and list.extend()
list1 = [1,2,"Prashanth",3,9+7j]
list2 = ["Hello",619]
print("Append : ")
list1.append(list2)  # list within a list
print(list1)

## Will work only in jupyter (%%time) To find the time taken for a particular cell to execute
list1 = [1,2,"Prashanth",3,9+7j]
list2 = ["Hello",619]
print("Extend : ")
list1.extend(list2)
print(list1)

##########################################################################################

## for else condition
sum1=0
for i in list1:
    if i==2:
        break   # will completely come out and will not go the else also
    sum1+=i
else:
    print("This sum is ",sum1)


sum1=0
for i in list1:
    if i==2:
        sum1+=i
else:
    print("This sum is ",sum1)  # Will get execute if the for is executed successfully
    
print("The final sum out of the loop : ",sum1)

##########################################################################################
list1 = [1,2,3,4,5,6,7]
sum_odd = sum_even = 0
for i in list1:
    if i%2==0:
            sum_even+=i
            if sum_even>20:
                   break
    else:
            sum_odd+=i
            if sum_odd>20:
                break

else:  # Will get execute if the for is executed successfully
    print("Odd sum = {} and Even sum = {}".format(sum_odd,sum_even))

#########################################################################################
str1 = "Prashanth"
print(str1)
print(str1[:])
print("Reverse of a string : ",str1[::-1])

str1 = "This is , good "
str1.split()    # Splits when there is a space
str1.split(';') # Splits what ever character is given

str1.split('s') # to ommit s
str1.partition('s')  #  to include s

str1 = "Prashanth"
str1.find('a')  # Will get only the index of the first occurence
str1.center(20,'@')  # Will make the string padded with  (@5+9(len of the string)+6@)
 
str1.isalnum()
str1.isalpha()

str1 = "Pras/hanth"
print(str1.expandtabs())
#########################################################################################
