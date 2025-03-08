from random import randrange
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from flask.typing import ResponseClass

from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True  #default val bool, user doesnt have to provide this field. If not provided it will default to True, or None if set to None
    rating: Optional[int] = None #To set optional input we are importing optional. If nothing is passed in for rating, it returns None. 
my_posts = [{"title": "XY", "content": "CX", "id": 1}, {"title": "ew", "content": "CfsdX", "id": 2}]
#for now we are storing the post data here, as an array of dicts. each dict needs to have its own unique id. 
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post): #here the body is saved in post_dict. id is added. post_dict is saved in my posts, then returned to the user. 
    post_dict = post.model_dump() 
    post_dict["id"] = randrange(0, 100000000) 
    my_posts.append(post_dict)
    return {"data": post_dict}

def find_post(id):
    for p in my_posts:
        if p["id"] == id: return p
def find_index_post(id):
    for i, po in enumerate(my_posts):
        if po['id'] == id:
            return i



@app.get("/") #Route or a Path operation
def root():
    return {'message': 'sig'}

@app.get("/posts") #get requests are only used to retrieve data and should not contain a request. When we use postman we are 
def get_posts():
    return {"data": "Post"}

@app.get("/posts/{id}") #request for a single post. id is a path parameter
def get_post(id: int, response: Response): #specifying the param type will ensure that a validation error is thrown when the param type if not int. 
    
    post = find_post(id)    
    if not post:
        '''response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"post with id: {id} was not found. "}'''
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found. ")
    return {"Post detail": post}

@app.put("/posts/{id}")
def update_post(id: int, post:Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"post with id: {id} does not exist.")
    post_dict = post.model_dump() #convert update data into dict
    post_dict["id"] = id
    my_posts[index] = post_dict
    return {"message": "updated post"}

    