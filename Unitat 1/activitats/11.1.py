f = open("./txts/prova.txt", 'r', encoding='utf-8')
mensaje = f.read()

print(mensaje)

with open("./txts/prova.txt", 'w', encoding='utf-8') as f:
    f.write("Primer arxiu\n")
    f.write("Este arxiu\n")
    f.write("conté tre línies\n")
    f.close()

x = open("./txts/prova.txt", 'r', encoding='utf-8')
x.read(6)
x.read(6)
x.read()
x.close()
