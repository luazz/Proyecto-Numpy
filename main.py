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
    posteriores