def saluda(nom="desconegut", msg="Benvingut!"):
    
    print("Hola ", nom + "-", msg)

saluda("Tomàs", "Qué fas?")
saluda("Pau")
saluda()
saluda(msg="", nom="Artur")