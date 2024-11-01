from Package_SmartPen.class_boligrafo import *
from Package_SmartPen.funciones import *
lista_lapicera = []

while True:
    opcion = int(input("""
    1- cargar lapiceras
    2- mostrar lapiceras
    3- escribir
    4- cargar tinta
    5- escribir hasta agotar tinta
    0- salir
                    
    -->  """))

    match opcion:

        case 1:
            for i in range (5):
                color = input("Ingrese el color del boligrafo: ")
                grosor = input("Ingrese el grosor del boligrafo: ").upper()
                lapicera = crear_boligrafo(color, grosor)
                lista_lapicera += [lapicera]

        case 2:
            for i in range (len(lista_lapicera)):
                lista_lapicera[i].mostrar()
        
        case 3:
            opcion_birome = int(input("Ingrese con que birome quiere escribir: "))

            lista_lapicera[opcion_birome].escribir()

        case 4:
            opcion_birome = int(input("Ingrese que birome quiere recargar: "))
            cantidad_tinta = int(input("Cuanta tinta quiere agregar: "))
            lista_lapicera[opcion_birome].recargar(cantidad_tinta)

        case 5:
            lapiceras_gastadas = escribir_hasta_agotar(lista_lapicera)

            print("Estas lapiceras han sido agotadas:")

            for i in range (len(lapiceras_gastadas)):
                lapiceras_gastadas[i].mostrar()

        case 6:
            cargar_lapiceras_gastadas(lista_lapicera, lapiceras_gastadas)
            print("se han cargado todas las lapiceras gastadas")

        case 0:
            break



