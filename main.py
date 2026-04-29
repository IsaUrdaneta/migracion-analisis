import os
from src.limpieza import cargar_datos, limpiar_datos
from src.analisis import (
    estadisticas_migracion,
    migrantes_por_razon,
    diferencia_idh,
    generar_insights
)
from src.visualizacion import (
    grafico_migrantes_por_razon,
    histograma_migrantes,
    scatter_pib_migrantes,
    boxplot_idh
)


def main():
    OUTPUT_DIR = "images/graficos"
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 1. Cargar
    df = cargar_datos("data/raw/migracion.csv")

    # 2. Limpiar
    df = limpiar_datos(df)

    # 3. Feature engineering
    df = diferencia_idh(df)

    # 4. Estadísticas
    stats = estadisticas_migracion(df)

    # 5. Aggregaciones
    resumen_razon = migrantes_por_razon(df)

    # 6. Insights
    insights = generar_insights(df)

    # 7. Guardar outputs tabulares
    df.to_csv("data/processed/migracion_limpio.csv", index=False)
    resumen_razon.to_csv(f"{OUTPUT_DIR}/migrantes_por_razon.csv")

    # Guardar estadísticas
    with open(f"{OUTPUT_DIR}/estadisticas.txt", "w") as f:
        for k, v in stats.items():
            f.write(f"{k}: {v}\n")

    # Guardar insights
    with open(f"{OUTPUT_DIR}/insights.txt", "w", encoding="utf-8") as f:
        for ins in insights:
            f.write(f"- {ins}\n")

    # 8. Gráficos (guárdalos en outputs o images)
    grafico_migrantes_por_razon(df, OUTPUT_DIR)
    histograma_migrantes(df, OUTPUT_DIR)
    scatter_pib_migrantes(df, OUTPUT_DIR)
    boxplot_idh(df, OUTPUT_DIR)

    # 9. Consola (debug / visibilidad)
    print("\n📊 Estadísticas:")
    print(stats)

    print("\n📈 Migrantes por razón:")
    print(resumen_razon)

    print("\n🧠 Insights:")
    for ins in insights:
        print("-", ins)


if __name__ == "__main__":
    main()