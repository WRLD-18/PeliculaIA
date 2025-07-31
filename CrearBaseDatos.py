
#Panda lo usamos para trabajar con datos
#Numpy lo usamos para trabajar con matrices y operaciones matemáticas
#os lo usamos para interactuar con el sistema operativo, (rutas, carpetas, etc)
import pandas as pd
import numpy as np
import os

#Esto busca en el mismo directorio donde se encuentra nuestro archivo, la carpeta data
DIR = "data"

#creamos las rutas de archivos a partir de la carpeta DIR anterior.
RATINGS = os.path.join(DIR,"u.data")
MOVIES = os.path.join(DIR,"u.item")

def create_rating_dataframe():
        #creamos un dataframe de pandas con los ratings:
    #Creo un encabezado personalizado para las columnas del dataframe
    ratings_encabezado = ["usuario_id", "pelicula_id", "rating", "timestamp"]
    rating_dataframe =  pd.read_csv(
                            RATINGS,         # Ruta del archivo, por ejemplo 'data/u.data'
                            sep='\t',             # El archivo está separado por TABULACIONES (no comas)
                            names=ratings_encabezado,   # Nombre personalizado para cada columna
                            encoding='latin-1'    # Para evitar errores con acentos/caracteres raros
                        )
    return rating_dataframe
def create_movies_dataframe(): 
    movies_encabezado = ["pelicula_id", "titulo", "fecha_lanzamiento", "video_release_date", "imdb_url"]
    movies_dataframe = pd.read_csv(
                            MOVIES, 
                            sep='|', #u.item esta separado por '|' no por tabs como el u.data
                            names=movies_encabezado, 
                            usecols=[0, 1, 2, 3, 4],
                            encoding='latin-1',
                        )
    return movies_dataframe

