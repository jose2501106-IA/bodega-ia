# corte.py — el corte como función reutilizable, con diccionarios

def calcular_corte(pesos, precio_kg=29):
    num_cajas = len(pesos)
    total_kg = sum(pesos)
    valor = total_kg * precio_kg
    return num_cajas, total_kg, valor

# Día 3: cada día es un diccionario con etiquetas (clave: valor)
semana = [
    {"dia": "Lunes",     "pesos": [20, 21.5, 22, 20.8, 21]},
    {"dia": "Martes",    "pesos": [19, 20, 22.5, 21]},
    {"dia": "Miércoles", "pesos": [23, 22, 20, 21, 20.5]},
]

for jornada in semana:
    cajas, kg, valor = calcular_corte(jornada["pesos"])
    print(jornada["dia"], "->", cajas, "cajas, $", valor)
