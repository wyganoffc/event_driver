from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    """Модель пользователя"""
    id: int = Field(gt=0, description="Номер пользователя")
    name: str = Field(min_length=1, max_length=50, description="Имя пользователя")

class ProductSchema(BaseModel):
    """Модель товара"""
    id: int = Field(gt=0, description="Номер товара")
    name: str = Field(min_length=1, max_length=200, description="Название товара")
    salesman: str = Field(min_length=1, max_length=50, description="Продавец")

class OrderSchema(BaseModel):
    """Модель заказа"""
    id: int = Field(gt=0, description="Номер заказа")
    customer: UserSchema

class OrderItemSchema(BaseModel):
    """Модель товара по номеру"""
    id: int = Field(gt=0, description="Номер заказа")
    product: ProductSchema