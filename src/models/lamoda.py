from pydantic import BaseModel, Field


class Sneakers(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    brand: str = Field(min_length=1, max_length=30)
    price: float = Field(gt=0)

    class Config:
        schema_extra = {
            'example': {
                'name': 'Sneakers',
                'brand': 'Nike',
                'price': 209.99
            }
        }
