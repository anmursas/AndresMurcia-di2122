f = open("./txts/oper.txt", 'r', encoding='utf-8')

# Operaciones
suma = lambda var1, y: var1 + y
resta = lambda var1, y: var1 - y
multiplicacion = lambda var1, y: var1 * y
division = lambda var1, y: var1 / y

text = f.read()
x = text.strip()

# solo hay numeros
operands = []
op = ""

for c in x.split():
    if c.isdigit():
        operands.append(c)
    else:
        op = c

    if len(operands) == 2:
        if op == "+":
            res = suma(int(operands[0]), int(operands[1]))
            print(operands[0], "+", operands[1], "=", res)
        elif op == "-":
            res = resta(int(operands[0]), int(operands[1]))
            print(operands[0], "-", operands[1], "=", res)
        elif op == "*":
            res = multiplicacion(int(operands[0]), int(operands[1]))
            print(operands[0], "*", operands[1], "=", res)
        elif op == "/":
            res = division(int(operands[0]), int(operands[1]))
            print(operands[0], "/", operands[1], "=", res)
        operands.clear()

f.close()
