def validacion(msj):
    while True:
        try:
            a = int(input(msj))
            return a
        except:
            print("Por favor ingrese solo valores numericos.....")
            
def validacion_STR(msj):
    while True:
        try:
            a = str(input(msj))
            return a
        except:
            print("Por favor ingrese solo valores alfabeticos.....")
            
def validacion_ISALNUM(msj):
    while True:
        a = input(msj)
        if a.isalnum()==True:
            return a
            break
        else: 
            print("Por favor ingrese solo valores alfanumericos.....")
            continue
        
def validacion_Float(msj):
    while True:
        try:
            a = float(input(msj))
            return a
        except:
            print("Por favor ingrese solo valores flotantes.....")

def opciones(option, Number_One, Number_two):
    if option<Number_One:
        print("Ingrese una opcion correcta.....")
    elif option>Number_two:
        print("Ingrese una opcion correcta.....")
        

