def line():
    A = float (input ("Ingerese el coeficiente A:"))
    B = float(input("Ingrese el coeficiente B:"))
    X1 = float(input("Ingrese el coeficiente X1:"))
    X2 = float(input("Ingrese el coeficiente X2:"))
    print (f"El coeficiente A de su ecuacion de la recta es:{A}")
    print (f"El coeficiente B de su ecuacion de la recta es:{B}")
    print (f"El coeficiente X1 de su ecuacion de la recta es:{X1}")
    print (f"El coeficiente X2 de su ecuacion de la recta es:{X2}")
    print ("\n")
    print ("para la siguiente ecuacion:")
    print (f"\tY = {A}X+{B}")
    print ("\n")
    print ("Dados los siguientes puntos:")

    Y1=A*X1+B
    Y2=A*X2+B
    print (f"\tP1({X1},{Y1})")
    print (f"\tP2({X2},{Y2})")
    print ("\n")
    distancia = ((X1-X2)**2+(Y1-Y2)**2)**(1/2)
    print (f"La distancia entre ellos es:{distancia}")
