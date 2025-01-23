def inicio(): #aqui se crea la variable de inicio
    saludo() #esta linea es la que ejecuta la funcion
    saludar("Luis",20)
    saludoPideNombre()
    suma(3,5)
    suma(56,34)
    sumarvarios(3,4,5,6,7,3,2,4,76)
    

def saludo(): #define la funcion
    print (f"Hola mundo")



def saludar(nombre,edad):
    print(f"Hola Mr.{nombre} que tienes {edad} años")



def saludoPideNombre():
    nombre=input("dame un nombre") #el input siempre para pedir parameros
    print (f"Hola Mr. {nombre}")



def suma(num1, num2):
    total = num1+num2
    return total #return para devolver algo en este caso el total




def sumarvarios(*args):
    print("Voy a sumar los numeros")

    for n in args:
        print(n)
    
    print(f"el total es :{total}")


def restar(num1,num2):
    diferencia = num1 - num2
    return diferencia
    total = restar (7,4)
    print(f"el resultado es {total}")

if __name__ == "__main__":
    
    inicio()#aqui empezaria el algoritmo
