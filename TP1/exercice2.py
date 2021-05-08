#Abdou quitte Dakar à 10h58mn et arrive au Kenya à 23h18mn.
#Faites un programme qui calcule et affiche le temps parcourru.

hdepart = (10 * 60) + 58 #(unité en minutes)
harrivee = (23*60) + 18 #(unité en minutes)

temps = harrivee - hdepart

nbheure = temps // 60
nbmin = temps % 60

print("Le temps mis est ",nbheure,"h",nbmin,'min')