def saludar():
    print("hola")


# Así se llama a la función
saludar()

def comprobar():
    n=int(input("dime un número")) #convertir el string a número
    if n>10:
        print("el número es alto")
    else:
        print("el número es bajo")

comprobar()

def llamar():
    nombre=input("Dime tu nombre ")
    print("hola "+nombre) #debo concatenar texto y variable

llamar()