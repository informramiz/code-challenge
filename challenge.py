
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import uuid


# In[2]:

SUM_INTERVALS = [(-7,0), (-14,0), (-30,0)]


# ## Generate some random data

# In[3]:

uids=np.array([str(uuid.uuid4()) for _ in range(10)])
times = pd.date_range('2016-01-01','2016-02-01', freq='s')
data = dict(
    id=np.random.choice(uids, 100),
    timestamp=np.random.choice(times, 100),
    feature_a=np.ones(100),
    feature_b=np.zeros(100),
)


# ## Challenge:
# The `SUM_INTERVAL` variable contains relative time intervals in days. So the first means 7 days back until today (asof time writing this 2016-02-01).
# the dictionary `data` contains 10 distinct users which made visists over the timespan of one month. Each visit has a value for `feature a`, as awell as `feature_b` assigned to it. **For each user calculate the sum of it's respective features for each time interval. The final output should be a dataframe or numpy matrix containing one row per user, an id column an the feature columns (N_users, 1 + N_intervals*N_features)**
# 
# *It is encouraged to use the pandas library for this task but it is not required.*

# In[4]:

def bin_sum_features(data, today=pd.Timestamp('2016-02-01')):
    pass


# ## Result shape example
# below you see how the results could look like with pandas

# In[5]:

pd.DataFrame([['1aa9204b-5956-41a3-96b6-58cbf6bc147e',1,2,3,4,5,6]], 
             columns=['id', 'feature_a_7', 'feature_a_14', 'feature_a_30', 
                      'feature_b_7', 'feature_b_14', 'feature_b_30'])


# ## Solution

# In[6]:

import math

def do_bin(df, start, end):
    #find the visits that are in given bin and sum the features for those visits
    select = df[(df.days_diff >= start) & (df.days_diff <= end)].groupby(['id']).sum()

    bin_features = {}
    #add the features with appropriate name to dictionary
    bin_features['feature_a_' + str(abs(start))] = select['feature_a']
    bin_features['feature_b_' + str(abs(start))] = select['feature_b']
    
    return bin_features

def do_bin_sum_features(data, today=pd.Timestamp('2016-02-01')):
    #convert data dictionary into a pandas DataFrame
    df = pd.DataFrame(data)

    #calculate days in past from today for each user visit
    df['days_diff'] = df['timestamp'].apply(lambda t: (t - today).days)

    #to verify code correctness, adding an assertion
    assert np.sum(do_bin(df, -31, 0)['feature_a_31']) == 100, "feature_a_31 sum is not 100"
    
    #for each time bin, sum features for each user
    items = {}
    for start, end in SUM_INTERVALS:
        #find the visits that are in given bin and sum the features for those visits
        items.update(do_bin(df, start, end))
        
    #create another pandas DatFrame from this new dictionary
    return pd.DataFrame(items)
    
    
do_bin_sum_features(data)


# In[ ]:



