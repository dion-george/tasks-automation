# importing pandas module 
import pandas as pd 
	
# making data frame 
df = pd.read_csv("attempt-1.csv") 

df['count'] = df.groupby('freq')['freq'].transform(pd.Series.value_counts)
df.sort('count', ascending=False)

df.to_csv('example.csv')
