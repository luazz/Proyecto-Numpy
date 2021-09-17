import yfinance as yf
import pandas as pd
# (data['Precio Finish'] <= ggal)  &
if __name__ == '__main__':
    ggal = 200
    data = pd.read_excel('Opciones GGAL.xlsx')
    data2 = data['Símbolo'].str.split('\n', n=1, expand=True)
    data2['Strike'] = data.Símbolo.str[4:7]
    data.columns = data.columns.str.replace('\n', ' ')
    data = data.drop(['Último Operado', 'Variación Diaria', 'Cantidad Compra', 'Cantidad Venta', 'Apertura', 'Mínimo',
                      'Máximo', 'Último Cierre', 'Monto Operado', 'Fecha/Hora'], axis=1)
    data['Símbolo'] = data2[0]
    data['Precio Finish'] = 0
    for i in range(47):
        data['Precio Finish'][i] = float(data['Precio Venta'][i]) + float(data2['Strike'][i])

    filtro = data[(data['Precio Venta'] != 0) & (data['Símbolo'].str[8:10] == 'OC')]
    filtro = filtro.sort_values(by='Precio Finish', ascending=True)
    print(filtro)