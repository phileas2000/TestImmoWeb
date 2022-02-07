import pandas as pd

data=pd.read_csv('static/immo_CSV.csv',delimiter=";")
print(data.head(15))