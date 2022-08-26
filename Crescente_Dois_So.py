def numeroCheck():
    c = 0
    global n1, n2
    while c == 0:
        try: 
            n1 = int(input("Digite o primeiro numero inteiro: "))
            n2 = int(input("Digite o segundo numero inteiro: "))
            while(n1 == n2):
                print("os numeros devem ser diferentes")
                n2 = int(input("Digite o segundo numero inteiro: "))
            c = 1
        except:
            print("nao e numero ou inteiro")
numeroCheck()
if(n1 > n2):
    print("em ordem crescente: {} {}".format(n2, n1))
else:
    print("em ordem crescente: {} {}".format(n1, n2))