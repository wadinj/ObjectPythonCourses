# TP seul
# L'objectif de ce TP est de faire une machine à sous cmd !
# La machine à sous est un tableau à deux dimensions de longueur 5 et largeur 5.
# Il y a quatres possibilités dans votre machine à sous (chaque possibilité est un emoji à prendre ici: https://emojipedia.org/)
# Votre machine à sous doit prendre un nombre de joueurs et initialiser une machine pour chacun.
# Le jeu est tour par tour, chaque joueur lance un coup de machine à son tour
# A chaque tour, le joueur doit choisir quel émoji bloqué.
# Le jeu s'arrête lorsqu'il y a un vainqueur (une ligne complète du même emoji)


# Améliorations:
# 1. Permettre au joueur de tout relancer sans choisir un emoji
# 2. Prendre en paramètre (args) la taille de la machine à sous
# 3. Développer une IA (la plus simple possible) permettant d'ajouter des joueurs "machine"
# 4. Ajouter un menu contextuel présentant le Casino EPSI Lille et permettant de naviguer vers la machine à sous

# Remplacer le deuxième joueur par un joueur IA 
# Ajouter un budget lors du lancement du casino (Crédits: 10)
# Lors du lancement de la machine à sous, demandez le nombre de crédit que vous souhaitez jouer
# Ajouter un menu contextuel avec les options des différents jeux (pour l'instant juste la machine à sous) ainsi que le nombre de crédits du joueur
# Permettre de revenir au menu à chaque fin de partie de machine à sous

# Développez le jeu BlackJack
# Fonctionnement :
    # > Demander le montant de la mise
    # > Tirer une carte pour le croupier et l'afficher
    # > Tirer deux cartes pour le joueur et lui montrer, proposer si le joueur souhaite encore des cartes 
    # > Si oui, tirer des cartes tant qu'il souhaite. Si le joueur dépasse 21 il a perdu.
    # > Si le joueur s'arrête, tirer des cartes pour le croupier jusqu'a sa victoire