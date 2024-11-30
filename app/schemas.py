from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional
from pydantic.types import conint


# POST
class PostBase(BaseModel):
    title: str = Field(..., description="Title of the post")
    content: str = Field(..., description="Content of the post")
    published: bool = Field(default=True, description="Whether the post is published or not")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "My First Post",
                "content": "This is the content of the post.",
                "published": True,
            }
        }
    )


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int = Field(..., description="ID of the user")
    email: EmailStr = Field(..., description="Email address of the user")
    created_at: datetime = Field(..., description="Timestamp of when the user was created")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "email": "user@example.com",
                "created_at": "2024-11-16T12:00:00",
            }
        }
    )


class Post(PostBase):
    id: int = Field(..., description="ID of the post")
    created_at: datetime = Field(..., description="Timestamp of when the post was created")
    owner_id: int = Field(..., description="ID of the user who owns the post")
    owner: UserOut

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 123,
                "title": "My First Post",
                "content": "This is the content of the post.",
                "published": True,
                "created_at": "2024-11-16T12:00:00",
                "owner_id": 1,
                "owner": {
                    "id": 1,
                    "email": "user@example.com",
                    "created_at": "2024-11-16T12:00:00",
                },
            }
        }
    )


class PostOut(BaseModel):
    Post: Post
    votes: int = Field(..., description="Number of votes for the post")

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "Post": {
                    "id": 123,
                    "title": "My First Post",
                    "content": "This is the content of the post.",
                    "published": True,
                    "created_at": "2024-11-16T12:00:00",
                    "owner_id": 1,
                    "owner": {
                        "id": 1,
                        "email": "user@example.com",
                        "created_at": "2024-11-16T12:00:00",
                    },
                },
                "votes": 10,
            }
        }
    )


class UserCreate(BaseModel):
    email: EmailStr = Field(..., description="Email address of the user")
    password: str = Field(..., description="Password for the user")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "newuser@example.com",
                "password": "SecurePassword123!",
            }
        }
    )


# class UserLogin(BaseModel):
#     email: EmailStr = Field(..., description="Email address of the user")
#     password: str = Field(..., description="Password for the user")

#     model_config = ConfigDict(
#         json_schema_extra={
#             "example": {
#                 "email": "user@example.com",
#                 "password": "SecurePassword123!",
#             }
#         }
#     )


class Vote(BaseModel):
    post_id: int = Field(..., description="ID of the post that the vote is for", ge=1)
    dir: conint(le=1) = Field(..., description="Direction of the vote, 1 for upvote, 0 for downvote") # type: ignore

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "post_id": 123,
                "dir": 1,
            }
        }
    )


class Token(BaseModel):
    access_token: str = Field(..., description="The access token for authentication")
    token_type: str = Field(..., description="Type of token, usually 'bearer'")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "access_token": "access-token-123",
                "token_type": "bearer",
            }
        }
    )


class TokenData(BaseModel):
    id: int = Field(..., description="User ID associated with the token")
