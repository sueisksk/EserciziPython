FASCINE = 5
SACCHI = 20
BANCALI = 50
SPESE_DI_TRASPORTO = 3
numeroTot = int(input("Inserisci il numero di FASCINE "))
numeroTot2 = int(input("Inserisci il numero di SACCHI "))
numeroTot3 = int(input("Inserisci il numero di BANCALI "))
totaleKg = (FASCINE*numeroTot + SACCHI*numeroTot2 + BANCALI*numeroTot3)
print(f"il totale di kg è: {totaleKg} ")
spesaTotale = (totaleKg*0.8)+(SPESE_DI_TRASPORTO)
print(f"il costo totale è: {spesaTotale}€ ")
if (totaleKg>100):
   sconto = (spesaTotale*15 /100)
   print(f"lo sconto applicato è:{sconto} € ")
   spesaTotale = spesaTotale - (spesaTotale*15 /100)+(SPESE_DI_TRASPORTO)
   print(f"il prezzo finale su scontrino è: {spesaTotale} €")
   print(f"le spese di trasporto sono: {SPESE_DI_TRASPORTO}€ ")