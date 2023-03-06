while True:
        a = int(input("Digite o valor da inicial":))
        if a == 0:
            break

        soma = 0
        if a % 2 == 1:
            a += 1
        for i in range(a,a+10, 2):
            soma += i
        print(f"A soma dos 5 pares é..: {soma}")