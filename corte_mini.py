# corte_mini.py - mi primer programa

pesos = [20,21.5,22,20.8,21]
precio_kg = 29

num_cajas = len(pesos)
total_kg = sum(pesos)
promedio = total_kg / num_cajas
valor_total = total_kg * precio_kg

print ("Cajas: ", num_cajas)
print ("Total kg: ", total_kg)
print ("Promedio por caja: ", promedio)
print ("Valor total: $", valor_total)

meta = 20

if num_cajas >= meta:
	print ("¡Meta del día alcanzada!")
else:
	faltan = meta - num_cajas
	print ("Te faltan ", faltan," cajas para tu meta de ", meta)

