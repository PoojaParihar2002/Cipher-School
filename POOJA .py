#!/usr/bin/env python
# coding: utf-8

# In[1]:


##CODING PROBLEM 1

NumList = []
Even_Sum = 0
Odd_Sum = 0
j = 0

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

while(j < Number):
    if(NumList[j] % 2 == 0):
        Even_Sum = Even_Sum + NumList[j]
    else:
        Odd_Sum = Odd_Sum + NumList[j]
    j = j+ 1

print("\nThe Sum of Even Numbers in this List =  ", Even_Sum)
print("The Sum of Odd Numbers in this List =  ", Odd_Sum)


# In[5]:


#CODING PROBLEM 2

def find(nums):
 
    distinct = {*nums}
 
    index = 5
    while True:
        if index not in distinct:
            return index
        index += 1
nums = [5, 1, 2, 3, 4, 5]
print('smallest missing positive natural number',find(nums))
 

 
    #nums = [5, 1, 2, 3, 4, 5]
   # print('smallest missing positive natural number',
      #  find(nums))




# In[ ]:




