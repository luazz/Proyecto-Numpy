import pandas as pd

def separador():
    print('-' * 70)

data = pd.read_excel('AAPL.xlsx', sheet_name='Hoja1')
dataIndexDate = data.set_index('timestamp')
dataResul = dataIndexDate[['volume']].copy()
dataResul['dif volume'] = dataResul['volume'] - (dataResul['volume'].shift(-1))
print(dataResul)
separador()