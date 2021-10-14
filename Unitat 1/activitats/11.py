# Crea una aplicacion que vaya leyendo operaciones de un fichero
# (una operación por línea) y muestre los resultados, por ejemplo
# si lee 4 + 4 deberá mostrar 4 + 4 = 8

f = open("./txts/oper.txt", 'r', encoding='utf-8')

suma = lambda var1, y: var1 + y
text = f.read()
x = text.split()
print(x)
print(x[0])


for c in x:
    op1 = 0

if x[1] == "+":
    print(suma(int(x[0]), int(x[2])))

f.close()
