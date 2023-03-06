a = int(input("Digite o valor 1: "))
b = int(input("Digite o valor de 2:"))

if a > b:
    a, b = b, a
numeros = []
for i in range (a + 1,b)
    if i % 5 == 2 or i % 5 == 3:
      numeros.oppend(i)

print("Os números são..:{}".format("".join(str(n)for n in numeros)))