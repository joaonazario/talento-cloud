# Algoritmo para imprimir os andares de um predio (de menos o 13 andar,o dono é supersticioso .. rsrs)

print ('::: Mapa de Andares do Predio :::')

andardopredio = 21
for i in range (21,1,-1):
	andardopredio = andardopredio - 1
	
	if andardopredio == 13:
	    continue
	result  = str(andardopredio) + " Andar"
	print (result)
