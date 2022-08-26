bidimensional = [[1, 2], [3, 4], [5, 6]]
unidimensional = []
for x in range(0,3):
    for y in range(0,2):
        n = bidimensional[x].pop(0)
        unidimensional.append(n)
print(unidimensional)  