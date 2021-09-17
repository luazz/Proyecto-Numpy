import pandas as pd

def separador():
    print('-' * 70)

if __name__ == '__main__':
    data = pd.read_excel('AAPL.xlsx', sheet_name='Hoja1')
    dataIndexDate = data.set_index('timestamp')
    print(dataIndexDate.loc['2008-05-15'])
    separador()
    posteriores = dataIndexDate.loc['2008-05-15':'2020-03-06']
    print(posteriores.tail().iloc[2:5])
    separador()
    print(len(posteriores.loc[:'2011-08-21']))
    separador()
    ruedasMayores = dataIndexDate.loc['2011-08-20':'2008-05-15']
    ruedasMayores = ruedasMayores.loc[ruedasMayores['close'] > ruedasMayores['open']]
    print(len(ruedasMayores))
