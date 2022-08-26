maria = {'coreano': 94, 'ingles': 91, 'matematica': 89, 'ciencia': 83}
soma = maria.get('coreano')
soma += maria.get('ingles')
soma += maria.get('matematica')
soma += maria.get('ciencia')
print(soma/4)