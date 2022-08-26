for x in range(2,13):
    #print("x: "+str(x))
    c = 0
    for y in range(x, 0, -1):
        #print("y: "+str(y))
        if(x % y == 0):
            c += 1
    if(c > 2):
        print(str(x)+" é composto")
    else:
        print(str(x)+" é primo")