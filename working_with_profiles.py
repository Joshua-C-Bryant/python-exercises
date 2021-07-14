#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[2]:


json.load(open('profiles.json'))


# In[3]:


profiles = json.load(open('profiles.json'))


# In[4]:


print(len(profiles))


# In[5]:


name = 'name'
names = [dictionary[name] for dictionary in profiles]


# In[6]:


print(names)


# ### Number of Users

# In[7]:


print(len(names))


# In[8]:


is_active = [dictionary['isActive'] for dictionary in profiles]


# In[9]:


print(is_active)


# ### Number of Active Users

# In[10]:


is_active.count(True)


# ### Number of Inactive Users

# In[11]:


is_active.count(False)


# In[12]:


balances = [dictionary['balance'] for dictionary in profiles]


# ### Grand total of balances

# In[13]:


print(balances)


# In[38]:


cleaned_balances = []
for balance in balances:
    balance = balance.replace('$','')
    balance = balance.replace(',','')
    balance = float(balance)
    cleaned_balances.append(balance)


# In[40]:


print(sum(cleaned_balances))


# ### Average balance per user

# In[46]:


average_balance = (sum(cleaned_balances))/len(balances)
print(round(average_balance,2))


# ### User with the lowest balance

# In[48]:


print(min(balances))


# In[91]:


user_with_lowest_balance = next(i for i in profiles if i['balance']=='$1,214.10')


# In[60]:


print(user_with_lowest_balance)


# In[61]:


print(user_with_lowest_balance['name'])


# ### User with the highest balance

# In[62]:


print(max(balances))


# In[63]:


user_with_highest_balance = next(i for i in profiles if i['balance']=='$3,919.64')


# In[64]:


print(user_with_highest_balance)


# In[65]:


print(user_with_highest_balance['name'])


# ### Most common favorite fruit

# In[67]:


favorite_fruit = [dictionary['favoriteFruit'] for dictionary in profiles]


# In[68]:


print(favorite_fruit)


# In[73]:


from collections import Counter

print(Counter(favorite_fruit))

most_common_favorite_fruit = max(Counter(favorite_fruit))


# In[74]:


print(most_common_favorite_fruit)


# ### Leaset common favorite fruit

# In[75]:


least_common_favorite_fruit = min(Counter(favorite_fruit))


# In[76]:


print(least_common_favorite_fruit)


# ### Total number of  unread messages for all users

# In[80]:


greetings = [dictionary['greeting'] for dictionary in profiles]


# In[81]:


print(greetings)


# In[85]:


number_of_messages = []
for greeting in greetings:
    for letter in greeting:
        if letter.isnumeric() == True:
            number_of_messages.append(letter)


# In[87]:


print(number_of_messages)


# In[88]:


number_of_messages_as_int = [int(i) for i in number_of_messages]


# In[89]:


print(sum(number_of_messages_as_int))

