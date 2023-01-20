#ARCHIVO DEDICADO AL FUNCIONAMIENTO DE LA API

from fastapi import FastAPI

app = FastAPI()

from general import Querys

@app.get("/")
async def Main():
    return "¡BIENVENIDO AL PI01! (Consulte la base de datos agregando /query + el numero de la consulta y cambie los parametros de consulta)"

@app.get("/query1")
async def query1(platform, keyword):
    return 'La Palabra ' + keyword + ' se encuentra ' + str(Querys.get_word_count(platform, keyword)) + ' veces en la plataforma ' + platform

@app.get("/query2")
async def query2(platform ,score ,year):
    return (Querys.get_score_count(platform , int(score), int(year)))

@app.get('/query3')
async def query3(platform):
    return Querys.get_second_score(platform)

@app.get('/query4')
async def query4(platform, durationtype, year):
    return Querys.get_longest(platform, durationtype, int(year))

@app.get('/query5')
async def query5(rating):
    return Querys.get_rating_count(rating)