mi_var = [99, True, "una lista", [1, 2]]

mi_var2 = mi_var[::2]

mi_var = mi_var[::2]

print(mi_var)


mi_var.append("Elemento nuevo")
print(mi_var)
print(mi_var.count(99)) #cuantas veces aparece el num99

a = (2,3) #Tupla
mi_var.extend(a) #Pasa elementos de la tupla a la lista con extend


print(mi_var)


mi_var2.append("elemento nuevo")
alista = list(a)

for i in alista:
    mi_var2.append(i)

print(mi_var2)