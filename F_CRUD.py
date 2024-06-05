import xml.etree.ElementTree as ET
import os
from Validaciones import *
import mysql.connector
directorio = os.getcwd()
Espacio = "____________________________________________________________________"

def I_User(Nom, Id, Key, Root, tree):
    """Crea un nuevo Usuario Administrador en el archvio Users.xml"""
    usser3 = ET.SubElement(Root, "Usuario")
    usser3.set("ID", Id)
    usser3.set("Clave", Key)
    name3 = ET.SubElement(usser3, "Nombre")
    name3.text=Nom
    tree = ET.ElementTree(Root)
    ET.indent(tree)
    tree.write(f"{directorio}/admin/Users.xml", encoding="UTF-8")
    
def V_User(Mensaje, Lista_Key, lista):
    """Permite visualizar el usuario administrador que se filtra por la clave"""
    ver = validacion_ISALNUM(Mensaje)
    print(Espacio)
    if ver in Lista_Key:
        for b in lista:
            Ver_val = b.get(ver)
            if Ver_val!=None:
                print(f"""
                      \nNombre: {Ver_val[0]}
                      \nNumero de Identificacion: {Ver_val[1]}
                      \nContraseña: {ver}""")
        print(Espacio)
    else:
        print("La contraseña ingresada no se encuentra en el sistema.....")
        print(Espacio)
        
def A_User(Mensaje1, Lista_CC, Root, Tree, principal, Actualizar):
    """Actualiza los datos del usuario administrador deseado"""
    Actu = input(Mensaje1)
    if Actu in Lista_CC:
        Finalizar=0
        while Finalizar!=1:
            Actu_menu = validacion("""¿Que desea modificar de este administrador?
                                   1- Nombre
                                   2- Numero de Identificacion
                                   3- Cancelar
                                   \n""")
            print(Espacio)
            opciones(Actu_menu, 1, 3)
            if Actu_menu==1:
                New_N = validacion_STR("Ingrese el nombre nuevo: ")
                for Ac in Root.findall("Usuario"):
                    if Ac.get("ID")==Actu:
                        Ac.find("Nombre").text = New_N
                        Tree.write(f"{directorio}/admin/Users.xml")
                        Finalizar+=1
            elif Actu_menu==2:
                New_I = input("Ingrese el numero de identificacion nuevo: ")
                for Ac_I in Root.findall("Usuario"):
                    if Ac_I.get("ID")==Actu:
                        Ac_I.set("ID", New_I)
                        Tree.write(f"{directorio}/admin/Users.xml")
                        Info = validacion("""¿Desea actualizar los cambios ahora?
                                          1- SI
                                          2- NO
                                          \n""")
                        print(Espacio)
                        opciones(Info, 1, 2)
                        if Info==1:
                            Finalizar+=1
                            principal+=3
                            Actualizar+=1
                        else:
                            Finalizar+=1
            elif Actu_menu==3:
                break
    else:
        print("El numero de identificacion ingresado no se encuntra en el sistema")
        print(Espacio)
        
def E_User(Mensaje, Lista_CC, Root, Tree):
    """Elimina el usuario administrador filtrado por el ID"""
    Eliminar = input(Mensaje)
    if Eliminar in Lista_CC:
        for ced in Root.findall("Usuario"):
            if ced.get("ID")==Eliminar:
                Root.remove(ced)
                Tree.write(f"{directorio}/admin/Users.xml")
    else:
        print("El numero de identificacion ingresado no se encuntra en el sistema")
        print(Espacio)
        
