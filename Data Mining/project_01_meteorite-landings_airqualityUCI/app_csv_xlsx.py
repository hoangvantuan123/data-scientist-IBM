import pandas as pd

df = pd.read_csv('//Users/tuanhoang/Desktop/Data/meteorite-landings/meteorite-landings.csv')

df.to_excel('/Users/tuanhoang/Desktop/Data/meteorite-landings/meteorite-landings.xlsx' , index=False)