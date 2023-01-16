import numpy as np
import pandas as pd
import datetime

def importar():
    clientes = []
    df = pd.read_excel('D:\Capstone\Zonas.xlsx', sheet_name = 'Hoja 1')
    df = df.drop_duplicates()
    df.reset_index(drop=True, inplace=True)
    df['Latitud'].replace('  ', np.nan, inplace=True)
    df['Longitud'].replace('  ', np.nan, inplace=True)
    df= df.dropna(subset=['Latitud'])
    df= df.dropna(subset=['Longitud'])
    df.reset_index(drop=True, inplace=True)

    df = df[['Codigo', 'Razon', 'Domicilio', 'Tipo', 'Dias', 'Sector', 'Latitud', 'Longitud', 'Zona']]
    df['Latitud'] = pd.to_numeric(df ['Latitud'])
    df['Longitud'] = pd.to_numeric(df ['Longitud'])

    df.duplicated(df.columns[~df.columns.isin(['Codigo'])])
    df.reset_index(drop=True, inplace=True)

    for i in range(len(df)):
        if df['Sector'][i] == datetime.datetime(2022, 5, 21, 0, 0):
            df['Sector'][i] = "21 Mayo"
        cliente = {}
        cliente['codigo'] = df['Codigo'][i]
        cliente['nombre'] = df['Razon'][i]
        cliente['direccion'] = df['Domicilio'][i]
        cliente['tipo'] = df['Tipo'][i]
        cliente['latitud'] = df['Latitud'][i]
        cliente['longitud'] = df['Longitud'][i]
        cliente['dias'] = df['Dias'][i]
        cliente['sector'] = df['Sector'][i]
        cliente['zona'] = df['Zona'][i]
        clientes.append(cliente)

    return clientes