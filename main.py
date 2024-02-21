from random import randint

def Personnage(nom_classe, points_de_vie, attaque, nom):
    return {
        'nom_classe': nom_classe,
        'points_de_vie': points_de_vie,
        'attaque': attaque,
        'nom': nom,
        'defense_active': False
    }
    
def combat(personnage, monstre):
    print(f"Vous êtes en combat avec {monstre}!")

    while True:
        print("Que voulez-vous faire ?")
        print("1. Attaquer")
        print("2. Fuir")
        print("3. Se défendre")
        print("4. Continuer vers d'autre monstre")

        choix = input("Entrez le numéro de votre choix : ")

        if choix == "1":
            if attaquer(personnage,monstre):
                break
        elif choix == "2":
            print("Vous avez décidé de fuir. Bonne chance la prochaine fois!")
            return False
        elif choix == "3":
            defendre(personnage,monstre)
        elif choix == "4":
            print("Vous décidez de continuer vers d'autres monstres.")
            return False
        else:
            print("Action non valide. Réessayez.")

def attaquer(personnage, monstre):
        print(f"Vous attaquez {monstre['nom']} !")
        monstre['points_de_vie'] -= personnage['attaque']

        if monstre['points_de_vie'] <= 0:
            print(f"{monstre['nom']} est mort !")
            return True
        else:
            print(f"{monstre['nom']} a {monstre['points_de_vie']} points de vie restants.")
            subir_attaque(personnage,monstre)
            return False

def subir_attaque(personnage, monstre):
    print(f"{monstre['nom']} contre-attaque !")
    personnage['points_de_vie'] -= monstre['attaque']
    print(f"Vous avez maintenant {personnage['points_de_vie']} points de vie restants.")

    if personnage['points_de_vie'] <= 0:
        print("Vous avez été vaincu...")
        exit()

def defendre(personnage, monstre):
    print(f"Vous vous défendez face à {monstre['nom']}.")
    personnage['defense_active'] = True
    subir_attaque(personnage, monstre)
    personnage['defense_active'] = False

def victoire():
        print("Vous avez vaincu le monstre et continuez votre aventure.")
        return True
    

def creer_monstres():
    return [
        {'nom_classe': "Vampire", 'points_de_vie': 4, 'attaque': 2, 'nom': "Vampire", 'position': (5, 0)},
        {'nom_classe': "Vampire", 'points_de_vie': 4, 'attaque': 2, 'nom': "Vampire", 'position': (5, 2)},
        {'nom_classe': "Goule", 'points_de_vie': 3.5, 'attaque': 1.5, 'nom': "Goule"'position': (5, 1)},
        {'nom_classe': "Goule", 'points_de_vie': 3.5, 'attaque': 1.5, 'nom': "Goule"'position': (5, 3)},
        {'nom_classe': "Squelette", 'points_de_vie': 4, 'attaque': 2, 'nom': "Squelette", 'position': (4, 0)},
        {'nom_classe': "Gobelin", 'points_de_vie': 4, 'attaque': 2, 'nom': "Gobelin", 'position': (4, 1)},
        {'nom_classe': "Squelette", 'points_de_vie': 4, 'attaque': 2, 'nom': "Squelette", 'position': (4, 2)},
        {'nom_classe': "Gobelin", 'points_de_vie': 4, 'attaque': 2, 'nom': "Gobelin", 'position': (4, 3)},
        {'nom_classe': "Ogre", 'points_de_vie': 4, 'attaque': 2, 'nom': "Ogre", 'position': (3, 0)},
        {'nom_classe': "Ogre", 'points_de_vie': 4, 'attaque': 2, 'nom': "Ogre", 'position': (3, 1)},
        {'nom_classe': "Ogre", 'points_de_vie': 4, 'attaque': 2, 'nom': "Ogre", 'position': (3, 2)},
        {'nom_classe': "Ogre", 'points_de_vie': 4, 'attaque': 2, 'nom': "Ogre", 'position': (3, 3)},
        {'nom_classe': "Zombie", 'points_de_vie': 4, 'attaque': 2, 'nom': "Zombie", 'position': (2, 0)},
        {'nom_classe': "Zombie", 'points_de_vie': 4, 'attaque': 2, 'nom': "Zombie", 'position': (2, 1)},
        {'nom_classe': "Zombie", 'points_de_vie': 4, 'attaque': 2, 'nom': "Zombie", 'position': (2, 2)},
        {'nom_classe': "Zombie", 'points_de_vie': 4, 'attaque': 2, 'nom': "Zombie", 'position': (2, 3)},
        {'nom_classe': "Vouivre", 'points_de_vie': 4, 'attaque': 2, 'nom': "Vouivre", 'position': (1, 0)},
        {'nom_classe': "Vouivre", 'points_de_vie': 4, 'attaque': 2, 'nom': "Vouivre", 'position': (1, 1)},
        {'nom_classe': "Vouivre", 'points_de_vie': 4, 'attaque': 2, 'nom': "Vouivre", 'position': (1, 2)},
        {'nom_classe': "Vouivre", 'points_de_vie': 4, 'attaque': 2, 'nom': "Vouivre", 'position': (1, 3)},
        {'nom_classe': "boss_final", 'points_de_vie': 15, 'attaque': 2.5, 'nom': "Boss Final", 'position': (0, 0)}
    ]

