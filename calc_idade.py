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