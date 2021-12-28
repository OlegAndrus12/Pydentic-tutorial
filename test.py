from pydentic import BaseModel, ValidationError

class City(BaseModel):
    city_id: int
    name: str


input_json = """
{
    "city_id":"1",
    "name": "Lviv",
}
"""

try:
    city = City.parse_raw(input_json)
except ValidationError as e:
    print(e.json())