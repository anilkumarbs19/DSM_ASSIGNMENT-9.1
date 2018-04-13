
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

'''
PROBLEM STATEMENT 1
-------------------
How-to-count-distance-to-the-previous-zero. For each value, count the difference back to the previous zero (or the start of 
the Series, whichever is closer).

Create a new column 'Y'

Consider a DataFrame df where there is an integer column 'X'
import pandas as pd
df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

'''
### SOLUTION ###

df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
df = df.assign(Y = df.loc[df.X==0])
nulval = df['Y'].isnull()
df = df.assign(Y = nulval.groupby((nulval.diff() == 1).cumsum()).cumsum())
print("Dataframe with y column containing distance to previous zero or to the start of the series:\n\n", df, "\n")


'''
PROBLEM STATEMENT 2
-------------------

Create a DatetimeIndex that contains each business day of 2015 and use it to index a series of 
random numbers.

'''

### SOLUTION ###

date_range_y2015_bd = pd.date_range('1/1/2015', '12/31/2015', freq='B') 
series_randn_dtrng_index = pd.Series(np.random.randn(date_range_y2015_bd.size), index=date_range_y2015_bd)
print("The series of randon numbers with date range as index is:\n\n", series_randn_dtrng_index, "\n")


'''
PROBLEM STATEMENT 3
-------------------

Find the sum of the values in s for every Wednesday

'''

### SOLUTION ###

sum_wed = series_randn_dtrng_index.loc[series_randn_dtrng_index.index.weekday==2].sum()
print("The sum of the values in the series for every Wednesday is:", sum_wed, "\n")


'''
PROBLEM STATEMENT 4
-------------------

Find average For each calendar month

'''

### SOLUTION ###

series_avg_each_month = series_randn_dtrng_index.resample('M').mean()
print("Average for each calendar month:\n\n", series_avg_each_month, "\n")


'''
PROBLEM STATEMENT 5
-------------------

For each group of four consecutive calendar months in s, find the date on which the highest value occurred.

'''

max_idx = series_randn_dtrng_index.resample('4M', closed='left').agg({np.argmax})
print("The dates in four consecutive months where the highest value occurred are {:%Y-%m-%d}, {:%Y-%m-%d} and {:%Y-%m-%d}".format(max_idx.argmax[0], max_idx.argmax[1], max_idx.argmax[2]))

