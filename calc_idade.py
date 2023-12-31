'''
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022). 
Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
'''

while True:
        nome_completo = input("Digite seu nome completo: ")

        try:
            ano_nascimento = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                idade = 2022 - ano_nascimento
                print(f"Nome: {nome_completo}")
                print(f"Idade em 2022: {idade} anos")
                break
            else:
                print("Ano de nascimento fora do intervalo permitido.")
        except ValueError:
            print("Por favor, digite um ano válido.")
