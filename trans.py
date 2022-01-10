import pandas as pd
from googletrans import Translator

df = pd.read_csv(r"C:\Users\talha\Downloads\cfco.csv")
transl = df.loc[:,'comment']
translations = {}
translater = Translator()
for i in range(len(transl)):
    # Unique elements of the column
    print(translater.translate(transl[i],dest="en").text)