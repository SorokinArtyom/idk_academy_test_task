# from pydantic import BaseModel, Field
# from typing import Annotated

# class User(BaseModel):

#     id: int 
#     name: str
#     age: int


# class Post(BaseModel):

#     id: int
#     title: str
#     body: str
#     author: User

# class PostCreate(BaseModel):
    
#     title: str
#     body: str
#     author_id: int

# class UserCreate(BaseModel):
#     name: Annotated[
#         str, Field(..., title="Имя пользователя", min_length=2, max_length=20)
#     ]
#     age: Annotated[
#         int, Field(..., title="Возраст пользователя", ge=1, le=120)
#     ]
