def numeroCheck():
    c = 0
    global trabalho, b1p1, b1p2, b2p1, b2p2, b3p1, b3p2, b4p1, b4p2
    while c >= 0 and c <= 3:
        try:
            if c == 0: 
                trabalho = float(input("\tDigite sua nota do trabalho: "))
                while trabalho < 0 or trabalho > 10:
                    print("\n\t\tnão é valido\n")
                    b1p1 = float(input("\tDigite sua nota do trabalho: "))
                print("\n\t\t*Digite as notas primeiro bimestre*\n")
                b1p1 = float(input("\tDigite sua primeira nota: "))
                while b1p1 < 0 or b1p1 > 10:
                    print("\n\t\tnão é valido\n")
                    b1p1 = float(input("\tDigite sua primeira nota: "))
                b1p2 = float(input("\tDigite sua segunda nota: "))
                while b1p2 < 0 or b1p2 > 10:
                    print("\n\t\tnão é valido\n")
                    b1p2 = float(input("\tDigite sua segunda nota: "))
                c += 1
            elif c == 1:
                print("\n\t\t*Digite as notas segundo bimestre*\n")
                b2p1 = float(input("\tDigite sua primeira nota: "))
                while b2p1 < 0 or b2p1 > 10:
                    print("\n\t\tnão é valido\n")
                    b2p1 = float(input("\tDigite sua primeira nota: "))
                b2p2 = float(input("\tDigite sua segunda nota: "))
                while b2p2 < 0 or b2p2 > 10:
                    print("\n\t\tnão é valido\n")
                    b2p2 = float(input("\tDigite sua segunda nota: "))
                c += 1
            elif c == 2:
                print("\n\t\tDigite as notas terceiro bimestre\n")
                b3p1 = float(input("\tDigite sua primeira nota: "))
                while b3p1 < 0 or b3p1 > 10:
                    print("\n\t\tnão é valido\n")
                    b3p1 = float(input("\tDigite sua primeira nota: "))
                b3p2 = float(input("\tDigite sua segunda nota: "))
                while b3p2 < 0 or b3p2 > 10:
                    print("\n\t\tnão é valido\n")
                    b3p2 = float(input("\tDigite sua segunda nota: "))
                c += 1
            else:
                print("\n\t\tDigite as notas quarto bimestre\n")
                b4p1 = float(input("\tDigite sua primeira nota: "))
                while b4p1 < 0 or b4p1 > 10:
                    print("\n\t\tnão é valido\n")
                    b4p1 = float(input("\tDigite sua primeira nota: "))
                b4p2 = float(input("\tDigite sua segunda nota: "))
                while b4p2 < 0 or b4p2 > 10:
                    print("\n\t\tnão é valido\n")
                    b4p2 = float(input("\tDigite sua segunda nota: "))
                c += 1
        except:
            print("alguma das notas foi digitada errada, digite-as novamente do bimestre que parou")
nome = input("\tDigite seu nome: ")
numeroCheck()
mb1 = (b1p1+b1p2+trabalho)/3 
mb2 = (b2p1+b2p2+trabalho)/3
mb3 = (b3p1+b3p2+trabalho)/3
mb4 = (b4p1+b4p2+trabalho)/3
mtt = (mb1+mb2+mb3+mb4)/4
print("\n\n\tNotas do Aluno: "+ nome +"\n\t\tPrimeiro Semestre:\n\t\t\tNota 1: "+ str(b1p1))
print("\t\t\tNota 2: "+ str(b1p2) +"\n\t\t\ttrabalho: "+ str(trabalho) +"\n\t\t\tmedia: {0:.2f}".format(mb1))
print("\t\tSegundo Semestre:\n\t\t\tNota 1: "+ str(b2p1))
print("\t\t\tNota 2: "+ str(b2p2) +"\n\t\t\ttrabalho: "+ str(trabalho) +"\n\t\t\tmedia: {0:.2f}".format(mb2))
print("\t\tTerceiro Semestre:\n\t\t\tNota 1: "+ str(b3p1))
print("\t\t\tNota 2: "+ str(b3p2) +"\n\t\t\ttrabalho: "+ str(trabalho) +"\n\t\t\tmedia: {0:.2f}".format(mb3))
print("\t\tQuarto Semestre:\n\t\t\tNota 1: "+ str(b4p1))
print("\t\t\tNota 2: "+ str(b4p2) +"\n\t\t\ttrabalho: "+ str(trabalho) +"\n\t\t\tmedia: {0:.2f}".format(mb4))
if(mtt < 4):
    print("\t\tmedia total: {0:.2f}".format(mtt) +" (REPROVADO)")
elif(mtt >= 4 and mtt < 6):
    print("\t\tmedia total: {0:.2f}".format(mtt) +" (RECUPERAÇÃO)")
else:
    print("\t\tmedia total: {0:.2f}".format(mtt) +" (APROVADO)")