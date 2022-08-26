def numeroCheck():
    c = 0
    global n
    while c == 0:
        try: 
            n = int(input("Digite numero inteiro positivo: "))
            while n < 0:
                print("nao e positivo")
                n = int(input("Digite numero inteiro positivo: "))
            c = 1
        except:
            print("nao e numero ou inteiro")
numeroCheck()
if n%2 == 0:
    print("o numero e par")
else:
    print("o numero e impar")