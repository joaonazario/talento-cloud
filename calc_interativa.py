
'''
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair.
No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela.
Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado.
'''

print('::: Calculator :::')
print ('\n 1: Soma \n 2: Subtração \n 3: Multiplicação \n 4: Divisão \n 0: Sair ')
escolha = int(input("Qual operação matemática você deseja realizar"))


if escolha == 0:
    print("Você escolheu sair.")

elif escolha == 1:
    print ("Você escolheu Soma")
    n1 = float(input("Digite o primeiro numero"))
    n2 = float(input('Digite o segundo numero'))
    soma = n1 + n2
    print (soma)

elif escolha == 2:
    print ("Você escolheu Subtração")
    n1 = float(input("Digite o primeiro numero"))
    n2 = float(input('Digite o segundo numero'))
    subtracao = n1 - n2
    print (subtracao)

elif escolha == 3:
    print ("Você escolheu Multiplicação")
    n1 = float(input("Digite o primeiro numero"))
    n2 = float(input('Digite o segundo numero'))
    multiplicacao = n1 * n2
    print (multiplicacao)

elif escolha == 4:
    print ("Você escolheu Divisão")
    n1 = float(input("Digite o primeiro numero"))
    n2 = float(input('Digite o segundo numero'))
    divisao = n1 / n2
    print (divisao)

else:
    print('Opção invalida')