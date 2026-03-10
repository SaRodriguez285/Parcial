from enum import Enum, auto
from datetime import date

class Material(Enum):
    BRONCE = auto()
    PLATAA = auto()
    ORO = auto()

class Caballero:
    def __init__(self, id: int, name: str, material: Material, attack: int, constelation: str):
        self.id = id
        self.name = name
        self.material = material
        self.attack = attack
        self.constelation = constelation

    def showCaballero(self):
        return {
            "id": self.id,
            "name": self.name,
            "material": self.material.name,
            "attack": self.attack,
            "constelation": self.constelation
        }

    def figthCaballero(self, other: "Caballero"):
        return f"{self.name} lucha contra {other.name}. Ganador: {self.name if self.attack >= other.attack else other.name}"

    def showconstelation(self):
        return f"{self.name} pertenece a la constelación {self.constelation}"

    def showYourCaballero(self, date: date):
        return f"Caballero {self.name} registrado en la fecha {date}"