def Boss_final(nom_classe, points_de_vie, attaque, nom):
    return {
        'nom_classe': nom_classe,
        'points_de_vie': points_de_vie,
        'attaque': attaque,
        'nom': nom,
    }

def monstre_vaincu(carte, x, y):
    if len(carte[y][x]) > 0:
        carte[y][x] = ' '

def trouver_monstre_par_nom(nom_monstre, liste_monstres):
    for monstre in liste_monstres:
        if monstre['nom'] == nom_monstre:
            return monstre
    return None

def choisir_hero():
    print("Choisissez votre héros :")
    print("1. Soldat : Point de vie moyen, attaque normale")
    print("2. Chevalier : Plus de points de vie, moins d'attaques")
    print("3. Assassin : Moins de points de vie, plus d'attaques")
    while True:
        choix = input("Entrez le numéro de votre choix : ")
        if choix == "1":
            nom = input("Quel est le nom de votre Soldat ? ")
            return Personnage("Soldat", 20, 1, nom)
        elif choix == "2":
            nom = input("Quel est le nom de votre Chevalier ? ")
            return Personnage("Chevalier", 25, 0.5, nom)
        elif choix == "3":
            nom = input("Quel est le nom de votre Assassin ? ")
            return Personnage("Assassin", 15, 2, nom)
        else:
            print("Choix invalide. Veuillez choisir à nouveau.")


def choisir_direction():
    print("Choisissez la direction que vous voulez prendre : ")
    print("1. À droite")
    print("2. À gauche")
    print("3. Tout droit")
    print("4. Quitter la partie et la sauvegarder")
    return input("Entrez le numero de votre choix : ")

def introduction():
    print("Bienvenue dans le monde d'Aventuria, où de nombreux défis vous attendent !")
    print("Vous êtes un valeureux aventurier en quête de gloire et de trésors.")
    print("Votre périple commence dans le village paisible de Tornel, au cœur de la contrée mystique.")
    print("Votre quête est de sauver le royaume menacé par le Grand Dragon Ignus.")
    print("Pour cela, vous devrez affronter des créatures terrifiantes, gagner en puissance et explorer des lieux périlleux.")
    print("Prenez garde, chaque décision que vous prendrez influencera votre destinée.")
    print("Que l'aventure commence !")

