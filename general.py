import numpy as np  
import pandas as pd 
from datetime import datetime

pathnetflix = 'Datasets/netflix_titles-score.csv'
pathamazon = 'Datasets/amazon_prime_titles-score.csv'
pathhulu = 'Datasets/hulu_titles-score (2).csv'
pathdisney = 'Datasets/disney_plus_titles-score.csv'

Dfdisney = pd.read_csv(pathdisney) #Leer el archivo csv
Dfdisney.insert(0, 'id', 'd' + Dfdisney['show_id'], allow_duplicates=False) #Insertar Columna 'id'
Dfdisney['rating'] = Dfdisney['rating'].fillna('G') #Reemplazar NaN por 'G' en columna 'rating'
Dfdisney['date_added'] = pd.to_datetime(Dfdisney['date_added']) #Cambiar formato de fecha
Dfdisney['type'] = Dfdisney['type'].str.lower() #Cambiar a minúsculas las columnas con formato string
Dfdisney['title'] = Dfdisney['title'].str.lower()
Dfdisney['director'] = Dfdisney['director'].str.lower()
Dfdisney['cast'] = Dfdisney['cast'].str.lower()
Dfdisney['country'] = Dfdisney['country'].str.lower()
Dfdisney['rating'] = Dfdisney['rating'].str.lower()
Dfdisney['listed_in'] = Dfdisney['type'].str.lower()
Dfdisney['description'] = Dfdisney['description'].str.lower()
Dfdisney[['duration_int', 'duration_type']] = Dfdisney['duration'].str.split(expand = True) #Separar la columna duration en dos
Dfdisney['duration_type'] = Dfdisney['duration_type'].str.lower().replace('seasons','season') #Cambiar a minusculas la nueva columna str y poner en singular
Dfdisney['duration_int'] = Dfdisney['duration_int'].fillna(0) #Cambiar valores NaN por '0'(sino no se puede convertir a entero)
Dfdisney['duration_int'] = Dfdisney['duration_int'].astype(int) #Cambiar la otra nueva columna a entero

Dfnetflix = pd.read_csv(pathnetflix) #Leer el archivo csv
Dfnetflix.insert(0, 'id', 'n' + Dfnetflix['show_id'], allow_duplicates=False) #Insertar Columna 'id'
Dfnetflix['rating'] = Dfnetflix['rating'].fillna('G') #Reemplazar NaN por 'G' en columna 'rating'
Dfnetflix['date_added'] = pd.to_datetime(Dfnetflix['date_added']) #Cambiar formato de fecha
Dfnetflix['type'] = Dfnetflix['type'].str.lower() #Cambiar a minúsculas las columnas con formato string
Dfnetflix['title'] = Dfnetflix['title'].str.lower()
Dfnetflix['director'] = Dfnetflix['director'].str.lower()
Dfnetflix['cast'] = Dfnetflix['cast'].str.lower()
Dfnetflix['country'] = Dfnetflix['country'].str.lower()
Dfnetflix['rating'] = Dfnetflix['rating'].str.lower()
Dfnetflix['listed_in'] = Dfnetflix['type'].str.lower()
Dfnetflix['description'] = Dfnetflix['description'].str.lower()
Dfnetflix[['duration_int', 'duration_type']] = Dfnetflix['duration'].str.split(expand = True) #Separar la columna duration en dos
Dfnetflix['duration_type'] = Dfnetflix['duration_type'].str.lower().replace('seasons','season') #Cambiar a minusculas la nueva columna str y poner en singular
Dfnetflix['duration_int'] = Dfnetflix['duration_int'].fillna(0) #Cambiar valores NaN por '0'(sino no se puede convertir a entero)
Dfnetflix['duration_int'] = Dfnetflix['duration_int'].astype(int) #Cambiar la otra nueva columna a entero


Dfamazon = pd.read_csv(pathamazon) #Leer el archivo csv
Dfamazon.insert(0, 'id', 'a' + Dfamazon['show_id'], allow_duplicates=False) #Insertar Columna 'id'
Dfamazon['rating'] = Dfamazon['rating'].fillna('G') #Reemplazar NaN por 'G' en columna 'rating'
Dfamazon['date_added'] = pd.to_datetime(Dfamazon['date_added']) #Cambiar formato de fecha
Dfamazon['type'] = Dfamazon['type'].str.lower() #Cambiar a minúsculas las columnas con formato string
Dfamazon['title'] = Dfamazon['title'].str.lower()
Dfamazon['director'] = Dfamazon['director'].str.lower()
Dfamazon['cast'] = Dfamazon['cast'].str.lower()
Dfamazon['country'] = Dfamazon['country'].str.lower()
Dfamazon['rating'] = Dfamazon['rating'].str.lower()
Dfamazon['listed_in'] = Dfamazon['type'].str.lower()
Dfamazon['description'] = Dfamazon['description'].str.lower()
Dfamazon[['duration_int', 'duration_type']] = Dfamazon['duration'].str.split(expand = True) #Separar la columna duration en dos
Dfamazon['duration_type'] = Dfamazon['duration_type'].str.lower().replace('seasons','season') #Cambiar a minusculas la nueva columna str y poner en singular
Dfamazon['duration_int'] = Dfamazon['duration_int'].fillna(0) #Cambiar valores NaN por '0'(sino no se puede convertir a entero)
Dfamazon['duration_int'] = Dfamazon['duration_int'].astype(int) #Cambiar la otra nueva columna a entero

