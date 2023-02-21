from math import *
def laukums_rinkis(r):
    return pi*(r*2)
r1=float(input("ievadi pirma rinka radiusu, cm - "))
r2=float(input("ievadi otra rinka radiusu, cm - "))
s1=laukums_rinkis(r1)
s2=laukums_rinkis(r2)
print("S1 = ",round(s1,2),"cm2")
print("S2 = ",round(s2,2), "cm2")