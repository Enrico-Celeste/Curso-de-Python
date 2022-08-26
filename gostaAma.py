s1 = ["Eu amo Panqueca.","Eu amo Suco de laranja.","Eu amo Café."]
s2 = ["Eu gosto de Panqueca.","Eu gosto de Suco de laranja.","Eu gosto de Café."]
for x in range(0, 6):
    if(x < 3):
        print(s1[x])
    else:
        print(s2[x-3])