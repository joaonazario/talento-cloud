''' 
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada.
Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

'''

def calc_user (n1, n2, simbol) :
    if simbol == 1:
        calculadora = n1 + n2
        return calculadora
    
    elif simbol == 2:
        calculadora = n1 - n2
        return calculadora
    
    elif simbol == 3:
        calculadora = n1 * n2
        return calculadora

    elif simbol == 4:
        calculadora = n1 / n2
        return calculadora

    else:
        calculadora = 0
        return calculadora

result = calc_user (3,3,3)
print(result)
    
    

