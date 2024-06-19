import json
opc=0
print("Bienvenido")
trabajador=[]
sueldoBru=0

while opc!=4:
    print("Elija una de estas 3 opciones\n1.- Registrar trabajador\n2.- Lista de los trabajadores\n3.- Imprimir plantillas de sueldo\n4.- Salir")
    opc=input("Seleccione una de las opciones mensionadas\n> ")
    match opc:
        case "1":
            nombre=input("ingrese nombre\n> ")
            apellido=input("ingrese el apellido\n> ")
            Cargo=input("ingrese su cargo correspondiente\nCEO,Desarrollador,Analista de datos\n> ")
            sueldoBru=int(input("Ingrese el sueldo Bruto\n> "))
            descuentSalud=sueldoBru*0.7
            descuentAFP=sueldoBru*0.12
            sueldoLiquid=sueldoBru-descuentAFP-descuentSalud
            trabajador.append({"Nombre":nombre,"Apellido":apellido,"Puesto":Cargo,"Sueldo bruto":sueldoBru,"Desc. Salud": descuentSalud,"Desc. AFP": descuentAFP,"Sueldo Liquido":sueldoLiquid})
            with open("trabajadores.txt", "w") as archivo:
                json.dump(trabajador,archivo)
        case "2": 
            print(trabajador)
        case "3":
            print("**Lista de Trabajadores**")
            print(trabajador)
        case "4":
            print("Adios")
        
        

