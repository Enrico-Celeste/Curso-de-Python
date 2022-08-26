def palindramo():
    palavra = input("digite uma palavra: ")
    if palavra == "":
        print("palavra invalida, digite novamente")
        palindramo()
    tamanho = len(palavra)
    inverso = ""
    for x in range(tamanho-1,-1,-1):
        inverso += palavra[x]
    return inverso, palavra
inverso, palavra = palindramo()
if(inverso == palavra):
    print("É palíndromo!")
else:
    print("Não é palíndromo!")