def Jeu():
    
    introduction()
    
    joueur = choisir_hero()
    print(f"Vous avez choisi {joueur}. Bonne chance dans votre aventure !")

    carte = [
        ['boss_final'],
        ['Vouivre', ' ', 'Vouivre', ' '],
        ['Zombie', ' ', 'Zombie', ' '],
        [' ', 'Ogre', ' ', 'Ogre'],
        ['Squelette', 'Gobelin', 'Squelette', 'Gobelin'],
        ['Vampire',' ',' Vampire',' ']
    ]

    monstres = creer_monstres()

    position_joueur = [5, 0]
    position_boss_final = [0,0]

    while True:
        direction = choisir_direction()

        if direction == "1" or direction == "2" or direction == "3":
            
            print(f"Vous êtes face à : {carte[position_joueur[0]][position_joueur[1]]}")

            if position_joueur == position_boss_final:  
                if joueur['niveau'] < 3:
                    print("Vous n'êtes pas assez fort pour affronter le Grand Dragon Ignus.")
                    continue

                boss_final = Boss_final("Dragon", 15, 2.5, "Grand Dragon Ignus")
                print("Vous êtes face au Grand Dragon Ignus !")
                if combat(joueur, boss_final):
                    print("Vous avez vaincu le Grand Dragon Ignus ! Félicitations !")
                    break
            
            monstre_sur_case = carte[position_joueur[0]][position_joueur[1]]
            if monstre_sur_case != ' ':
                monstre_actuel = trouver_monstre_par_nom(monstre_sur_case, monstres)
                if combat(joueur, monstre_actuel):
                    victoire()
                    monstre_vaincu(carte, position_joueur[1], position_joueur[0])
                    if not monstres:
                        print("Tous les monstres ont été vaincus !")
                        break
                    else:
                        continue
            if direction == "1" and position_joueur[1] < 4:
                position_joueur[1] += 1
            elif direction == "2" and position_joueur[1] > 0:
                position_joueur[1] -= 1
            elif direction == "3" and position_joueur[0] > 0:
                position_joueur[0] -= 1
            elif direction == "4":
                if position_joueur[0] < len(carte) - 1:
                    position_joueur[0] += 1
                    print("Vous êtes descendu d'une salle.")
                else:
                    print("Vous ne pouvez pas descendre plus bas.")
            else:
                print("Direction invalide. Veuillez choisir à nouveau.")
        elif direction == "5":
            sauvegarder_avant_quitter = input("Voulez-vous sauvegarder avant de quitter ? (Oui/Non) : ")
            if sauvegarder_avant_quitter.lower() == "Oui":
                print("Sauvegarde en cours...")
                sauvegarder(joueur)
                break
        else:
            print("Direction invalide. Veuillez choisir à nouveau.")

def Regles():
    print("Le jeu est basé sur des combats simples entre des héros et des monstres.")
    print("Les héros sont des personnages créés par l'utilisateur avec un nom, une classe et des caractéristiques.")
    print("Les monstres sont des personnages générés aléatoirement avec des caractéristiques.")
    print("Durant un combat, un héros peut choisir d'attaquer un monstre. L'attaque réduit les points de vie du monstre.")
    print("Le combat se termine lorsque tous les monstres sont battus ou qu'un monstre bat le héros.")

def Credits():
    print("Les Crédits")
    print("Les createurs de ce jeu sont Jeson, Michael et Emilie. Des jeunes développeurs avec beaucoup de potentiel. ")

def menu():
    print("Bienvenue dans le jeu de combat!")
    print("Voici le menu principal :")
    print("1. Commencer une nouvelle partie")
    print("2. Reprendre une partie en cours")
    print("3. Consulter les règles du jeu")
    print("4. Découvrir les crédits du jeu")
    print("5. Quitter le jeu")

def sauvegarder(joueur):
    try:
        with open("sauvegarde.txt", "w") as fichier:
            fichier.write(f"{joueur.nom}\n")
            fichier.write(f"{joueur.points_de_vie}\n")
            fichier.write(f"{joueur.attaque}\n")
            fichier.write(f"{joueur.nom_classe}\n")
        print("Sauvegarde réussie.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")

def reprendre_partie():
    joueur_charge = charger_partie()
    if joueur_charge:
        print("Partie chargée avec succès!")
        print(f"Reprendre avec le personnage {joueur_charge.nom} {joueur_charge.nom_classe}")
        Jeu()
    else:
        print("Impossible de charger la partie. Commencez une nouvelle partie.")

def charger_partie():
    try:
        with open("sauvegarde.txt", "r") as fichier:
            nom = fichier.readline().strip()
            points_de_vie = int(fichier.readline().strip())
            attaque = float(fichier.readline().strip())
            nom_classe = fichier.readline().strip()

            return Personnage(nom, points_de_vie, attaque, nom_classe)
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée.")
        return None
    except Exception as e:
        print(f"Erreur lors du chargement de la sauvegarde : {e}")
        return None

while True:
    menu()
    choix = input("Fais ton choix : ")

    if choix == "1":
        Jeu()
    elif choix == "2":
        reprendre_partie()
    elif choix == "3":
        Regles()
    elif choix == "4":
        Credits()
    elif choix == "5":
        print("Adieu !")
        break
    else:
        print("Recommence ça n'a pas marché")
