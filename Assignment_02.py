#!/usr/bin/env python
# coding: utf-8

# #### 1.What are the two values of the Boolean data type? How do you write them?
# 

# In[ ]:


# two values of boolean data type is true and false
# we write in python these values True and False


# #### 2. What are the three different types of Boolean operators? 

# In[ ]:


# Three types of boolean operators are 
# and
# or
# not


# #### 3. Make a list of each Boolean operator&#39;s truth tables (i.e. every possible combination of Boolean
# #### values for the operator and what it evaluate ). 

# In[ ]:


# p and q are  two conditions
# x=22
# y=23
# p= x>y
# q =y>x
#  x>y or y>x

# operator  syntex     operations                                    output
#  and       p and q   if p is true and q is true                     True
#  and       p and q   if p is true and q is false                    False
#  and       p and q   if p is false and q is true                    False

#  or       p or  q    if p is false and q is false                   False
#  or       p or  q    if p is false and q is true                    True
#  or       p or  q    if p is true and q is false                    True

# not       not p      if p is not true                               True
# not       not q      if q is true                                   False


# #### 4. What are the values of the following expressions?
# #### 1. (5 >4) and (3 == 5)
# #### 2. not (5 > 4)
# #### 3.(5 > 4) or (3 == 5)
# #### 4.not ((5 > 4) or (3 == 5))
# #### 5.(True and True) and (True == False)
# #### 6.(not False) or (not True) 

# In[ ]:


#1. False
#2. False
#3. True
#4. False
#5. False
#6. True


# #### 5. What are the six comparison operators?

# In[ ]:


# == equal to
# >= greater than and equal to
# <= lesser than and equal to
# >  greater than
# <  lesser than
# != not equal to


# #### 6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.

# In[ ]:


# assignment operators is denoted by = it define the value of for example a=10, b=10
# equal to is a comparision operator. for this we define the condition is true it is denoted by == . a==b


# #### 7. Identify the three blocks in this code:

# In[ ]:


spam = 0
if spam == 10:
    print('eggs')          # indent increased block a
    if spam > 5:           # still block a
        print('bacon')     # slill block a indent incresed block b inside a
    else:                  # still block a indent decresed block b ended
        print('ham')       # still bock a indent increased block c inside block a
    print('spam')          # still block a indent decreased block c ended
print('spam')              # indent decreased block a ended in above line


# #### 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
#           

# In[32]:


n= int(input('the value of n'))
spam=n
if spam == 1:
    print('Hello')
elif spam ==2 :
    print('Howdy')
else:
    print('greetings')


# #### 9.If your programme is stuck in an endless loop, what keys you’ll press? 

# In[ ]:


# Ctr+c


# #### 10. How can you tell the difference between break and continue?

# In[37]:


# Generally break and continue keywords is used in loop.so i can explin this with the help of one example
l=[1,2,3,4,5,6,78,9,12]
for i in l:
    if i==5:
        break # so here when i==5 it will be break the loop before 5 everything will be print present in list 
    print(i)


# In[38]:


l=[1,2,3,4,5,6,78,9,12]
for i in l:
    if i==5:
        continue #  with the help of continue we can leave 5 and each integer present in list can be print
    print(i)


# #### 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

# In[ ]:


# There is no difference between range because in case of range(10) default it will start from 0 and in range(0,10,1) default 
# range function take gap of 1.


# #### 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# In[39]:


for i in range(1,11):
    print(i)
    


# In[40]:


i=1
while i<11:
    print(i)
    i=i+1


# #### 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
# 

# In[ ]:


spam.bacon()

