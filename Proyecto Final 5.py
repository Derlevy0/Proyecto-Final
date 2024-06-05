import os
import xml.etree.ElementTree as ET
from Validaciones import *   
from F_CRUD import * 
import mysql.connector
import json

Espacio = "____________________________________________________________________"
directorio = os.getcwd()

Lista_Resul = []
Resultados = {"Serial_Probeta":202401, "Nombre_Material":"Hierro", "Resultado_Ensayo_Deformacion":22.5, "Resultado_Dureza":255, "Resultado_Hemocompatibilidad":"NO", 
"Resultado_Inflamabilidad":"NO", "Resultado_Densidad":15.234, "Resultado_Temperatura_Fusion":16, "Fecha_Realizacion":"2024/06/01", "Codigo_Responsable":110}
Resultados1 = {"Serial_Probeta":202402, "Nombre_Material":"Aluminio", "Resultado_Ensayo_Deformacion":105.01, "Resultado_Dureza":87, "Resultado_Hemocompatibilidad":"NO", 
"Resultado_Inflamabilidad":"NO", "Resultado_Densidad":15.44, "Resultado_Temperatura_Fusion":5, "Fecha_Realizacion":"2024/06/05", "Codigo_Responsable":100}
Lista_Resul.append(Resultados)
Lista_Resul.append(Resultados1)
with open(f"{directorio}/Pruebas.json", "w+") as P_Datos:
    json.dump(Lista_Resul, P_Datos, indent="\t")

conexion = mysql.connector.connect(user="root", password="", host="localhost")
Cursor = conexion.cursor()
Cursor.execute("SHOW DATABASES")
List_DB = []
for bd in Cursor:
    List_DB.append(bd)
if ("informatica1_pf",) in List_DB:
    True
else:
    Cursor.execute("CREATE DATABASE informatica1_pf")
conexion.close()

conexion1 = mysql.connector.connect(user="root", password="", host="localhost", database="informatica1_pf")
Cursor1 = conexion1.cursor()
Cursor1.execute("SHOW TABLES")
List_TB = []
for tb in Cursor1:
    List_TB.append(tb)
if ("responsables",) in List_TB:
    True
else:
    sql = """CREATE TABLE responsables (Codigo_Responsanble INT(10), Contraseña VARCHAR(10), Apellido TEXT(40), Nombre TEXT(20), Numero_Documento_Identidad INT(10), Cargo TEXT(20))"""
    Cursor1.execute(sql)
if ("pruebas",) in List_TB:
    True
else:
    sql = """CREATE TABLE pruebas (Serial_Probeta INT(6), Nombre_Material TEXT(20), Resultado_Ensayo_Deformacion FLOAT(10), Resultado_Dureza INT(5), Resultado_Hemocompatibilidad TEXT(2), 
    Resultado_Inflamabilidad TEXT(2), Resultado_Densidad FLOAT(10), Resultado_Temperatura_Fusion INT(10), Fecha_Realizacion VARCHAR(11), Codigo_Responsable INT(10))"""
    Cursor1.execute(sql)
    conexion1.commit()
Cursor1.close()
conexion1.close()

