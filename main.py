import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NOMBRE_VIE = 4

vies = NOMBRE_VIE


# Demander le nombre
# Si le nombre est petit ou plus grand le préciser
# Ajouter le nombre de vie
# gerer les nombres barriere


def demander_nombre(nb_min, nb_max):

    nombre_int = 0
    while nombre_int == 0:
        print("Le nombre magique est compris entre " + str(nb_min) + " et " + str(nb_max))
        nombre_str = input("Quel est le nombre magique?")
        try:
            nombre_int = int(nombre_str)
        except:
            print("ERREUR :  Vous devez saisir un nombre!")
        else:
            if not nb_min <= nombre_int <= nb_max:
                print(f"ERREUR : le chiffre saisit soit être compris entre {nb_min} et {nb_max}")
                nombre_int = 0

    return nombre_int


# nombre = 0
# print(f"Vous avez {NOMBRE_VIE} vies et vous devez deviner le nombre magique")
# while nombre != NOMBRE_MAGIQUE and vies > 0:
#     nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
#     if nombre > NOMBRE_MAGIQUE:
#         print("le nombre magique est plus petit!")
#         vies -= 1
#         print("il vous reste " + str(vies) + " vies")
#     elif nombre < NOMBRE_MAGIQUE:
#         print("le nombre magique est plus grand!")
#         vies = vies - 1
#         print("il vous reste " + str(vies) + " vies")
#     elif nombre == NOMBRE_MAGIQUE:
#         print("Gagné : Vous avez trouvé le nombre magique!")
# if vies == 0:
#     print(f"Vous avez perdu le nombre magique était {NOMBRE_MAGIQUE}")


# faire le programme avec une boucle for :
gagne = False

print(f"Vous avez {vies} vies et vous devez deviner le nombre magique")
for i in range(0, NOMBRE_VIE):
    vies = NOMBRE_VIE - i
    print("il vous reste " + str(vies) + " vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Gagné : Vous avez trouvé le nombre magique!")
        gagne = True
        break
    elif nombre < NOMBRE_MAGIQUE:
        print("le nombre magique est plus grand!")
    else:
        print("le nombre magique est plus petit!")
#if vies == 0:

if not gagne:
    print(f"Vous avez perdu le nombre magique était {NOMBRE_MAGIQUE}")




#
# while nombre_vie != 0:
#     if not 0 < int(nombre_utilisateur) < 11:
#         print("le nombre que vous devez saisir doit être compris entre 1 et 10")
#     else:
#         if int(nombre_utilisateur) > NOMBRE_MAGIQUE:
#             print("le nombre magique est plus petit!")
#             nombre_vie = nombre_vie - 1
#             print("il vous reste " + str(nombre_vie) + " vies")
#
#         elif int(nombre_demande) < NOMBRE_MAGIQUE:
#             print("le nombre magique est plus grand!")
#             nombre_vie = nombre_vie - 1
#             print("il vous reste " + str(nombre_vie) + " vies")
#         else:
#             print("Vous avez trouvé le nombre magique!")
#             break