Dfhulu = pd.read_csv(pathhulu) #Leer el archivo csv
Dfhulu.insert(0, 'id', 'h' + Dfhulu['show_id'], allow_duplicates=False) #Insertar Columna 'id'
Dfhulu['rating'] = Dfhulu['rating'].fillna('G') #Reemplazar NaN por 'G' en columna 'rating'
Dfhulu['date_added'] = pd.to_datetime(Dfhulu['date_added']) #Cambiar formato de fecha
Dfhulu['type'] = Dfhulu['type'].str.lower() #Cambiar a minúsculas las columnas con formato string
Dfhulu['title'] = Dfhulu['title'].str.lower()
Dfhulu['director'] = Dfhulu['director'].str.lower()
Dfhulu['country'] = Dfhulu['country'].str.lower()
Dfhulu['rating'] = Dfhulu['rating'].str.lower()
Dfhulu['listed_in'] = Dfhulu['type'].str.lower()
Dfhulu['description'] = Dfhulu['description'].str.lower()
Dfhulu[['duration_int', 'duration_type']] = Dfhulu['duration'].str.split(expand = True) #Separar la columna duration en dos
Dfhulu['duration_type'] = Dfhulu['duration_type'].str.lower().replace('seasons','season') #Cambiar a minusculas la nueva columna str y poner en singular
Dfhulu['duration_int'] = Dfhulu['duration_int'].fillna(0) #Cambiar valores NaN por '0'(sino no se puede convertir a entero)
Dfhulu['duration_int'] = Dfhulu['duration_int'].astype(int) #Cambiar la otra nueva columna a entero

