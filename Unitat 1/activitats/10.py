def par(num):
    return not num%2

def impar(num):
    return num%2
llista = range(101)

llistapar = list(filter(par,llista))
llistaimpar = list(filter(impar,llista))

print(llistapar)
print(llistaimpar)