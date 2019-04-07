
# coding: utf-8

# In[1]:


class Student(object):
    def __init__(self,first,last,age):
        self.__name = first
        self.__lastName = last
        self.__age = age
    def __str__(self):
        return "Name is:"+ self.__name
    def getName(self):
        return self.__name

