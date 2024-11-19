### Esercizio 2b
#Realizzare un programma che permetta il calcolo
#della media di tre voti dati in decimi.
#La media deve essere fornita in decimi o
#centesimi a seconda della scelta effettuata
#dall'utente. (Per ottenere la media in centesimi basta moltiplicare la
#media in decimi per 100/10)

num1=float(input("inserisci il primo numero: "))
num2=float(input("inserisci il secondo numero: "))
num3=float(input("inserisci il terzo numero: "))
decisione=str(input("vorresti la media in decimi o centesimi? "))

if decisione=="decimi":
 mediadecimi=round(num1+num2+num3)/3
 print("la media in decimi è ", mediadecimi)
elif decisione=="centesimi":

 mediacentesimi=round(mediadecimi*100/10)
 print("la media in centesimi è ",mediacentesimi)


 