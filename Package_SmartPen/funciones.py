from Package_SmartPen.class_boligrafo import *

def crear_boligrafo (color:str, grosor:str):
    tinta = 80
    max_tinta = 100

    smartpen = Boligrafo(max_tinta, grosor, color, tinta)

    return smartpen


def escribir_hasta_agotar (lista_lapiceras):
    cadena = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    contador = 0
    lapiceras_gastadas = []
    i = 0

    while True:
        
        if i > len(lista_lapiceras)-1:
            i = 0


        if lista_lapiceras[i].grosor_punta == 'FINO':
            lista_lapiceras[i].cantidad_tinta -= len(cadena)
            if lista_lapiceras[i].cantidad_tinta <= 0:
                lista_lapiceras[i].cantidad_tinta = 0
                print(f"Se ha gastado la lapicera {lista_lapiceras[i].color}")

        else:
            lista_lapiceras[i].cantidad_tinta -= (len(cadena) * 2)
            if lista_lapiceras[i].cantidad_tinta <= 0:
                lista_lapiceras[i].cantidad_tinta = 0
                print(f"Se ha gastado la lapicera {lista_lapiceras[i].color}")

        if lista_lapiceras[i].cantidad_tinta == 0:

            lapiceras_gastadas = lapiceras_gastadas + [lista_lapiceras[i]]
            del lista_lapiceras[i]
            
            contador += 1

            if contador == 2:
                return lapiceras_gastadas

        i+=1
def cargar_lapiceras_gastadas (lista_lapiceras, lapiceras_gastadas):

    for i in range (len(lapiceras_gastadas)):


        lapiceras_gastadas[i].recargar(100)

        lista_lapiceras += [lapiceras_gastadas[i]]
