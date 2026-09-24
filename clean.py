import pandas as pd
df= pd.read_csv('data/project6_time_series_sales.csv')
df['Date']=pd.to_datetime(df['Date'])
col=['Date', 'Sales', 'Orders', 'Customers', 'Marketing_Spend', 'Returns']
df=df.sort_values('Date').reset_index(drop=True)
df['Marketing_Spend'] = df['Marketing_Spend'].interpolate(method='linear')


df.to_csv('data/cleaned.csv',index=False)
print(df)
print(df.shape)
print(df.columns.tolist())
print(df.info())

#print(df[df['Marketing_Spend'].isnull()].index)

#print(df[df.duplicated()])
#for column in df.columns:
#    print(df[column].describe())
#print(df[df['Sales']<0][['Sales','Returns']])

