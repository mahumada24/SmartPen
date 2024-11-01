class Boligrafo:
    def __init__ (self, capacidad_max, grosor_punta, color, cantidad_tinta): 

        self.capacidad_max = capacidad_max
        self.grosor_punta = grosor_punta
        self.color = color
        self.cantidad_tinta = cantidad_tinta

    
    def escribir (self):
        texto = input("texto--> ")
        if self.grosor_punta == "FINO": #Si es fino

            if self.cantidad_tinta >= len(texto): #Si la cantidad de tinta, no supera los caracteres del texto
                self.cantidad_tinta -= len(texto) #Se le resta a la cantidad de tita, los caracteres
                return texto #retorno el texto

            else:
                print("tinta insuficiente")
        
        else:
            if self.cantidad_tinta >= len(texto): 
                self.cantidad_tinta -= (len(texto) *2) #Se descuenta el doble de la cantida de caracteres
                return texto
            else:
                print("tinta insuficiente")
        


    def recargar (self, agregar_tinta):
        
        if self.cantidad_tinta + agregar_tinta < self.capacidad_max:
            self.cantidad_tinta += agregar_tinta
            print ("lapicera recargada")

            return self.cantidad_tinta
        
        else:
            resto = (self.cantidad_tinta + agregar_tinta) - self.capacidad_max

            self.cantidad_tinta += (agregar_tinta - resto)

            print(f"Lapicera cargada, sobro {resto} cantidad de tinta")

            return self.cantidad_tinta

    def mostrar(self):

        print (self.cantidad_tinta, self.capacidad_max, self.color, self.grosor_punta)
