import Funciones as fs
import pandas as pd

def separador():
    print('-' * 70)

if __name__ == '__main__':
    data = pd.read_excel('AAPL.xlsx', sheet_name='Hoja1')
    data_index_date = data.set_index('timestamp')
    print(data_index_date.loc['2008-05-15'])
    separador()
    posteriores = data_index_date.loc['2008-05-15':'2020-03-06']
    print(posteriores.tail().iloc[2:5])
    separador()
    print(len(posteriores.loc[:'2011-08-21']))
    separador()
    ruedas_mayores = data_index_date.loc['2011-08-20':'2008-05-15']
    ruedas_mayores = ruedas_mayores.loc[ruedas_mayores['close']>ruedas_mayores['open']]
    print(len(ruedas_mayores))
