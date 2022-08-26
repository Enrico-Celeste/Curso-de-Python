import math
def distancia(x1,y1,x2,y2):
    if(x1 > x2):
        if(y1 > y2):
            d = math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
        else:
            d = math.sqrt(math.pow(x1-x2,2)+math.pow(y2-y1,2))
    else:
        if(y1 > y2):
            d = math.sqrt(math.pow(x2-x1,2)+math.pow(y1-y2,2))
        else:
            d = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
    return d
x1 = int(input("digite o x do primeiro ponto: "))
y1 = int(input("digite o y do primeiro ponto: "))
x2 = int(input("digite o x do segundo ponto: "))
y2 = int(input("digite o y do segundo ponto: "))
print("distancia ", distancia(x1,y1,x2,y2))