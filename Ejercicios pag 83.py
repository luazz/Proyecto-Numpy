import pandas as pd

data = pd.read_excel('AAPL.xlsx', sheet_name='Hoja1')
dataIndexDate = data.set_index('timestamp')
dataResul = dataIndexDate[['volume']].copy()
dataResul['dif volume'] = dataResul['volume'] - (dataResul['volume'].shift(-1))