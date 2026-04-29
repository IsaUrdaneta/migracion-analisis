def estadisticas_migracion(df):
    return {
        "media": df['Cantidad_Migrantes'].mean(),
        "mediana": df['Cantidad_Migrantes'].median()
    }


def migrantes_por_razon(df):
    return df.groupby('Razon_Migracion')['Cantidad_Migrantes'].sum()


def diferencia_idh(df):
    df['Diferencia_IDH'] = df['IDH_Origen'] - df['IDH_Destino']
    return df