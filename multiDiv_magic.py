v1 = (30, 40)
v2 = (10, 20)
m0 = v1[0].__mul__(v2[0])
m1 = v1[1].__mul__(v2[1])
d0 = v1[0].__truediv__(v2[0])
d1 = v1[1].__truediv__(v2[1])
print("v1 * v2 = ({}, {})\nv1 / v2 = ({}, {})".format(m0,m1,d0,d1))