def Ingresar_Responsable(conexion2):
    """Ingresa un nuevo Responsable en la tabla; "responsables" perteneciente a la base de datos; "informatica_pf" """
    conexion2 = mysql.connector.connect(user="root", password="", host="localhost", database="informatica1_pf")
    Cursor2 = conexion2.cursor()
    Cod_Resp = input("Código responsable: ") 
    Contr = input("Contraseña: ") 
    Ape = input("Apellido: ") 
    Nom = input("Nombre: ") 
    N_ID = input("Número del documento de identidad: ") 
    Car = input("Cargo: ") 
    Ingreso_Datos = """INSERT INTO responsables(Codigo_Responsanble, Contraseña, Apellido, Nombre, Numero_Documento_Identidad, Cargo) VALUES (%s,%s,%s,%s,%s,%s)"""
    Cursor2.execute(Ingreso_Datos, (Cod_Resp, Contr, Ape, Nom, N_ID, Car))
    conexion2.commit()
    conexion2.close()
    
def Ver_Responsable(conexion3):
    """Permite ver el responsable de prueba filtrado por la cedula"""
    conexion3 = mysql.connector.connect(user="root", password="", host="localhost", database="informatica1_pf")
    Cursor3 = conexion3.cursor()
    Consul_ID = validacion("Ingrese la cedula del responsable: ")
    print(Espacio)
    sql = "SELECT * FROM responsables WHERE Numero_Documento_Identidad=%s" %Consul_ID
    Cursor3.execute(sql)
    resultado = Cursor3.fetchall()
    Datos = []
    for lr in resultado:
        for D in lr:
            Datos.append(D)
    if Consul_ID in Datos:
        for r in resultado:
            print(f"""
                  Codigo: {r[0]}
                  Contraseña: {r[1]}
                  Apellido: {r[2]}
                  Nombre: {r[3]}
                  Numero de Identificacion: {r[4]}
                  Cargo: {r[5]}""")
        print(Espacio)
    else:
        print("La Cedula ingresada no se encuntra en el sistema...")
        print(Espacio)
    Cursor3.close()
    conexion3.close()
    
def Actualizar_Todo(conexion3):
    """Permite actualizar la informacion del responsable filtrado por la cedula"""
    conexion3 = mysql.connector.connect(user="root", password="", host="localhost", database="informatica1_pf")
    Cursor3 = conexion3.cursor()
    Consul_ID = validacion("Ingrese la cedula del responsable: ")
    print(Espacio)
    sql = "SELECT * FROM responsables WHERE Numero_Documento_Identidad=%s" %Consul_ID
    Cursor3.execute(sql)
    resultado = Cursor3.fetchall()
    Datos = []
    for lr in resultado:
        for D in lr:
            Datos.append(D)
    if Consul_ID in Datos:
        while True:
            Mod = validacion("""¿Que desea modificar?
                             1- Codigo
                             2- Contraseña
                             3- Apellido
                             4- Nombre
                             5- Numero de Identificacion
                             6- Cargo
                             \n""")
            print(Espacio)
            opciones(Mod, 1, 6)
            if Mod==1:
                N_C = validacion("Ingrese un nuevo codigo: ")
                print(Espacio)
                sql2 = f"""UPDATE responsables SET Codigo_Responsanble = {N_C} WHERE Numero_Documento_Identidad = {Consul_ID}"""
                Cursor3.execute(sql2)
                conexion3.commit()
                break
            elif Mod==2:
                N_Con = validacion_ISALNUM("Ingrese una nueva contraseña: ")
                print(Espacio)
                sql2 = f"""UPDATE responsables SET Contraseña = "{N_Con}" WHERE Numero_Documento_Identidad = {Consul_ID}"""
                Cursor3.execute(sql2)
                conexion3.commit()
                break
            elif Mod==3:
                N_A = validacion_STR("Ingrese un nuevo apellido: ")
                print(Espacio)
                sql2 = f"""UPDATE responsables SET Apellido = "{N_A}" WHERE Numero_Documento_Identidad = {Consul_ID}"""
                Cursor3.execute(sql2)
                conexion3.commit()
                break
            elif Mod==4:
                N_Nom = validacion_STR("Ingrese un nuevo nombre: ")
                print(Espacio)
                sql2 = f"""UPDATE responsables SET Nombre = "{N_Nom}" WHERE Numero_Documento_Identidad = {Consul_ID}"""
                Cursor3.execute(sql2)
                conexion3.commit()
                break
            elif Mod==5:
                N_CC = validacion("Ingrese un nuevo numero de identificacion: ")
                print(Espacio)
                sql2 = f"""UPDATE responsables SET Numero_Documento_Identidad = {N_CC} WHERE Numero_Documento_Identidad = {Consul_ID}"""
                Cursor3.execute(sql2)
                conexion3.commit()
                break
            elif Mod==6:
                N_Car = validacion_STR("Ingrese un nuevo cargo: ")
                print(Espacio)
                sql2 = f"""UPDATE responsables SET Cargo = "{N_Car}" WHERE Numero_Documento_Identidad = {Consul_ID}"""
                Cursor3.execute(sql2)
                conexion3.commit()
                break
    else:
        print("La Cedula ingresada no se encuntra en el sistema...")
        print(Espacio)
    Cursor3.close()
    conexion3.close()
    
