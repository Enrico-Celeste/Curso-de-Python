notas = [['Davi',  88,  95, 90], ['Felipe', 83, 98, 81], ['Luciano', 81, 97, 98], ['Rodrigo', 82, 89, 83]]
media = 0
for x in range(0,3):
    media += notas[x].pop(2)
print(media/4)