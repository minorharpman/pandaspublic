


import pandas as pd

# Excel fájl beolvasása
df = pd.read_excel('files/SampleData.xlsx')

for index, row in df.iterrows():
    order_date = str(row['OrderDate'])
    print ( order_date[0:10] , row['Item'])
    #print(row.to_dict())