def Eliminar(Mensaje1, Mensaje2, responsables, Numero_Documento_Identidad):
    """Permite eliminar un objeto en especifico de una tabla en especifico filtrado por el elemento ingresado y la tabla ingresada respectivamente"""
    conexion3 = mysql.connector.connect(user="root", password="", host="localhost", database="informatica1_pf")
    Cursor3 = conexion3.cursor()
    Borrar = validacion(Mensaje1)
    print(Espacio)
    sql = f"SELECT * FROM {responsables} WHERE {Numero_Documento_Identidad}=%s" %Borrar
    Cursor3.execute(sql)
    resultado = Cursor3.fetchall()
    Datos = []
    for lr in resultado:
        for D in lr:
            Datos.append(D)
    if Borrar in Datos:
        Seg = validacion("""¿Esta seguro de querer realizar la eliminacion?
                         1- SI
                         2- NO
                         \n""")
        print(Espacio)
        opciones(Seg, 1, 2)
        if Seg==1:
            sql1 = f"""DELETE FROM {responsables} WHERE {Numero_Documento_Identidad} = {Borrar}"""
            Cursor3.execute(sql1)
            conexion3.commit()
            print("La Eliminacion ha sido realizada con exito")
            print(Espacio)
    else:
        print(Mensaje2)
        print(Espacio)
    Cursor3.close()
    conexion3.close()

def Actualizar_Responsable(Mensaje1, Mensaje2, Modificar):
    """Permite actualizar la informacion de un responsable de prueba filtrado por su identificacion"""
    conexionF = mysql.connector.connect(user="root", password="", host="localhost", database="informatica1_pf")
    CursorF = conexionF.cursor()
    Consul_ID = validacion(Mensaje1)
    print(Espacio)
    sql = "SELECT * FROM responsables WHERE Numero_Documento_Identidad=%s" %Consul_ID
    CursorF.execute(sql)
    resultado = CursorF.fetchall()
    Datos = []
    for lr in resultado:
        for D in lr:
            Datos.append(D)
    if Consul_ID in Datos:
        New_F = validacion(Mensaje2)
        print(Espacio)
        sqlF = f"""UPDATE responsables SET {Modificar} = {New_F} WHERE Numero_Documento_Identidad = {Consul_ID}"""
        CursorF.execute(sqlF)
        conexionF.commit()
        conexionF.close()
    else:
        print("La Cedula ingresada no se encuntra en el sistema...")
        print(Espacio)
        
