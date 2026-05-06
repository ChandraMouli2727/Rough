from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class AvailableCuisines(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"

food_items = {
    "indian": ["Samosa", "Dosa"],
    "american": ["Hot dog", "Apple pie"],
    "italian": ["Pizza", "Pasta"]
}

@app.get("/items/{cuisine}")
async def items(cuisine: AvailableCuisines):
    return {"cuisine": cuisine, "items": food_items[cuisine.value]}


coupon_code = {
    1:'10%',
    2:'20%',
    3:'30%'
}
#http://127.0.0.1:8080/docs
#http://127.0.0.1:8080/redoc
#explore fastapi.tiangolo
#benefit 1 : Inbuilt data validation
#benefit 2 : Inbuilt documentation support
# benefit 3 : run time performance speed/fast running performance
#benefit 4 : code compacted development speed is fast / less time to write code,few bugs
@app.get("/get_coupon/{code}")
async def get_items(code:int):
    return {'discount_amount ': coupon_code.get(code)}