# https://colab.research.google.com/drive/1jm-EFvKUAdwZmWSfhD7hC-Lc2KlUhYcS?usp=sharing
# https://github.com/minorharpman/pandaspublic/

# csomagok telepítése, parancsok a Terminálban
# pip install pandas
# pip install openpyxl


import pandas as pd

# Excel fájl beolvasása, read_excel - függvény
df = pd.read_excel('files/SampleData.xlsx')

#print(df.head())
print(df)
#print(df['OrderDate'])


#bejárások
'''
for index, row in df.iterrows():
    order_date = str(row['OrderDate'])
    print ( order_date[0:10] , row['Item'])
    #print(row.to_dict())
'''