bye=0
while bye!=1:
    if os.path.exists(f"{directorio}/admin"):
        True
    else:
        os.mkdir(f"{directorio}/admin")
        
        root = ET.Element("Usuarios")
        usser1 = ET.SubElement(root, "Usuario")
        usser1.set("ID", "1041056543")
        usser1.set("Clave", "12345678")
        name1 = ET.SubElement(usser1, "Nombre")
        name1.text="Derlevy Yepes Valencia"
        usser2 = ET.SubElement(root, "Usuario")
        usser2.set("ID", "1018224431")
        usser2.set("Clave", "87654321")
        name2 = ET.SubElement(usser2, "Nombre")
        name2.text="Daniel Esteban Rojas Correa"
        tree = ET.ElementTree(root)
        ET.indent(tree)
        tree.write(f"{directorio}/admin/Users.xml", encoding="UTF-8")
        
    Tree = ET.parse(f"{directorio}/admin/Users.xml")
    Root = Tree.getroot()
    lista = []
    Lista_Key = []
    Lista_CC = []
    for child in Root.findall("Usuario"):
        dicc = {child.get("Clave"):[child.find("Nombre").text, child.get("ID")]}   
        lista.append(dicc)
        Lista_Key.append(child.get("Clave"))
        Lista_CC.append(child.get("ID"))
        
    conexion_p = mysql.connector.connect(user="root", password="", host="localhost", database="informatica1_pf")
    Cursor_p = conexion_p.cursor()
    sql = "SELECT * FROM responsables"
    Cursor_p.execute(sql)
    resultado_p = Cursor_p.fetchall()
    Datos_p = []
    List_p = []
    for lr_p in resultado_p:
        dicc_p = {lr_p[1]:lr_p[3]}
        Datos_p.append(dicc_p)
        List_p.append(lr_p[1])
            
    login = validacion("""Seleccione: 
                       1- Para ingresar
                       2- Para cambiar contraseña
                       \n""")
    opciones(login, 1, 2)
    print(Espacio)
    if login==1:
        usser = input("Ingrese su Usuario: ")
        print(Espacio)
        contra = input("Ingrese su Contraseña: ")
        print(Espacio)
        if contra in Lista_Key:
            for L in lista:
                val = L.get(contra, "Su usuario o contraseña son incorrectos, por favor intentelo nuevamente.....")
                if val!="Su usuario o contraseña son incorrectos, por favor intentelo nuevamente.....":
                    if val[0]==usser:
                        Actualizar=0
                        while Actualizar!=1:
                            principal = validacion("""Gestionar la informacion de:
                                                   1- Administradores
                                                   2- Responsables
                                                   3- Resultados de Prueba
                                                   4- Salir
                                                   \n""")
                            opciones(principal, 1, 4)
                            print(Espacio)
                            Intentos = 0
                            if principal==1:
                                while Intentos!=3:
                                    SubMenu1 = validacion("""
                                                          1. Crear usuario administrador
                                                          2. Ver usuario administrador
                                                          3. Actualizar la información de un administrador
                                                          4. Eliminar un administrador
                                                          5. Ingresar responsable de prueba
                                                          6. Ver información de responsable de prueba
                                                          7. Actualizar la información del responsable de la prueba
                                                          8. Ver la información de todas las pruebas almacenadas asociadas a la persona responsable de la
                                                          prueba
                                                          9. Ver materiales estudiados por los diferentes responsables
                                                          10. Eliminar un responsable
                                                          11. Volver al menú principal
                                                          \n""")
                                    opciones(SubMenu1, 1, 11)
                                    if SubMenu1<1 or SubMenu1>11:
                                        Intentos+=1
                                    print(Espacio)
                                    if SubMenu1==1:
                                        nombre = validacion_STR("Nombre: ")
                                        cedula = input("Numero de Identificacion: ")
                                        contraseña = validacion_ISALNUM("Contraseña: ")
                                        print(Espacio)
                                        I_User(nombre, cedula, contraseña, Root, Tree)
                                        
                                    elif SubMenu1==2:
                                        V_User("Ingrese la contraseña del administrador que desea ver: ", Lista_Key, lista)
                                        
                                    elif SubMenu1==3:
                                        A_User("Ingrese el numero de identificacion del administrador: ", Lista_CC, Root, Tree, principal, Actualizar)
                                        
                                    elif SubMenu1==4:
                                        E_User("Ingrese el numero de identificacion del administrador: ", Lista_CC, Root, Tree)
                                        
                                    elif SubMenu1==5:
                                        Ingresar_Responsable("conexion2")
                                        
                                    elif SubMenu1==6:
                                        Ver_Responsable("conexion3")
                                        
                                    elif SubMenu1==7:
                                        Actualizar_Todo("conexion3")
                                        
                                    elif SubMenu1==8:
                                        Ver_Prueba("Ingrese el Codigo Responsable: ", "El Codigo Responsable ingresado no se encuentra en el sistema", "Codigo_Responsable")
                                        
                                    elif SubMenu1==10:
                                        Eliminar("Ingrese el numero de identificacion del responsable: ", "La Cedula ingresada no se encuntra en el sistema...", "responsables", "Numero_Documento_Identidad")
                                        
                                    elif SubMenu1==11:
                                        break
                                
                            elif principal==2:
                                while True:
                                    SubMenu2 = validacion("""
                                                          1. Cambiar contraseña
                                                          2. Ver datos personales
                                                          3. Actualizar datos personales
                                                          4. Ingresar nuevo resultado de prueba de material
                                                          5. Importar resultados de prueba 
                                                          6. Actualizar la información de resultados de pruebas
                                                          7. Ver la información del resultado una de las pruebas de material
                                                          8. Ver todos los resultados de todas la pruebas realizadas
                                                          9. Eliminar un resultado de prueba
                                                          10. Volver al menú principal
                                                          \n""")
                                    opciones(SubMenu2, 1, 10)
                                    print(Espacio)
                                    if SubMenu2==1:
                                        Actualizar_Responsable("Ingrese la cedula del Responsable: ", "Ingrese la nueva contraseña: ", "Contraseña")
                                    
                                    elif SubMenu2==2:
                                        Ver_Responsable("conexion3")
                                    
                                    elif SubMenu2==3:
                                        Actualizar_Todo("conexion3")
                                        
                                    elif SubMenu2==4:
                                        Ingresar_Prueba("conexion2")
                                        
                                    elif SubMenu2==5:
                                        Archivo = validacion_STR("Ingrese el nombre del archivo del que desea importar los datos: ") 
                                        print(Espacio)
                                        Exist = os.path.exists(f"{directorio}/{Archivo}")
                                        if Exist==True:
                                            conexion1 = mysql.connector.connect(user="root", password="", host="localhost", database="informatica1_pf")
                                            Cursor1 = conexion1.cursor()
                                            with open(f"{directorio}/{Archivo}", "r") as Date:
                                                Diccionarios = json.load(Date)
                                            for Dt in Diccionarios:
                                                val = (Dt["Serial_Probeta"], Dt["Nombre_Material"], Dt["Resultado_Ensayo_Deformacion"], Dt["Resultado_Dureza"], Dt["Resultado_Hemocompatibilidad"], 
                                                Dt["Resultado_Inflamabilidad"], Dt["Resultado_Densidad"], Dt["Resultado_Temperatura_Fusion"], Dt["Fecha_Realizacion"], Dt["Codigo_Responsable"])
                                                sql1 = """INSERT INTO pruebas (Serial_Probeta, Nombre_Material, Resultado_Ensayo_Deformacion, Resultado_Dureza, Resultado_Hemocompatibilidad, 
                                                Resultado_Inflamabilidad, Resultado_Densidad, Resultado_Temperatura_Fusion, Fecha_Realizacion, Codigo_Responsable) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""" 
                                                Cursor1.execute(sql1,val)
                                                conexion1.commit()
                                            print("Archivo Importado con Exito")
                                            print(Espacio)
                                        else:
                                            print("No se ha encontrado ningun archivo con el nombre ingresado.....")
                                            print(Espacio)
                                        Cursor1.close()
                                        conexion1.close()
                                        
                                    elif SubMenu2==6:
                                        Actualizar_Prueba("conexion3")
                                        
                                    elif SubMenu2==7:
                                        Ver_Prueba("Ingrese el numero de serie correspondiente a la probeta de la prueba: ", "El serial de la probeta ingresado no se encuentra en el sistema...", "Serial_Probeta")
                                        
                                    elif SubMenu2==8:
                                        conexion3 = mysql.connector.connect(user="root", password="", host="localhost", database="informatica1_pf")
                                        Cursor3 = conexion3.cursor()
                                        sql = "SELECT * FROM pruebas"
                                        Cursor3.execute(sql)
                                        resultado = Cursor3.fetchall()
                                        for lr in resultado:
                                            serie = lr[0]
                                            fecha =lr[8]
                                            print(f"""
                                                  Serie de la Probeta: {serie}
                                                  Fecha de Estudio: {fecha}""")
                                                  
                                    elif SubMenu2==9:
                                        Eliminar("Ingrese la serie de probeta de la prueba que desea eliminar: ", "El numero de serie ingresado no se encuntra en el sistema...", "pruebas", "Serial_Probeta")
                                    
                                    elif SubMenu2==10:
                                        break
                                    
                            elif principal==4:
                                salir = input("Ingrese su contraseña: ")
                                if salir==contra:
                                    bye+=1
                                    break
                                else:
                                    print("La contraseña es incorreta.....")
                                    continue
                    else:
                        print("Su usuario o contraseña son incorrectos, por favor intentelo nuevamente.....")
                        continue
        else:
            print("Su usuario o contraseña son incorrectos, por favor intentelo nuevamente.....")
            continue
            
    elif login==2:
        CC = input("Ingrese su numero de cedula: ")
        vieja = input("Ingrese su contraseña anterior: ")
        if CC in Lista_CC:
            if vieja in Lista_Key:
                new = input("Ingrese su nueva contraseña: ")
                for C in Root.findall("Usuario"):
                    if C.get("Clave")==vieja:
                        C.set("Clave", new)
                        Tree.write(f"{directorio}/admin/Users.xml")
            else:
                print("La clave ingresada es incorrecta.....")
                continue
        else:
            print("El numero de cedula ingresado no se encuentra en el sistema.....")
            continue
            
        
    
    