#exercice 1: 
# on demande une fonction qui fait la rotation des éléments dans la liste.
def rotation_droite(lst):
    temp=lst[0]                #on sauve le dernier élément dans une variable
    del(lst[0])
    lst.append(temp)                          
    return(lst)
#exercice 2 : 
#modifier ce programme pour que la rotation se fait par pas à déterminer par l'utilisateur
# pas=int(input("donner le pas de décalage : "))
# for i in range(0,pas):
#     temp=liste[len(liste)-1]
#     for i in range(len(liste)-1,0,-1):
#         liste[i]=liste[i-1]
#     liste[0]=temp
# print(liste)
#exercice 3 : 
#ecrire un programme qui code un texte suivant un autre texte considéré comme clé
#exemple : texte="bonjour le monde"     cle="ntic"
# résultat attendu : texte_code="nticnti cn ticnt"
def texte_cle(txt,cle):
    texte_code=""
    j=0 #compteur pour la clé
    for i in range(len(txt)): #boucle qui parcour le texte original
        if txt[i]==" ":   #si la boucle rencontre un espace dans le texte, il affecte cet espace au texte codé
            texte_code+=" "
        else:
            texte_code+=cle[j] #si la boucle rencontre une lettre elle affecte une lettre de la clé au texte codé de même ordre
            j+=1
            if j==len(cle): #si la clé se termine, alors on recommence le mot clé à 0
                j=0
    return(texte_code)

#exercice 4 :
#on demande un programme qui construit une matrice d'alphabets à partir d'une liste d'alphabets à condition
#qu'avant chaque nouvelle ligne, la liste reçois une rotation comme à l'exercice 1

alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def matrix_building(lst):
    matrice=[]
    for i in range(0,26):
        matrice.append(lst[:])
        rotation_droite(lst)      
    return(matrice)
#exercice 5 :
#avec les fonctions précédements réalisées, ecrire la fonction qui permet le cryptage d'un texte en 
# utilisant la fonction texte_cle
def crypted_text_building(txt,txt_cle):
    txt_crypte=""
    x,y,i=0,0,0
    matrice=matrix_building(alphabets)
    while i<len(txt):
        if txt[i]==" ":#si le texte contient un espace, l'ajouter aussi au texte crypté
            txt_crypte+=" "
        else:
            for j in range(len(alphabets)):#chercher l'indice de la lettre en cours et
                if txt[i].lower()==matrice[0][j]:#stocker son indice dans la variable x
                    x=j
            for k in range(len(alphabets)):#chercher l'indice de la lettre en cours et
                if txt_cle[i].lower()==matrice[k][0]:#stocker son indice dans la variable y
                    y=k
            txt_crypte+=matrice[x][y] #la lettre dans la matrice aux indices x et y l'ajouter
            # au texte crypté
        i+=1
    return txt_crypte
#test

#exercice 6 :
# on vous demande maintenant de faire la fonction qui permet le décryptage d'un message à l'aide du même
# clé
def decrypted_coded_text_building(ctxt,txt_cle):
    txt=""
    x,y,i=0,0,0
    matrice=matrix_building(alphabets)
    while i<len(ctxt):
        if ctxt[i]==" ":
            txt+=" "
        else:
            for j in range(len(alphabets)):
                if txt_cle[i].lower()==matrice[j][0]:
                    y=j
            for k in range(len(alphabets)):
                if ctxt[i].lower()==matrice[y][k]:
                    x=k
            txt+=matrice[0][x]
        i+=1
    return txt
# # #exercice 7 :  
# # faites les tests nécessaires pour s'assurer du bon fonctionnement des fonctions
# # exemple texte crypté : ohvlbnz nr fwpqx
reponse='o'
while reponse=='o':
    choix=input("Quel opération voulez vous effectuer ? cryptage ou décryptage (c/d) : ") 
    if choix=='c':
        texte=input("Donner le text à crypter : ")
        cle=input("Donner une cle de cryptage sans espaces : ")
        txt_cle=texte_cle(texte,cle)
        txt_crypted=crypted_text_building(texte,txt_cle)
        print(txt_crypted)
    elif choix=='d':
        ctexte=input("Donner le text à décrypter : ")
        cle=input("Donner la cle utilisée dans le cryptage : ")
        txt_cle=texte_cle(ctexte,cle)
        txt_decrypted=decrypted_coded_text_building(ctexte,txt_cle)
        print(txt_decrypted)
    else:
        print("reponse incorrecte !")
    reponse=input("voulez vous recommencer ? (o/n)")



