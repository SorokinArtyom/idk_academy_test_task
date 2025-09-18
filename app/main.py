from fastapi import FastAPI, HTTPException, Path, Query, Body
from typing import Optional, Annotated

from app.schemas import Post, PostCreate, User, UserCreate


users = [
    {"id": 1, "name": "John", "age": 34},
    {"id": 2, "name": "Anatoly", "age": 28},
    {"id": 3, "name": "Ivan", "age": 21}
]

posts = [
    {'id': 1, 'title': 'News page 1', 'body': 'Text from page 1', 'author': users[1]},
    {'id': 2, 'title': 'News page 2', 'body': 'Text from page 2', 'author': users[0]},
    {'id': 3, 'title': 'News page 3', 'body': 'Text from page 3', 'author': users[2]}
]

app = FastAPI()

@app.get("/")
async def home() -> dict:
    return {"data": "message"}

@app.get("/contacts")
async def contacts() -> int:
    return 34

# @app.get("/items")
# async def items() -> list[Post]:
#     post_objects = []
#     for post in posts:
#         post_objects.append(Post(id=post['id'], title=post['title'], body=post['body']))
#     return post_objects

@app.get("/items")
async def items() -> list[Post]:
    return [Post(**post) for post in posts]

@app.get("/items/{id}")
async def items(id: Annotated[int, Path(..., title='Здесь указывается ID поста', ge=1, lt=100)]) -> Post:
    for post in posts:
        if post['id'] == id:
            return Post(**post)
    raise HTTPException(status_code=404, detail="Page not found")

@app.post("/items/add")
async def add_item(post: PostCreate) -> Post:
    author = next((user for user in users if user['id'] == post.author_id), None)
    if not author:
        raise HTTPException(status_code=404, detail="User not found")
    
    new_post_id = len(posts) + 1
    new_post = {
        'id': new_post_id,
        'title': post.title,
        'body': post.body,
        'author': author
    }
    posts.append(new_post) 

    return Post(**new_post)

@app.get("/search")
async def search(post_id: Annotated[
    Optional[int],
    Query(title="ID of post search for", ge=1, le=50)
    ]) -> dict[str, Optional[Post]]:

    if post_id:
        for post in posts:
            if post['id'] == post_id:
                return {"data": Post(**post)}
        raise HTTPException(status_code=404, detail="Page not found")
    else:
        raise {"data": None}

@app.post("/user/add")
async def add_user(user: Annotated[
    UserCreate,
    Body(..., example={
        "name": "John",
        "age": 20
    })
]) -> User:
    new_user_id = len(User) + 1

    new_user = {
        'id': new_user_id,
        'name': user.name,
        'age': user.age
    }
    users.append(new_user) 

    return User(**new_user)