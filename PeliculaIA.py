from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import CrearBaseDatos
import pandas as pd

def create_similarity(titulos):

    #inicializamos el vector
    vectorizer = TfidfVectorizer()

    #fit lo que hace es aprender las palabras de los titulos
    vectorizer.fit(titulos)

    #almacenamosen vect_matriz la matriz generada al tranformarlo en numeros
    #Tranform lo que hace es a partir de lo aprendido, saca el vector numero de lo que le pases, si añadimos luego mas titulos, simplemente hacemos otro tranform y ya tendriamos recomendaciones
    #de peliculas anteriores a las nuevas, luego se deberian añadir al aprendizaje esas palabras ?supongo
    vect_matriz= vectorizer.transform(titulos)
    
    #vectorizer.fit_transform(), se puede hacer de 1

    #nos dan las palabras aprendidas
    palabras = vectorizer.get_feature_names_out()

    #usamos DataFrame ya que tenemos almacenado en memoria datos y no queremos crear un dataframe a partir de un archivo de texto
    #es para depuracion y ver lo que hemos generado.

    TFIDF = pd.DataFrame(
                vect_matriz.toarray(),columns=palabras,index=titulos
            )
    similitud = cosine_similarity(vect_matriz)
    return similitud
    

def comprobar_rating(ratings_dataframe,lista_recomendado,titulos,titulos_id ):
    ratings_all = ratings_dataframe["rating"].tolist()
    for i in range(lista_recomendado):
        posicion = titulos.index(lista_recomendado[i])
        id = titulos_id[posicion]
        posicion_rat = ratings_dataframe["pelicula_id"].tolist().index(id)
        rate = ratings_all[posicion_rat]
        if rate < 2:
            del lista_recomendado[i]    


    #con del borro la un elemento de la lista y automaticamente se desplazan a la izquierda

def main():
    movies_dataframe = CrearBaseDatos.create_movies_dataframe()
    ratings_dataframe = CrearBaseDatos.create_rating_dataframe()

    #Hago unas listas con los nombres
    titulos = movies_dataframe["titulo"].tolist()

    titulo_usuario = input("Titulo de pelicula: ")

    sim = create_similarity(titulos)

    #uso la funcion not in  de las listas
    if titulo_usuario not in titulos:
        print("No existe tal titulo")
        return 
    #saca la posicion de titlos_usuario
    lista_recomendada = []
    posicion = titulos.index(titulo_usuario)
    for i in range(len(sim[posicion])):
        if sim[posicion][i] > 0.60:
            lista_recomendada.append(titulos[i])
    
    comprobar_rating(ratings_dataframe,lista_recomendada,titulos,movies_dataframe["pelicula_id"].tolist())
    print("las peliculas recomendadas son: ")
    for pel in lista_recomendada:
        print(pel)


if __name__ == "__main__":
    main()



