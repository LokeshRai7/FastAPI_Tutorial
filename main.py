from typing import Optional
from fastapi import FastAPI 
from pydantic import BaseModel
import uvicorn


app = FastAPI()

@app.get('/blog')
def index(limit=10,published: bool = True, sort: Optional[str] = None ):
    # Only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs from the DB'}
    else:
        return {'data': f'{limit} blogs from the DB'}

@app.get('/blog/unpublished')
def unpublished(): 
    return {'data' : 'All unpublished blogs'}


@app.get('/blog/{id}')
def show(id : int):
    # Fetch blog with id = id
    return {'data': id}



@app.get(' ')
def comments(id,limit=10):
    # Fetch comments of blog with id = id
    return limit
    return {'data':{'1','2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return{'data':f'Blog is created with title as {blog.title}'}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)

