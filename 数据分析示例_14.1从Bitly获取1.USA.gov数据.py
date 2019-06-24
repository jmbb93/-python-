
# coding: utf-8

# In[6]:


path='D:/jmbb/python/datasets/bitly_usagov.txt'


# In[7]:


open(path).readline()


# In[8]:


import json
records = [json.loads(line) for line in open(path)]


# In[9]:


records[0]


# In[81]:


time_zones = [rec['tz'] for rec in records]


# In[11]:


time_zones = [rec['tz'] for rec in records if 'tz' in rec]


# In[12]:


time_zones[:10]


# In[13]:


def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts


# In[14]:


from collections import defaultdict
def get_counts2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts


# In[15]:


counts=get_counts(time_zones)


# In[17]:


counts['America/New_York']


# In[18]:


len(time_zones)


# In[19]:


counts2=get_counts2(time_zones)


# In[20]:


counts2['America/New_York']


# In[21]:


def top_counts(count_dict,n=10):
    value_key_pairs = [(count,tz) for tz,count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]


# In[22]:


top_counts(counts)


# In[23]:


from collections import Counter
counts=Counter(time_zones)
counts.most_common(10)


# In[24]:


import pandas as pd
frame = pd.DataFrame(records)
frame.info()


# In[25]:


frame['tz'][:10]


# In[26]:


tz_counts = frame['tz'].value_counts()


# In[27]:


tz_counts[:10]


# In[28]:


clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()


# In[30]:


tz_counts[:10]


# In[32]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline #显示图片结果')
subset = tz_counts[:10]
sns.barplot(y=subset.index,x=subset.values)


# In[33]:


frame['a'][1]


# In[39]:


frame['a'][51]


# In[38]:


frame['a'][51][:50] #[:50]截取


# In[40]:


results = pd.Series([x.split()[0] for x in frame.a.dropna()])


# In[41]:


results[:5]


# In[42]:


results.value_counts()[:8]


# In[48]:


import numpy as np


# In[50]:


cframe = frame[frame.a.notnull()]


# In[51]:


cframe['os'] = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')


# In[52]:


cframe['os'][:5]


# In[54]:


by_tz_os = cframe.groupby(['tz','os'])


# In[55]:


agg_counts = by_tz_os.size().unstack().fillna(0)


# In[56]:


agg_counts[:10]


# In[58]:


indexer = agg_counts.sum(1).argsort()


# In[59]:


indexer[:10]


# In[69]:


count_subset = agg_counts.take(indexer[-10:])


# In[70]:


count_subset


# In[63]:


agg_counts.sum(1).nlargest(10)


# In[71]:


count_subset = count_subset.stack()
count_subset.name = 'total'
count_subset = count_subset.reset_index()
count_subset[:10]


# In[72]:


sns.barplot(x='total',y='tz',hue='os',data=count_subset)


# In[75]:


def norm_total(group):
    group['normed_total'] = group.total/group.total.sum()
    return group

results= count_subset.groupby('tz').apply(norm_total)


# In[76]:


sns.barplot(x='normed_total',y='tz',hue='os',data=results)


# In[77]:


g = count_subset.groupby('tz')


# In[78]:


results2=count_subset.total / g.total.transform('sum')


# In[79]:


results2

