#!/usr/bin/env python
# coding: utf-8

# In[6]:


#price of renting a movie per day = $3 per day
def total_price(n):
    return n*3


# In[2]:


#The Little Mermaid (3 days)
total_price(3)


# In[3]:


#Brother Bear (5 days)
total_price(5)


# In[4]:


#Hercules(1 day)
total_price(1)


# In[11]:


#Pay for different companies
def google_pay(n):
    return n*400
def amazon_pay(n):
    return n*380
def facebook_pay(n):
    return n*350


# In[9]:


google_pay(6)


# In[10]:


amazon_pay(4)


# In[12]:


facebook_pay(10)


# In[13]:


class_not_full = True
no_class_conflicts = True
enrollment_eligibility = class_not_full and no_class_conflicts


# In[14]:


enrollment_eligibility


# In[6]:


#product offer eligibility
def product_offer_eligibility():
    if sales > 2 and date() > now():
        return True
    if premium_member and date() > now():
        return True
    else: False


# In[7]:


#usernam/password exercises
username = 'codeup'
password = 'notastrongpassword'


# In[12]:


if len(password) > 5 : True


# In[14]:


if len(username) > 20 : False


# In[15]:


if username == password : False


# In[23]:


if username[0] == " " or username[-1] == " " or password[0] == " " or password[-1] == " ": False

