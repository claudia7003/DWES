FILAS = [
    
"Ana Lara;absoluta;Club Atletismo Cádiz;3187",
    
"Bruno Ruiz;absoluta;-;3425",
    
"Carmen Solís;absoluta;Corredores Puntales;2958",
    
"David Mora;absoluta;-;-",
    
"Elena Cano;absoluta;Corredores Puntales;3345",
    
"Fran Gil;juvenil;Club Atletismo Cádiz;3601",
    
"Gloria Vega;juvenil;-;3750",
    
"Hugo Prats;juvenil;-;3903",
    
"Inés Roldán;veterano;Veteranos de la Bahía;3847",
    
"Javier Osuna;veterano;-;4110",
    
"Kais Zapata;veterano;Veteranos de la Bahía;3599",
    
"Lucía Prieto;veterano;-;4365",
]

#nombre;categoria;club;tiempo_en_segundos

class ErrorCarrera():
    pass

class TiempoInvalidoError(ErrorCarrera):
    def __init__(self, tiempo):
        super().__init__()
        self.tiempo = tiempo
#Se lanza cuando un tiempo en segundos es negativ
        if tiempo < 0:
            raise ErrorCarrera("El timepo no puede ser negativo")


class CategoriaInvalidaError(ErrorCarrera):
    def __init__(self, categoria):
        super().__init__()
        self.categoria = categoria
#Se lanza cuando la categoria no está en PRECIOS_BASE
        if categoria not in PRECIOS_BASE:
            raise ErrorCarrera("La categoria no está en Precios Base")


class ExtraInvalidoError(ErrorCarrera):
    def __init__(self, extra):
        super().__init__()
        self.extra = extra
#Se lanza cuando el extra no está en EXTRAS
        if extra not in EXTRAS:
            raise ErrorCarrera("El extra no está en EXTRAS")


