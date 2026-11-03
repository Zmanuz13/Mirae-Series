#Mirae 2 (미래2) V3
print("\033[34m")
import requests as rq
print("Benvenuto al convertitore Mirae!")
print("Il valore viene aggiornato ad ogni avvio del programma")
print("Valute disponibili:166")
api=input("Per iniziare fornisci una chiave API:")
valori=rq.get(f"https://v6.exchangerate-api.com/v6/{api}/latest/EUR").json()
tassi = {codice.lower(): valore for codice, valore in valori["conversion_rates"].items()}
def formula(valuta1,valuta2,importo):
    return(importo / tassi[valuta1]) * tassi[valuta2]

while True:
    print("Valute consigliate:")
    print("EUR;USD,KRW;JPY,RUB,GBP,CNY;CHF,MXN,AED")
    valuta1=input("Cosa vuoi convertire?").lower().strip()
    valuta2=input("In cosa vuoi convertire?").lower().strip()
    if valuta1 in tassi and valuta2 in tassi:
        try:
            importo=(float(input("Quanto vuoi convertire?:")))
            if importo<=0:
                print("Errore:l'importo è minore o uguale a 0")
                continue
        except ValueError:
            print("Errore:il valore inserito non è un numero")
            print("Riprova")
            continue
        if valuta2 in ["krw","jpy"]:
            print(f"{importo} {valuta1}→{formula(valuta1,valuta2,importo):.0f} {valuta2}")
        else:
            print(f"{importo} {valuta1}→{formula(valuta1,valuta2,importo):.2f} {valuta2}")
        if importo==2521 and valuta1=="krw" or importo==2521 and valuta2=="krw":
            print("2521!나희도,백이진,고유림,문지웅,지승완🥚")

        continuare=input("Vuoi continuare?").lower().strip()
        if continuare in ["si", "sì", "s", "i", "ì"]:
            continue
        else:
            break
    else:
        print("Una o entrambe le valute non sono disponibili")
        print("Attento a scrivere le sigle bene!")
        print("Riprova")
        continue
#Errori da correggere:Sistema Api non completato.