import os
import matplotlib.pyplot as plt
import seaborn as sns

OUTPUT_DIR = "images"

def grafico_migrantes_por_razon(df):
    # Crear carpeta si no existe
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    plt.figure()
    df['Razon_Migracion'].value_counts().plot(kind='bar')
    plt.title("Migrantes por razón")
    plt.xlabel("Razón")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/grafico1.png")
    plt.close()


def histograma_migrantes(df):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    plt.figure()
    plt.hist(df['Cantidad_Migrantes'], bins=10)
    plt.title("Distribución de migrantes")
    plt.xlabel("Cantidad")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/grafico2.png")
    plt.close()


def scatter_pib_migrantes(df):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    plt.figure()
    plt.scatter(df['PIB_Destino'], df['Cantidad_Migrantes'])
    plt.title("PIB destino vs Migrantes")
    plt.xlabel("PIB destino")
    plt.ylabel("Migrantes")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/grafico3.png")
    plt.close()


def boxplot_idh(df):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    plt.figure()
    df[['IDH_Origen', 'IDH_Destino']].plot(kind='box')
    plt.title("Distribución IDH Origen vs Destino")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/grafico4.png")
    plt.close()