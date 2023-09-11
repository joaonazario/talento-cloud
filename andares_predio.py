'''
Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13o andar.

Escreva um código que imprima todos os números exceto o número 13.
Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.

'''

# Algoritmo para imprimir os andares de um predio (de menos o 13 andar,o dono é supersticioso .. rsrs)

print ('::: Mapa de Andares do Predio :::')

andardopredio = 21
for i in range (21,1,-1):
	andardopredio = andardopredio - 1
	
	if andardopredio == 13:
	    continue
	result  = str(andardopredio) + " Andar"
	print (result)