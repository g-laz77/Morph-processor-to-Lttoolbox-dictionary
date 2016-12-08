#!/usr/bin/python
f = open("tagged")
a = f.readline()
b = a.split()
dis=[]
for i in b:
    j=i.split("/")
    if "NN" in j[1] and j[0] not in dis:
        dis.append(j[0])
        print j[0]




