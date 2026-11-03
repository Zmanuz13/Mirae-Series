#Mirae 4 V1
import json
import random
with open("domande_corea_100.json", "r", encoding="utf-8") as f:
    selezione = json.load(f)
domanda_selezionata=random.sample(selezione,20)
def domanda():
    print(domanda_selezionata)
    risposta=input("Risposta?:")
    if risposta=="":

print("Benvenuto al test del Vero Coreano 2.0!")



