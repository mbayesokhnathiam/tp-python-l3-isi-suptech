#Créer deux variables <distance> et <temps>.
# distance = 90km et temps = 3h
#Calculer la vitesse en km/h et m/s.

#Calcul de la vitesse en km/h.

distance = 90 #(unité: km)
temps = 3 #(unité: heure)

#1. Calcul de la vitesse en km/h

#Formule v = d/t
vitesse1 = distance / temps

print("La vitesse en Km/h est : ",vitesse1, " km/h")

#1. Calcul de la vitesse en km/h

#Conversion

mdistance = distance * 1000
mintemps = temps * 3600

#vitesse m/s

vitesse2 = mdistance / mintemps
print("La vitesse en m/s est : ",vitesse2, " m/s")
