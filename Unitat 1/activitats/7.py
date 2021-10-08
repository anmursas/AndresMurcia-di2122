def funcio_externa():
    global a
    a = 20

    def funcio_interna():
        global a
        a = 30
        print("a =",a )
    
    funcio_interna()
    print("a =", a)

a = 10
funcio_externa()
print("a =", a)