def Ingresar_Prueba(conexion2):
    """Permite ingresar un nuevo resultado de prueba en la tabla; "pruebas" perteneciente a la base de datos; "informatica1_pf" """
    conexion2 = mysql.connector.connect(user="root", password="", host="localhost", database="informatica1_pf")
    Cursor2 = conexion2.cursor()
    Se_Pr = input("Serial de la probeta: ")
    No_Ma = input("Nombre del material: ")
    Re_Tr = input("Resultado de ensayo de tracción: ") 
    Re_Du = input("Resultado prueba de dureza: ")
    Re_He = validacion("Resultado prueba de hemocompatibilidad: \n1- Para SI \n2- Para NO")
    opciones(Re_He, 1, 2)
    if Re_He==1:
        Re_He1="SI"
    else:
        Re_He1="NO"
    Re_In = validacion("Resultado prueba de inflamabilidad: \n1- Para SI \n2-Para NO")
    opciones(Re_In, 1, 2)
    if Re_In==1:
        Re_In1="SI"
    else:
        Re_In1="NO"
    Re_De = input("Resultado densidad: ")
    Re_Fu = input("Resultado temperatura de fusión: ")
    Fe_Re = input("Fecha de realización: ")
    Co_Re = input("Código responsable: ") 
    Ingreso_Datos = """INSERT INTO pruebas (Serial_Probeta, Nombre_Material, Resultado_Ensayo_Deformacion, Resultado_Dureza, Resultado_Hemocompatibilidad, 
    Resultado_Inflamabilidad, Resultado_Densidad, Resultado_Temperatura_Fusion, Fecha_Realizacion, Codigo_Responsable) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    Cursor2.execute(Ingreso_Datos, (Se_Pr,No_Ma,Re_Tr,Re_Du,Re_He1,Re_In1,Re_De,Re_Fu,Fe_Re,Co_Re))
    conexion2.commit()
    conexion2.close()
    
def Actualizar_Prueba(conexion3):
    """Permite actualizar la informacion de un resultado de prueba filtrado por el serial de la probeta"""
    conexion3 = mysql.connector.connect(user="root", password="", host="localhost", database="informatica1_pf")
    Cursor3 = conexion3.cursor()
    Consul_SR = validacion("Ingrese el nunmero de serie de la probeta correspondiente a la prueba: ")
    print(Espacio)
    sql = "SELECT * FROM pruebas WHERE Serial_Probeta=%s" %Consul_SR
    Cursor3.execute(sql)
    resultado = Cursor3.fetchall()
    Datos = []
    for lr in resultado:
        for D in lr:
            Datos.append(D)
    if Consul_SR in Datos:
        while True:
            Mod = validacion("""¿Que desea modificar?
                             1- Serial de la probeta
                             2- Nombre del material
                             3- Resultado de ensayo de tracción [Deformación]
                             4- Resultado prueba de dureza
                             5- Resultado prueba de hemocompatibilidad
                             6- Resultado prueba de inflamabilidad
                             7- Resultado densidad
                             8- Resultado temperatura de fusión
                             9- Fecha de realización
                             10- Código responsable
                             \n""")
            print(Espacio)
            opciones(Mod, 1, 10)
            if Mod==1:
                S_P = validacion("Ingrese un nuevo serial de la probeta: ")
                print(Espacio)
                sql2 = f"""UPDATE pruebas SET Serial_Probeta = {S_P} WHERE Serial_Probeta = {Consul_SR}"""
                Cursor3.execute(sql2)
                conexion3.commit()
                break
            elif Mod==2:
                N_M = validacion_STR("Ingrese un nuevo nombre del material: ")
                print(Espacio)
                sql2 = f"""UPDATE pruebas SET Nombre_Meterial = "{N_M}" WHERE Serial_Probeta = {Consul_SR}"""
                Cursor3.execute(sql2)
                conexion3.commit()
                break
            elif Mod==3:
                R_T = validacion_Float("Ingrese un nuevo valor para el resultado de ensayo de traccion: ")
                print(Espacio)
                sql2 = f"""UPDATE pruebas SET Resultado_Ensayo_Deformacion = "{R_T}" WHERE Serial_Probeta = {Consul_SR}"""
                Cursor3.execute(sql2)
                conexion3.commit()
                break
            elif Mod==4:
                R_D = validacion("Ingrese un nuevo resultado para prueba de dureza: ")
                print(Espacio)
                sql2 = f"""UPDATE pruebas SET Resultado_Dureza = "{R_D}" WHERE Serial_Probeta = {Consul_SR}"""
                Cursor3.execute(sql2)
                conexion3.commit()
                break
            elif Mod==5:
                R_H = validacion("Ingrese nuevo resultado de prueba de hemocompatibilidad: \n1- Para SI \n2- Para NO")
                print(Espacio)
                opciones(R_H, 1, 2)
                if R_H==1:
                    R_H1="SI"
                else:
                    R_H1="NO"
                sql2 = f"""UPDATE pruebas SET Resultado_Hemocompatibilidad = "{R_H1}" WHERE Serial_Probeta = {Consul_SR}"""
                Cursor3.execute(sql2)
                conexion3.commit()
                break
            elif Mod==6:
                R_I = validacion("Ingrese nuevo resultado de prueba de inflamabilidad: \n1- Para SI \n2- Para NO")
                print(Espacio)
                opciones(R_I, 1, 2)
                if R_I==1:
                    R_I1="SI"
                else:
                    R_I1="NO"
                sql2 = f"""UPDATE pruebas SET Resultado_Inflamabilidad = "{R_I1}" WHERE Serial_Probeta = {Consul_SR}"""
                Cursor3.execute(sql2)
                conexion3.commit()
                break
            elif Mod==7:
                R_De = validacion_Float("Ingrese nuevo resultado de densidad: ")
                print(Espacio)
                sql2 = f"""UPDATE pruebas SET Resultado_Densidad = "{R_De}" WHERE Serial_Probeta = {Consul_SR}"""
                Cursor3.execute(sql2)
                conexion3.commit()
                break
            elif Mod==8:
                R_TF = validacion("Ingrese nuevo resultado de temperatura de fusion: ")
                print(Espacio)
                sql2 = f"""UPDATE pruebas SET Resultado_Temperatura_Fusion = "{R_TF}" WHERE Serial_Probeta = {Consul_SR}"""
                Cursor3.execute(sql2)
                conexion3.commit()
                break
            elif Mod==9:
                F_R = validacion_ISALNUM("Ingrese una nueva fecha de realizacion: ")
                print(Espacio)
                sql2 = f"""UPDATE pruebas SET Fecha_Realizacion = "{F_R}" WHERE Serial_Probeta = {Consul_SR}"""
                Cursor3.execute(sql2)
                conexion3.commit()
                break
            elif Mod==10:
                C_R = validacion("Ingrese un nuevo codigo responsable: ")
                print(Espacio)
                sql2 = f"""UPDATE pruebas SET Codigo_Responsable = "{C_R}" WHERE Serial_Probeta = {Consul_SR}"""
                Cursor3.execute(sql2)
                conexion3.commit()
                break
    else:
        print("La Cedula ingresada no se encuntra en el sistema...")
        print(Espacio)
    Cursor3.close()
    conexion3.close()
    
def Ver_Prueba(Mensaje1, Mensaje2, Serial_Probeta):
    """Permite ver los resultados de una o mas pruebas filtrado por el serial de probeta o el codigo responsable"""
    conexion3 = mysql.connector.connect(user="root", password="", host="localhost", database="informatica1_pf")
    Cursor3 = conexion3.cursor()
    Consul_SR = validacion(Mensaje1)
    print(Espacio)
    sql = f"SELECT * FROM pruebas WHERE {Serial_Probeta}=%s" %Consul_SR
    Cursor3.execute(sql)
    resultado = Cursor3.fetchall()
    Datos = []
    for lr in resultado:
        for D in lr:
            Datos.append(D)
    if Consul_SR in Datos:
        for r in resultado:
            print(f"""
                  Serial de la probeta: {r[0]}
                  Nombre del material: {r[1]}
                  Resultado de ensayo de traccion: {r[2]}
                  Resultado prueba de dureza: {r[3]}
                  Resultado prueba de hemocompatibilidad: {r[4]}
                  Resultado prueba de inflamabilidad: {r[5]}
                  Resultado densidad: {r[6]}
                  Resultado temperatura de fusion: {r[7]}
                  Fecha de realizacion: {r[8]}
                  Codigo responsable: {r[9]}""")
        print(Espacio)
    else:
        print(Mensaje2)
        print(Espacio)
    Cursor3.close()
    conexion3.close()
    