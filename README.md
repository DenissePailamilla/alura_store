
# Desafío Alura Store — Análisis de Tiendas

**Objetivo:** ayudar al Sr. Juan a decidir qué tienda vender, analizando 4 tiendas de Alura Store con Python (Pandas + Matplotlib).

## Métricas a evaluar
- Facturación total por tienda.
- Categorías más vendidas por tienda.
- Promedio de evaluación de clientes.
- Productos más y menos vendidos por tienda.
- Costo promedio de envío por tienda.

> Requisito de visualización: **mínimo 3 gráficos** (barras, circular, dispersión u otros).

## Estructura del proyecto
```
.
├── data/          # Datos (CSV u otros) - provistos por el cuaderno base
├── figs/          # Gráficos exportados (PNG/JPG)
├── notebooks/     # Jupyter/Colab notebooks
├── src/           # Funciones auxiliares (opcional)
├── requirements.txt
├── README.md
└── .gitignore
```

## Cómo ejecutar
1. Abrir el cuaderno base en **Google Colab** (proporcionado por el desafío).
2. Asegurar dependencias mínimas:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar secciones:
   - A1: Facturación total por tienda
   - A2: Categorías más vendidas
   - A3: Promedio de evaluación
   - A4: Productos TOP/BOTTOM por tienda
   - A5: Costo de envío promedio por tienda
4. Exportar al final **conclusiones y recomendación** (¿qué tienda vender y por qué?).

## Guía de visualizaciones (sugerencias)
- Barras comparativas por tienda para facturación.
- Barras apiladas o ranking por categorías.
- Barras horizontales para ratings promedio.
- Tablas/gráficos para TOP/BOTTOM productos.
- Barras para costo de envío promedio.

## Resultado esperado
- Un notebook con análisis + gráficos.
- Una sección final con la **recomendación** para el Sr. Juan.
- Este repositorio actualizado con el notebook y recursos.

## Cómo versionar con Git/GitHub
```bash
# Dentro de la carpeta del proyecto
git init
git branch -M main
git remote add origin <URL-de-tu-repo>
git add .
git commit -m "feat: scaffold inicial Alura Store"
git push -u origin main
```

Para nuevos cambios:
```bash
git pull origin main
git add -A
git commit -m "feat: analisis A1-A3 con graficos"
git push
```

## Notas
- Mantén los gráficos exportados en `figs/` si los usas en el README.
- No subas datos sensibles.
- Puedes crear un `src/utils.py` para funciones reutilizables de análisis y gráficos.
