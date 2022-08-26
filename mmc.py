n1o = n1 = int(input("\tDigite o primeiro numero inteiro positivo: "))
n2o = n2 = int(input("\tDigite o segundo numero inteiro positivo: "))
div = 2
mmc = 1
i = 0
while n1 != 1 or n2 != 1:
    if n1%div == 0:
        n1 = n1/div
        i += 1
    if n2%div == 0:
        n2 = n2/div
        i += 1
    if i > 0:
        mmc = mmc*div
    if n1%div != 0 and n2%div != 0:
        div += 1
    i = 0
print("mmc de {} e {} é: {}".format(n1o,n2o,mmc))