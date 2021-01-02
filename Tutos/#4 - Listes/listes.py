from random import shuffle

# Générateur de phrases
# demander en console une chaine de la forme "mot1/mot2/mot3/mot4"
chained_words = input("Entrer une chaine de la forme mot1/mot2/mot3/mot4")

# transformer cette chaine en liste
words = chained_words.split("/")

# la mélanger
shuffle(words)

# récupérer le nombre elements
words_len = len(words)

# si le nombre d'éléments de cette liste est inférieur à 10
if words_len < 10:
    # afficher les deux premiers mots
    print(words[0], words[1])

# si le nombre d'éléments est supérieur ou égal à 10
else:
    # afficher les 3 derniers
    print(words[words_len - 1], words[words_len - 2], words[words_len - 3])
