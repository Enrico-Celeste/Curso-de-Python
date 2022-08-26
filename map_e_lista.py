def x2x3(x):
    return x*2,x*3
n_list = [10, 20, 30]
x = map(x2x3, n_list)
print(list(x))