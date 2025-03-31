import pandas as pd

 

namen_df = pd.read_excel('namen.xlsx', sheet_name="collectie")
bestelling_df = pd.read_csv('bestelling.csv')

namen_df.head()

# namen_df['postcode'] = namen_df['postcode'].fillna(8017)

# namen_df['letters'] = namen_df['letters'].fillna('CA')

# namen_df.loc[namen_df['id'] == 3, 'huisnummer'] = 14

# namen_df.head()

 

# kosten=9

# shirt=50

# namen_df['Naam_Lengte'] = namen_df['naam'].apply(len)

# namen_df['Kosten_Shirt'] = shirt + (namen_df['Naam_Lengte'] * kosten)

# namen_df.head()

 

# bestelling_df.columns = ['klantid', 'bestelid']

# bestelling_df.head(15)

# result = pd.merge(namen_df, bestelling_df, left_on='id', right_on='klantid', how='inner')

# result.head(30)

 

# namen_df['postcode'] = namen_df['postcode'].astype(int)

# namen_df.head()