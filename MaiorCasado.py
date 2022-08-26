def numeroCheck():
    c = 0
    global idade, casado
    while c == 0:
        try: 
            idade = int(input("Você é maior de idade? (digite 1 se sim, 0 se não): "))
            while(idade < 0 or idade > 1):
                idade = int(input("Você é maior de idade? (digite 1 se sim, 0 se não): "))
            casado = int(input("Você é casado(a)? (digite 1 se sim, 0 se não): "))
            while(casado < 0 or casado > 1):
                casado = int(input("Você é casado(a)? (digite 1 se sim, 0 se não): "))
            c = 1
        except:
            print("nao e numero ou inteiro")
numeroCheck()
if(idade == 1 and casado == 1):
    print("Você é maior de idade e casado.")
elif(idade == 1 and casado == 0):
    print("Você é maior de idade e solteiro.")
elif(idade == 0 and casado == 1):
    print("Você é menor de idade e casado.")
else:
    print("Você é menor de idade e solteiro.")
