#!/usr/bin/env python
# coding: utf-8

# #### 1. In the below elements which of them are values or an expression? eg:- values can be
# integer or string and expressions will be mathematical operators.
# *
# 'hello'
# -87.8
# -
# /
# +
# 6

# In[ ]:


# * ,/,-,+, are  the expression and 'hello', -87.8,6 are the values


# #### 2. What is the difference between string and variable?

# In[ ]:


# Variable= varibles is the collection of informations for examples list, string,dictonary,set,tuple and text
# for example a=[1,2,3,4,5,6,7,(1,2,3,4,5),'string']
# here a is the varible 
# string is the type of information which is present in variable
# for example a='This is the string'
# here a is the variable and this is the string is string.


# #### 3. Describe three different data types. 

# In[ ]:


# 1. string  example 'My name', 'his name', 'pythoncode'
# 2. integer examle 1,2,3,45,6
# 3. float   example 1.2,1.0, 3.4


# #### 4. What is an expression made up of? What do all expressions do?

# In[ ]:


# An Expression is the combination of operators and by using these operators we produces some other values.


# In[1]:


# 1. Constant Expressions: These are the expression that have constant value only for example
a= 45+34
print(a)


# In[3]:


# 2. Arithmetic Expressions:- combination of values, operators and parenthesis. The operations which is used in this expression 
# is the arithmatic operation like addition, multiply,devision etc.
# operators syntex operation
#   +        X+Y     addition
#   *       X*Y      Multiplication
#    -       X-Y     subtraction
X=23
Y=20
a=X+Y
print(a)


# In[4]:


# 3. Integral Expressions: produce only integer after applying all operations
a=13
b=56.5
c=a+int(b)
print(c)


# In[5]:


#4. Integral Expressions: return always floating values
a=12
b=14
c=float(a)+float(b)
print(c)


# In[6]:


#Relational Expressions:These are called comparision operators also(>,<,=,<=,>=)
a=21
b=23
a>b


# In[8]:


#6. Logical Expressions:Denote by and , or , not
# and : It give true only when both condition are true othewiswe false
# or  : It give true if one conditon is true 
# not : It give true if condition is false
a=13
b=14 
c=15
a>b and b>c 
a<b and b>c



# #### 5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
# 
# 
# 

# In[ ]:


# an expression is the cobination of values which always give the result by applying some operators.
# Each and every excecutable line which we write like define a variable, if and else statement is called statement.


# #### 6. After running the following code, what does the variable bacon contain? bacon = 22   bacon +1
# #### ans: 23
# 
# 

# #### 7. What should the values of the following two terms be?
# #### 'spam'+'spamspam'
# #### 'spam' * 3
# 

# In[ ]:


# 1. spamspamspam
# 2. spamspamspam
# in both statement we will get same value 


# #### 8. Why is eggs a valid variable name while 100 is invalid?
# 

# In[ ]:


# we can not start a variable by numeric value so if we will take 100 as a varible it will show error.


# #### 9. What three functions can be used to get the integer, floating-point number, or string version of a value?
# 

# In[ ]:


# int()   for getting the integer
# float() for getting the floating point number
# str()   for getting the string version


# #### 10. Why does this expression cause an error? How can you fix it? 'I have eaten' + 99 +  'burritos'
# 

# In[ ]:


# This will show error because data type is not same 

