from pydantic import BaseModel, ValidationError

class Character(BaseModel):
    name: str
    level: int
    damage: int

try:
    elegy = Character(name='Elegy', level=1, damage=5 )
except ValidationError as e:
    print(e.json())

# else:
#     print(f"Name: {elegy.name}")
#     print(f"Level: {elegy.level}")
#     print(f"Damage: {elegy.damage}")