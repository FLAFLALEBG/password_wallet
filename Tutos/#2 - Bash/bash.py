import os

tube = os.popen('date +%A-%d-%B-%Y')
# on récupère la première ligne :
bash = tube.read()
# on retire le dernier caractère qui est un « retour à la ligne ».
maDate = bash[:-1]
# on vérifie :
print("Nous sommes le :", maDate)

