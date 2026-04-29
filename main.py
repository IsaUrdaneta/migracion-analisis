from src.limpieza import cargar_datos, limpiar_datos
from src.analisis import estadisticas_migracion, migrantes_por_razon, diferencia_idh
from src.visualizacion import (
    grafico_migrantes_por_razon,
    histograma_migrantes,
    scatter_pib_migrantes,
    boxplot_idh
)

def main():
    df = cargar_datos("data/raw/migracion.csv")

    df = limpiar_datos(df)

    stats = estadisticas_migracion(df)
    print("Estadísticas:", stats)

    resumen = migrantes_por_razon(df)
    print("\nMigrantes por razón:\n", resumen)

    df = diferencia_idh(df)

    #graficos
    grafico_migrantes_por_razon(df)
    histograma_migrantes(df)
    scatter_pib_migrantes(df)
    boxplot_idh(df)

    df.to_csv("data/processed/migracion_limpio.csv", index=False)

if __name__ == "__main__":
    main()