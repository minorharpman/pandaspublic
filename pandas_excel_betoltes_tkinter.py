
#Pandas excel betöltés
# https://colab.research.google.com/drive/1jm-EFvKUAdwZmWSfhD7hC-Lc2KlUhYcS?usp=sharing

import pandas as pd
import tkinter as tk
from tkinter import ttk

def build_table(data):
    # Létrehozza a főablakot (root = fő GUI ablak)
    root = tk.Tk()

    # Fejléc színezése
    style = ttk.Style(root)
    style.theme_use("default")
    style.configure("Treeview.Heading", background="#444", foreground="white", font=("Arial", 10, "bold"))

    # Létrehoz egy keretet (frame) a főablakon belül
    frame = ttk.Frame(root)

    # A frame kitölti a rendelkezésre álló helyet, és méretezhető
    frame.pack(fill=tk.BOTH, expand=True)

    # A DataFrame oszlopainak listáját kinyerjük
    columns = data.columns.tolist()

    # Létrehozunk egy táblázatot (Treeview) a megadott oszlopokkal, csak fejlécekkel
    tree = ttk.Treeview(frame, columns=columns, show='headings')

    # A táblázat a bal oldalra kerül, és kitölti a helyet
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Fejlécek és oszlopszélességek beállítása
    for col in columns:
        # Az oszlop fejléce (felirat) beállítása
        tree.heading(col, text=col)

        # Az oszlop szélessége és igazítása (balra)
        tree.column(col, width=120, anchor="w")

    # Sorok hozzáadása a táblázathoz
    #for row in data.itertuples(index=False):
    for _, row in data.iterrows():
        # Minden sort hozzáadunk a táblázathoz (értékek tuple-ként)
        #tree.insert('', tk.END, values=row)
        tree.insert('', tk.END, values=list(row))

    # Görgetősáv létrehozása (függőleges), ami a táblázat görgetését vezérli
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)

    # Összekapcsoljuk a táblázat görgetését a görgetősávval
    tree.configure(yscrollcommand=scrollbar.set)

    # A görgetősáv a jobb oldalra kerül, és kitölti a függőleges teret
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Elindítja az eseménykezelő ciklust (az ablak megjelenik és használható lesz)
    root.mainloop()



 

# Excel fájl beolvasása
df = pd.read_excel('files/SampleData.xlsx')
#df['OrderDate'] = pd.to_datetime(df['OrderDate']).dt.date
df['OrderDate'] = df['OrderDate'].dt.date

# megjelenítés tkinter segítségével
build_table(df)


'''
for index, row in df.iterrows():
    order_date = str(row['OrderDate'])
    print ( order_date[0:10] , row['Item'])
    #print(row.to_dict())
'''


