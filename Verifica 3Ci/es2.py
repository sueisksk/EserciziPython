oreP = [10,11,13,15,17]
oreA = [11,14,18,19,20]
for i in range(len(oreA)):
    if oreA[i]>oreP[i]:
        print("ora di arrivo maggiore dell'ora di partenza")

destinazioni = ["Roma","Firenze","Milano","Foggia","Palermo"]
destinazione = " "
n = int(input("quante città vuoi chiedere l'ora di partenza: "))
i=0
while i<n:
    destinazione=str(input("quale destinazione vuoi"))
    for i in range(len(destinazioni)):
        if destinazione == destinazioni[i]:
            print(f"l'ora di partenza per {destinazione} è {oreP[i]}")
        else:
            print(f"la destinazione {destinazione} non è tra le scelte ")
i=0
r = int(input("inserisci quanti voli vuoi chiedere in un intervallo di tempo: "))
while i<r:
    oreDiPartenza = int(input("inserisci l'orda di partenza: "))
    oreDiArrivo = int(input("inserisci un orario di arrivo: "))
    for i in range(len(oreA)):
        if oreDiPartenza>=oreP[i] and oreDiArrivo<=oreA[i]:
            print(f"il volo per {destinazioni[i]} è nell'intervallo di tempo")


