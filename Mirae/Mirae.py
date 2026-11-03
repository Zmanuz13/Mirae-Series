#Primo progetto serie Mirae(미래)
print("\033[34m")
print ("Benvenuto alla calcolatrice Mirae!")
def addizione():
    return x+y
def sottrazione():
    return x-y
def moltiplicazione():
    return x*y
def divisione():
    if y!=0:
        return x/y
    else:
        return "Errore:Divisione per 0"
def elevazione():
    return x**y
while True:
    print("Scegli l'operazione:")
    print("1. Addizione (+)")
    print("2. Sottrazione (-)")
    print("3. Moltiplicazione (*)")
    print("4. Divisione (/)")
    print("5. Elevazione a potenza (^)")

    operazione=int(input("Scegliere operazione:"))
    x=float(input("Scegli numero(1):" ))
    y=float(input("Scegli numero(2): "))
    if operazione==1:
        print (addizione())
    elif operazione==2:
        print (sottrazione())
    elif operazione==3:
        print (moltiplicazione())
    elif operazione==4:
        print(divisione())
    elif operazione==5:
        print (elevazione())
    continuo=input("Continuare?SI|NO:").lower()
    if continuo not in ("si","sì","s","i","ì"):
        print("Arrivederci")
        break
    else:
        continue
