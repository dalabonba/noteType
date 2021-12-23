# -*- coding: utf-8 -*--
"""
Created on Sat Dec 18 17:09:58 2021

@author: upup5
"""

def changeV(vv):
    vv.pop()

v=[1,2,3,4,5]
print(f"1未改{v}")
changeV(v)
print(f"1改{v}","\n")


print(f"2未改{v}")
changeV(v[:])
print(f"2改{v}")