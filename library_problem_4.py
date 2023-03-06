def resultado():
    def e_perfeito(n):
        soma = 0
        for i in range(1, a):
            if n % i == 0:
                soma += i
        return soma == a

    def testar_numeros_perfeitos():
        n = int(input("Digite quantos testes realizará:"))
        for i in range(1, a+1):
            x = int(input(f"Teste {i}:"))
            if e_perfeito(a):
                print(f"{a} é perfeito.")
            else:
                print(f"{a} não é perfeito.")

          testar_numeros_perfeitos()