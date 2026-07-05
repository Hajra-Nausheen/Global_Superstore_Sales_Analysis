import pandas as pd
df=pd.read_csv("C:/Users/Hajra Syed/OneDrive/Documents/My Data Sources/Global_Superstore_Project/Superstore_raw.csv")

print(df.head())
print(df.info())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())


print(df['Market'].equals(df['Market2']))

print(df[['Market','Market2']].drop_duplicates().head(20))

print(df['Record_Count'].value_counts())

# Remove Unnecessary Columns
df.drop(
    columns= ['Unnamed: 0','Record_Count'],
    inplace=True)

# print(df.head())

# Standardize colums names
df.columns=(
    df.columns
    .str.lower()
    .str.replace(' ','_')
)

# print(df.head())

print(df['order_date'].head(10))
print(df['ship_date'].head(10))

# Convert Dates
df['order_date'] = pd.to_datetime(df['order_date'])
df['ship_date'] = pd.to_datetime (df['ship_date'])
print(df[['order_date','ship_date']].dtypes)

# Feature Engineering
# oreder year
df['order_year']=df['order_date'].dt.year

# order month (name)
df['order_month']=df['order_date'].dt.month_name()

# order month (number)
df['order_month_num']=df['order_date'].dt.month

# order quarter
df['order_quarter']=df['order_date'].dt.quarter

# Shipping days
df['shipping_days'] =(
    df['ship_date'] - df['order_date']
).dt.days

# Profit Margin
df['profit_margin']=(
    df['profit']/ df['sales']
)*100

df['profit_margin']=df['profit_margin'].round(2)

# print(df.head())

# Clean text column
text_columns=[
    'category',
    'city',
    'country',
    'customer_name',
    'market',
    'product_name',
    'region',
    'state',
    'sub_category'
]
for col in text_columns:
    df[col]=(
        df[col]
        .str.replace(r'\s+', ' ', regex=True)
        .str.strip()
    )

(df['year'] == df['order_year']).all()


# df.to_csv(
#     'global_superstore_cleaned.csv',
#     index=False,
#     encoding='utf-8'
# )

# print("File saved successfully!")

# import os

# print(os.path.exists('global_superstore_cleaned.csv'))

print(df.shape)
print(df.columns.tolist())

import numpy as np

df['profit_margin'] = np.where(
    df['sales'] != 0,
    (df['profit'] / df['sales']) * 100,
    0
)

print(df['profit_margin'].isin([np.inf, -np.inf]).sum())


print(df[['order_date','ship_date','shipping_days']].head(10))

(df['ship_date'] - df['order_date']).dt.days

# print(df.columns)

# with open('global_superstore_cleaned.csv', "r", encoding="utf-8") as f:
#     for i, line in enumerate(f, start=1):
#         if i == 51292:
#             print(repr(line))
#             break


# print(df.shape)
# print(df.columns.tolist())

# Cleaned dataset saving
# df.to_csv(
#     'global_superstore_cleaned.csv',
#     index=False
# )

df.to_csv(
    'global_superstore_final.csv',
    index=False,
    encoding='utf-8'
)


print("CSV saved sucsessfully!")

# new_df = pd.read_csv('global_superstore_final.csv')

# print(new_df.shape)
# print(new_df.columns.tolist())

# import os

# print(os.path.exists('global_superstore_final.csv'))

# import pandas as pd

# df_test = pd.read_csv("global_superstore_final.csv")
# print(df_test.shape)



