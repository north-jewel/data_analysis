
# coding: utf-8

# # Visualizing Chipotle's Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[1]:


import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt 

# set this so the graphs open internally
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 

# ### Step 3. Assign it to a variable called chipo.

# In[2]:


chipo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv',sep = '\t')
chipo.head()


# ### Step 4. See the first 10 entries

# In[3]:


chipo.head(10)


# ### Step 5. Create a histogram of the top 5 items bought
# #### 购买前五项的直方图

# In[4]:


x = chipo.item_name
print(x.head())
letter_counts = Counter(x)
print(letter_counts)
df = pd.DataFrame.from_dict(letter_counts, orient='index')


# In[5]:


df


# In[6]:


df1 = df[0].sort_values(ascending = True).tail()


# In[7]:


df1.plot.bar()
plt.xlabel('items')
plt.ylabel('price')
plt.title('the top 5 items ')
plt.show()


# ### Step 6. Create a scatterplot with the number of items orderered per order price
# #### 创建一个散点图，显示每个订单价格下订单的商品数量
# 
# #### Hint: Price should be in the X-axis and Items ordered in the Y-axis
# 提示:价格应该在x轴，商品应该在y轴

# In[8]:


chipo['item_price'] = chipo['item_price'].apply(lambda x:float(x[1:]))


# In[9]:


chipo.head()


# In[10]:


orders = chipo.groupby('order_id').sum()
orders


# In[65]:


plt.scatter(x = orders.item_price,y = orders.quantity,s = 50,c = 'c',marker = '+')
plt.ylim(0)
plt.xlabel('Order Price')
plt.ylabel('Items ordered')
plt.title('Number of items ordered per order price')
# plt.show()


# In[39]:


chipo.item_price


# In[40]:


chipo.item_price.value_counts()


# In[38]:


chipo.item_price.value_counts().head().plot.bar()
plt.show()


# ### Step 7. BONUS: Create a question and a graph to answer your own question.

# In[29]:


a = chipo.groupby(by = 'item_name').max().sort_values('item_price',ascending = False).head()


# In[30]:


a


# In[46]:


x = a.index
y = a.item_price
plt.barh(x,y)


# In[45]:


plt.bar(x,y)

