
import pandas as pd
import matplotlib.pyplot as plt

def check_cols(df, required, name="df"):
    missing = [c for c in required if c not in df.columns]
    if missing:
        print(f"[WARN] {name} faltan columnas: {missing}")
    else:
        print(f"[OK] {name} columnas correctas.")

def revenue_by_store(df):
    check_cols(df, ['tienda','precio','cantidad'], "ventas")
    agg = df.assign(ingreso = df['precio']*df['cantidad'])             .groupby('tienda', as_index=False)['ingreso'].sum()             .sort_values('ingreso', ascending=False)
    return agg

def plot_bar(df, x, y, title, rot=0):
    plt.figure()
    plt.bar(df[x], df[y])
    plt.title(title)
    plt.xticks(rotation=rot)
    plt.ylabel(y)
    plt.xlabel(x)
    plt.show()
