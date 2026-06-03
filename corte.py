#corte.py - el corte convertido en función reutilizable

def calcular_corte (pesos, precio_kg=29):
	num_cajas = len (pesos)
	total_kg = sum(pesos)
	valor = total_kg * precio_kg
	return num_cajas, total_kg, valor


#Usamos (llamamos) la función con los pesos de hoy
pesos_hoy = [20,21.5,22.8,21]
cajas, kg, valor = calcular_corte(pesos_hoy)

print ("Cajas: ", cajas)
print ("Total kg", kg)
print("Valor: $ ", valor)



# Ahora varios días, reusando la MISMA función
semana = [
    [20, 21.5, 22, 20.8, 21],
    [19, 20, 22.5, 21],
    [23, 22, 20, 21, 20.5],
]

dia = 1
for pesos in semana:
    cajas, kg, valor = calcular_corte(pesos)
    print("Día", dia, "->", cajas, "cajas,", kg, "kg, $", valor)
    dia = dia + 1
