venditeMax = [900, 890,967]
venditeMin = [500,320,446]
negozi = ["negozio1","negozio2","negozio3"]
sommaVenditeMin = 0
sommaVenditeMax = 0
for i in range (len(venditeMin)):
    sommaVenditeMin+=venditeMin[i]
for i in range (len(venditeMax)):
    sommaVenditeMax+=venditeMax[i]
mediaVenditeMin= sommaVenditeMin/len(venditeMin)
mediaVenditeMax= sommaVenditeMax/len(venditeMax)

print(f"la media delle vendite minime: {mediaVenditeMin}, invece la media delle vendite massime: {mediaVenditeMax}")
for i in range (len(negozi)):
    if venditeMin[i]<mediaVenditeMin:
        print(f"{negozi[i]}, ha registrato una vendita minima inferiore alla media delle vendite minime ")
domanda = "negozio3"
presente = False
for i in range(len(negozi)):
    if domanda in negozi:
        presente=True
    else:
        presente=False
if presente==True:
    print(f"{domanda} è presente nell'array di negozi ")
else:
    print(f"il {domanda} non è presente nell'array di negozi ")
venditaPiuAltaNome = " "
venditaPiuAlta = venditeMax[0]
for i in range (len(venditeMax)):
    if venditeMax[i]>venditaPiuAlta:
        venditaPiuAlta=venditeMax[i]
        venditaPiuAltaNome=negozi[i]
venditaPiuBassa=venditeMin[0]
venditaPiuBassaNome = " "
for i in range (len(venditeMin)):
    if venditeMin[i]>venditaPiuBassa:
        venditaPiuBassa=venditeMin[i]
        venditaPiuBassaNome=negozi[i]
