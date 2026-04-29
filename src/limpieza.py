import pandas as pd

def cargar_datos(path):
    return pd.read_csv(path)


def eliminar_outliers_iqr(df, columna):
    q1 = df[columna].quantile(0.25)
    q3 = df[columna].quantile(0.75)
    iqr = q3 - q1

    li = q1 - 1.5 * iqr
    ls = q3 + 1.5 * iqr

    return df[(df[columna] >= li) & (df[columna] <= ls)]


def limpiar_datos(df):
    df = eliminar_outliers_iqr(df, 'IDH_Destino')

    df['Razon_Migracion'] = df['Razon_Migracion'].map({
        'Económica': 'Trabajo',
        'Conflicto': 'Guerra',
        'Educativa': 'Estudios'
    })

    return df