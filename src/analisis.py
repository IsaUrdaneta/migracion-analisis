# 1. Imports
import pandas as pd

# 2. Funciones base (helpers)
def top_categorias(df, col, n=5):
    conteo = df[col].value_counts(dropna=False)
    pct = conteo / conteo.sum() * 100
    out = pd.DataFrame({
        col: conteo.index,
        "conteo": conteo.values,
        "pct": pct.values
    }).head(n)
    return out

def distribucion(df, col):
    conteo = df[col].value_counts(dropna=False)
    pct = conteo / conteo.sum() * 100
    return pd.DataFrame({"conteo": conteo, "pct": pct})

def cruces(df, col_a, col_b):
    tabla = pd.crosstab(df[col_a], df[col_b], normalize="index") * 100
    return tabla.round(2)

def calidad_datos(df):
    nulos = df.isna().mean().sort_values(ascending=False) * 100
    unicos = df.nunique().sort_values(ascending=False)
    return pd.DataFrame({"pct_nulos": nulos.round(2), "n_unicos": unicos})

# 3. Funciones de negocio (análisis)
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

# 4. Insights (usan funciones anteriores)
def generar_insights(df):
    insights = []

    top_razones = top_categorias(df, "Razon_Migracion", n=3)
    r1 = top_razones.iloc[0]

    insights.append(
        f"La principal razón de migración es '{r1['Razon_Migracion']}' con {r1['pct']:.1f}%."
    )

    acum = top_razones["pct"].sum()
    insights.append(
        f"Las tres principales razones concentran el {acum:.1f}% del total."
    )

    top_paises = top_categorias(df, "Pais_Origen", n=3)
    p1 = top_paises.iloc[0]

    insights.append(
        f"El país con mayor migración es '{p1['Pais_Origen']}' con {p1['pct']:.1f}%."
    )

    tabla = cruces(df, "Pais_Origen", "Razon_Migracion")

    if not tabla.empty:
        fila = tabla.iloc[0]
        col_dominante = fila.idxmax()
        val = fila.max()

        insights.append(
            f"En '{tabla.index[0]}', predomina '{col_dominante}' con {val:.1f}%."
        )

    return insights