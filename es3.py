### Esercizio 3b

#Creare un programma che calcoli la media dei lanci validi di un atleta di lancio del giavellotto in una gara; l’atleta ha a disposizione 5 lanci,
#di cui l’utente dovrà inserire la lunghezza, nel caso di lanci nulli l’utente inserirà zero
#per quei lanci e quei lanci non dovranno essere contati nel calcolo della media.
#Il programma restituirà la media dei lanci all’utente.


lancio1=float(input("inserisci la lunghezza del primo lancio "))
lancio2=float(input("inserisci la lunghezza del secondo lancio "))
lancio3=float(input("inserisci la lunghezza del terzo lancio "))
lancio4=float(input("inserisci la lunghezza del quarto lancio "))
lancio5=float(input("inserisci la lunghezza del quinto lancio "))

if lancio1 == 0:
 print((lancio2+lancio3+lancio4+lancio5)/4)
elif lancio2==0:
 print((lancio1+lancio3+lancio4+lancio5)/4)
elif lancio3==0:
 print((lancio1+lancio2+lancio4+lancio5)/4)
elif lancio4==0:
 print((lancio1+lancio2+lancio3+lancio5)/4)
elif lancio5==0:
 print((lancio1+lancio2+lancio4+lancio3)/4)
else:
 print((lancio1+lancio2+ lancio3+lancio4+lancio5)/5)

 
 
