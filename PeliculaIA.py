from sklearn.feature_extraction.text import TfidfVectorizer
import CrearBaseDatos
import pandas as pd

def main():
    movies_dataframe = CrearBaseDatos.create_movies_dataframe()
    ratings_dataframe = CrearBaseDatos.create_rating_dataframe()

    #Hago unas listas con los nombres
    titulos = movies_dataframe["titulo"].tolist()

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

    TFIDF = pd.DataFrame(
                vect_matriz.toarray(),columns=palabras,index=titulos
            )
    
