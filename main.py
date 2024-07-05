from fastapi import FastAPI
from data  import movies_list
from data.movies import movies

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "FAST API"}


@app.get("/hello/{rno}")
async def say_hello(rno: int):
    return {"message": f"Hello {rno}"}


@app.get("/movies")
async def get_movies():
    return list(movies .values())

#@app.get("/movies/{name}")
#async def get_movies(name :str):
    #return movies[name]

@app.get("/movies/{limit}")
async def get_all_movies(limit:int=5):
    all_movies=list(movies_list.values())
    return all_movies[:limit]

@app.get("/movies")
async def get_all_movies(offset: int,limit: int=5):
    all_movies=list(movies_list.values())
    movies_count=len(all_movies)
    start_index = (offset-1)*limit
    end_index = start_index+limit
    if start_index>=movies_count:
        return None
    return all_movies[start_index:end_index]