class Querys: 
    def __init__(self, platform, keyword, score , year, durationtype, rating):
        self.platform = platform
        self.keyword = keyword
        self.score = score
        self.year = year
        self.durationtype = durationtype
        self.rating = rating
        
    def get_word_count(platform , keyword):
        if (platform == 'amazon'):
            return Dfamazon['title'].str.contains(keyword).sum()
        if (platform == 'netflix'):
            return Dfnetflix['title'].str.contains(keyword).sum()
        if (platform == 'disney'):
            return Dfdisney['title'].str.contains(keyword).sum()
        if (platform == 'hulu'):
            return Dfhulu['title'].str.contains(keyword).sum()
        else:    
            return print('No existe esa Plataforma')

    def get_score_count(platform , score , year):
        if (platform == 'netflix'):
            return 'La cantidad de peliculas con un puntaje mayor a ' + str(score) + ' en el año '+ str(year)+ ' es de ' + str(len(Dfnetflix.query("type == 'movie' and score > @score and release_year == @year")))
        if (platform == 'amazon'):
            return 'La cantidad de peliculas con un puntaje mayor a ' + str(score) + ' en el año '+ str(year)+ ' es de ' + str(len(Dfamazon.query("type == 'movie' and score > @score and release_year == @year")))
        if (platform == 'disney'):
            return 'La cantidad de peliculas con un puntaje mayor a ' + str(score) + ' en el año '+ str(year)+ ' es de ' + str(len(Dfdisney.query("type == 'movie' and score > @score and release_year == @year")))
        if (platform == 'hulu'):
            return 'La cantidad de peliculas con un puntaje mayor a ' + str(score) + ' en el año '+ str(year)+ ' es de ' + str(len(Dfhulu.query("type == 'movie' and score > @score and release_year == @year")))
        else:    
            return 'No existe esa Plataforma'
    
    def get_second_score(platform):
        if (platform == 'netflix'):
            Df = Dfnetflix.query("type == 'movie'")
            n = Df['score'].max()
            c = Df.apply(lambda x: x['score'] == n, axis=1).sum()
            maximos = Df.nlargest(c, ['score'])
            ordenados = maximos['title'].sort_values()
            ordenados.iloc[1]
            return 'La segunda pelicula de '+ platform +' con mayor puntaje en orden alfabético es '+ ordenados.iloc[1] + ' con un puntaje de '+ str(n)
        if (platform == 'amazon'):
            Df = Dfamazon.query("type == 'movie'")
            n = Df['score'].max()
            c = Df.apply(lambda x: x['score'] == n, axis=1).sum()
            maximos = Df.nlargest(c, ['score'])
            ordenados = maximos['title'].sort_values()
            ordenados.iloc[1]
            return 'La segunda pelicula de '+ platform +' con mayor puntaje en orden alfabético es '+ ordenados.iloc[1] + ' con un puntaje de '+ str(n)
        if (platform == 'disney'):
            Df = Dfdisney.query("type == 'movie'")
            n = Df['score'].max()
            c = Df.apply(lambda x: x['score'] == n, axis=1).sum()
            maximos = Df.nlargest(c, ['score'])
            ordenados = maximos['title'].sort_values()
            ordenados.iloc[1]
            return 'La segunda pelicula de '+ platform +' con mayor puntaje en orden alfabético es '+ ordenados.iloc[1] + ' con un puntaje de '+ str(n)
        if (platform == 'hulu'):
            Df = Dfhulu.query("type == 'movie'")
            n = Df['score'].max()
            c = Df.apply(lambda x: x['score'] == n, axis=1).sum()
            maximos = Df.nlargest(c, ['score'])
            ordenados = maximos['title'].sort_values()
            ordenados.iloc[1]
            return 'La segunda pelicula de '+ platform +' con mayor puntaje en orden alfabético es '+ ordenados.iloc[1] + ' con un puntaje de '+ str(n)
        else:    
            return 'No existe esa Plataforma'

    def get_longest(platform, durationtype, year):
        if (platform == 'netflix'):
            Df = Dfnetflix.query("release_year == @year and duration_type == @durationtype")
            Df1 = Df.sort_values( by = 'duration_int' , ascending = False)
            title = str(Df1['title'].iloc[0])
            duration = str(Df1['duration_int'].iloc[0])
            if durationtype == 'min':
                return 'La pelicula con mayor duración de ' + platform +' en el año ' + str(year) + ' es '+ title +' con '+ str(duration) +'('+ durationtype +')'
            if durationtype == 'season':
                return 'La serie con mayor duración de ' + platform +' en el año ' + str(year) +  ' es '+ title +' con '+ str(duration) +'('+ durationtype +')'
        if (platform == 'amazon'):
            Df = Dfamazon.query("release_year == @year and duration_type == @durationtype")
            Df1 = Df.sort_values( by = 'duration_int' , ascending = False)
            title = str(Df1['title'].iloc[0])
            duration = str(Df1['duration_int'].iloc[0])
            if durationtype == 'min':
                return 'La pelicula con mayor duración de ' + platform +' en el año ' + str(year) +  ' es '+ title +' con '+ str(duration) +'('+ durationtype +')'
            if durationtype == 'season':
                return 'La serie con mayor duración de ' + platform +' en el año ' + str(year) +  ' es '+ title +' con '+ str(duration) +'('+ durationtype +')'
        if (platform == 'disney'):
            Df = Dfdisney.query("release_year == @year and duration_type == @durationtype")
            Df1 = Df.sort_values( by = 'duration_int' , ascending = False)
            title = str(Df1['title'].iloc[0])
            duration = str(Df1['duration_int'].iloc[0])
            if durationtype == 'min':
                return 'La pelicula con mayor duración de ' + platform +' en el año ' + str(year) +  ' es '+ title +' con '+ str(duration) +'('+ durationtype +')'
            if durationtype == 'season':
                return 'La serie con mayor duración de ' + platform +' en el año ' + str(year) +  ' es '+ title +' con '+ str(duration) +'('+ durationtype +')'
        if (platform == 'hulu'):
            Df = Dfhulu.query("release_year == @year and duration_type == @durationtype")
            Df1 = Df.sort_values( by = 'duration_int' , ascending = False)
            title = str(Df1['title'].iloc[0])
            duration = str(Df1['duration_int'].iloc[0])
            if durationtype == 'min':
                return 'La pelicula con mayor duración de ' + platform +' en el año ' + str(year) +  ' es '+ title +' con '+ str(duration) +'('+ durationtype +')'
            if durationtype == 'season':
                return 'La serie con mayor duración de ' + platform +' en el año ' + str(year) +  ' es '+ title +' con '+ str(duration) +'('+ durationtype +')'       
        else:    
            return 'No existe esa Plataforma'
        
    def get_rating_count(rating):
        n = Dfnetflix.apply(lambda x: x['rating'] == str(rating), axis = 1).sum()
        d = Dfdisney.apply(lambda x: x['rating'] == str(rating), axis = 1).sum() 
        a = Dfamazon.apply(lambda x: x['rating'] == str(rating), axis = 1).sum()
        h = Dfhulu.apply(lambda x: x['rating'] == str(rating), axis = 1).sum()
        return 'La cantidad de series y peliculas por rating = ' + rating + ' es de ' +str(n + d + a + h) + ' en las cuatro plataformas'

