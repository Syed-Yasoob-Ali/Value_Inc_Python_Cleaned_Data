import pandas as pd

df = pd.read_csv("transaction2.csv",sep=";")

df.info()


#   COST PER ITEM VAR
cost_per_item = df["CostPerItem"]

#   NUMBER OF ITEMS PURCHASED VAR
number_of_items_purchased = df["NumberOfItemsPurchased"]

#   SELLING PRICE PER ITEM VAR
selling_price_per_item = df["SellingPricePerItem"]

#   SALES PER TRANSACTION VAR
sales_per_transaction = selling_price_per_item * number_of_items_purchased

#   PROFIT PER ITEM VAR
profit_per_item = selling_price_per_item - cost_per_item

#   PROFIT PER TRANSACTION VAR
profit_per_transaction = profit_per_item * number_of_items_purchased

#   COST PER TRANSACTION VAR
cost_per_transaction = cost_per_item * number_of_items_purchased


#   CHANGING DAY TO OBJECT DTYPE VAR
DAY = df["Day"].astype(str)

#   MONTH VAR
MONTH = df['Month']

#   CHANGING YEAR TO OBJECT DTYPE VAR
YEAR = df['Year'].astype(str)

#   COMBINING ALL DATES VAR
combined_dates = DAY + '-' + MONTH + '-' + YEAR

#   COST PER TRANSACTION
df["CostPerTransaction"] = cost_per_transaction

#   SALES PER TRANSACTION
df["SalesPerTransaction"] = sales_per_transaction

#   PROFIT PER TRANSACTION
df["ProfitPerTransaction"] = profit_per_transaction

#   MARK UP
df["Markup"] = (sales_per_transaction - cost_per_transaction) / cost_per_transaction

#   ROUNDING MARKUP VAR
round_markup = round(df['Markup'], 2)

#   ROUND OF MARKUP
df['Markup'] = round_markup

#   ADDING THE COMBINED DATE TO DF
df['Date'] = combined_dates


#   BY USING ILOC WE CAN VIEW  SPECIFIC COLUMN
df.iloc[0]    # VIEWS THE FIRST ROW
df.iloc[5,1]  # ROW 5 COLUMN 1



#   SPLTTING THE CLIENT KEYWORD FIELDS
split_col = df['ClientKeywords'].str.split(',', expand=True)


#   CREATING NEW COLS FROM SPLIT COL INTO THE DF
#   CLIENT AGE VAR
df["ClientAge"] = split_col[0]
#   CLIENT TYPE
df['ClientType'] = split_col[1]
#   LENGTH OF CONTRCT
df['LengthofContract'] = split_col[2]


#   USING REPLACE FOR REPLACING THE []
df['ClientAge'] = df['ClientAge'].str.replace("[", "")

df['LengthofContract'] = df['LengthofContract'].str.replace("]", "")

df['ItemDescription'] = df['ItemDescription'].str.lower()

#   MERGING NEW FILES
#   --> READING THE NEW CSV
seasonal_df = pd.read_csv("value_inc_seasons.csv", sep=";")

#  common syntax = pd.merge(df_old, df_new, on = 'key') For ex here the key will be month

df = pd.merge(df, seasonal_df, on="Month")


#   GETTING RID OF UNNESSARY COLS
# basic syntax = df = df.drop('columnname', axis=1) Axis -> 1 col, 0 rows
df = df.drop(['Year', 'Month', 'Day', 'ClientKeywords'], axis=1)


#   EXPORT into a CSV
#df.to_csv('Value_Inc_Cleaned.csv', index = False)  #--> index is the col 0 [1,2,3]



















