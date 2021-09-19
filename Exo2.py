"""fonction position(L,e) qui admet en paramètres une liste Liste d'entiers et un entier e et 
retourne l'indice de l'entier e dans la liste"""
def position(liste:list,elt:int)->int:
    posit=-1
#si la liste il est vide en renvoi -1    
    taille2list = len(liste)
    if taille2list==0:
            posit=-1
    for i in range(taille2list) :
        if elt==liste[i]:
            posit=i
    return posit
"""fonction nb_occurrences quiretourne le nombre d'occurrences de l'entier elt dans la liste"""
def nb_occurence(liste:list,elt:int)->int:
    nbr_occ=0
    for i in range(len(liste)):
        if elt==liste[i]:
           nbr_occ=nbr_occ+1
    return nbr_occ  
"""fonction trie qui retourne un 
booléen vrai si la liste est triée par ordre croissant, faux sinon avec boucle while"""
def est_Triewhile(liste:list)->bool:
    i = 1
    if len(liste) < 0:
        listeEstTriee = False
    else:
        listeEstTriee=True
    while i < len(liste):
            if liste[i-1] > liste[i]:
                listeEstTriee = False
            i+=1
    return listeEstTriee
    
"""fonction trie qui retourne un 
booléen vrai si la liste est triée par ordre croissant, faux sinon avec boucle For"""
def est_trie_for(liste:list)->bool:      
    if liste==[] :
        trie=False
    else:
        trie= True    
    for i in range(1,len(liste)):
           if liste[i-1]>liste[i]:
                trie=False
                
    return trie            
"""fonction trie qui retourne un 
booléen vrai si la liste est triée par ordre croissant, faux sinon avec boucle For versionchoisit"""   
def listeTrie_version_bon(liste:list)->bool:
    if liste==[]:
        esttrie=False
    else :
        esttrie=True        
    for i in range(1,len(liste)):
        if liste[i-1]>liste[i] :
             esttrie=False                
    return esttrie
def positiontrie(liste:list,e:int)->int:
    posit=-1
#si la liste il est vide en renvoi -1    
    taille2liste = len(liste)
    if taille2liste==0:
        posit=-1
    if est_trie_for:    
     for i in range(taille2liste) :
        if e==liste[i]:
            liste = sorted(liste) #Liste trie
            posit=i
    return posit  
"""fonction repetition de valeur True si la liste Liste comporte des répétitions de valeurs et False sinon."""    
def repetitions(liste: list)-> bool:
    T = []
    rep = False
    i = 0
    while(not rep and i < len(liste)):
        e = liste[i]
        if e not in T:
            T.append(liste[i])
            i += 1
        else:
            rep = True
    return rep   
""" fonction separerliste qui prend en paramètre une liste d'entiers et retourne la 
liste LSEP cases des zéros sont situées entre les nombres négatifs et les nombres positifs."""       
def separer(liste:list)->list:
    lsep=[]
    negatif=0
    for e in liste:
        if e<0:
            lsep.insert(0,e)
            negatif=negatif+1
        elif e>0:
                lsep.append(e)
        else:
            lsep.insert(negatif,0)
    return lsep   

"""fonction test de tout le fonction Exo2"""

def test():
    s=[1,2,3,4,-1,-7]
    print("la position de indice de la liste numero 5 est:",position(s,5))  
    print("la position de indice de la liste numero 5 est:",position(s,1))  
    print("la position de indice de la liste numero 5 est:",position(s,6))  
    print("la position de indice de la liste numero 5 est:",position([],5))
    print("la liste s est:",s)
    print("occurence de la liste numero 2 dans la liste s est:",nb_occurence(s,2))
    print("trie  de la liste s avec bucle for est:",est_trie_for(s))   
    print("trie  de la liste s avec bucle for est:",listeTrie_version_bon(s))  
    print("trie  de la liste s avec bucle while est:",est_Triewhile(s)) 
    print("position_trie est:",positiontrie(s,2))
    print("repetition dans la liste est:",repetitions(s)) 
    print("separation dans la liste est:",separer(s))
test()     
            
            