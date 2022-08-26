for x in range(100, 1000):
    n1 = int(x/100)
    n2 = int((x-(n1*100))/10)
    n3 = x-(n1*100+n2*10)
    armstrong = (pow(n1, 3))+(pow(n2, 3))+(pow(n3, 3))
    if(armstrong == x):
        print(str(x) +" é um numero Armstrong")