from pydantic import BaseModel


class UserResponse(BaseModel):
    authToken: str


class OrderProduct(BaseModel):
    id: int
    quantity: int


class OrderResponse(BaseModel):
    id: int
    userId: int
    productsList: list[OrderProduct]
    status: int
