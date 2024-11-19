anniserv=int(input("quanti anni di servizio? "))
lvlpro=int(input("livello programmatore? (1,2,3) "))

if lvlpro==1:
 if anniserv==1:
  bonus=100
 elif lvlpro<=3:
  bonus=200
 elif lvlpro<=5:
  bonus=300
 elif lvlpro<=7:
  bonus=400
 else:
  bonus=500


if lvlpro==2:
  if anniserv==1:
   bonus=200
  elif anniserv<=3:
    bonus=300
  elif anniserv<=5:
    bonus=400
  elif anniserv<=7:
    bonus=500
  else:
    bonus=600

if lvlpro==3:
 if anniserv==1:
  bonus=300
 elif anniserv<=3:
  bonus=400
 elif anniserv<=5:
  bonus=500
 elif anniserv <=7:
  bonus=600
 else:
  bonus=700
else:
 print("livello programmazione non valido")

print("il tuo bonus è di: ", bonus)