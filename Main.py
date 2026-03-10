from fastapi import FastAPI
from datetime import date
from models import Caballero, Material 

app = FastAPI()

caballero1 = Caballero(1, "Camus de Acurio", Material.BRONCE, 80, "Pegaso")
caballero2 = Caballero(2, "Mu de Aries", Material.PLATAA, 85, "Dragón")
caballero3 = Caballero(3, "Shaka de Virgo", Material.ORO, 90, "Deidad")

@app.get("/caballero/show")
def show_caballero():
    return caballero1.showCaballero()

@app.get("/caballero/fight1")
def fight_caballero():
    return {"resultado": caballero1.figthCaballero(caballero2)}

@app.get("/caballero/fight2")
def fight_caballero():
    return {"resultado": caballero1.figthCaballero(caballero3)}

@app.get("/caballero/fight3")
def fight_caballero():
    return {"resultado": caballero2.figthCaballero(caballero3)}

@app.get("/caballero/constelation")
def show_constelation():
    return {"constelacion 1": caballero1.showconstelation(), 
            "constelacion 2": caballero2.showconstelation(), 
            "constelacion 3": caballero3.showconstelation()}

@app.get("/caballero/showYour")
def show_your_caballero():
    return {"mensaje": caballero1.showYourCaballero(date.today())}