"""fonction somme avec trois version de boucle for range ou e in liste et boucle while """
def somme1(liste:list)->int:
    somme=0
    for i in range(len(liste)):
#range elle retoune de nombre et len ce la taille de liste         
        somme=somme+liste[i]
    return somme
def somme2(liste:list)->int:
    somme=0
# e in l c'est une versiom plus simple car tu es deja a interieur de liste    
    for e in liste:
        somme=somme+e
    return somme        
def somme3(liste:list)->int:
# boucle while il faut initialiser i toujous et alors cette i est inferieur a la taille de liste     
    somme=0
    i=0
    while i<len(liste):
        somme=somme+liste[i]
        i=i+1
    return somme 
"""fonction pour calculer moyen de la liste moyenne ce float toujours son type de retour comme ca on es bien sur"""       
def moyenne(liste:list)->float:
    moy=0    
#la fonction doit renvoyer 0 ca veux dire que tout ce que / doit etre different de 0
#le moyen c'est la somme de la liste divise par la taille de la liste
    if len(liste)!=0:
        moy=somme1(liste)/len(liste)
    return moy  
"""pour calculer nbr superieur avec range avec taille de liste len et version normal e in liste"""
def nbr_sup(liste:list,elt:int)->int:
    nb_valeur=0
    for i in range(len(liste)):
#on peux faire la calcul de difference avec la variable donner en parametre exemple elt     
        if liste[i]>elt:
            nb_valeur=nb_valeur+1
    return nb_valeur    
def nbr_sup2(liste:list,elt:int)->int:
    nb_valeur=0
 #quand il sagit de version simple on deja dans la liste on peux faire directement calcule avec element dans la dans la liste    
    for i in liste:
        if i>elt:
            nb_valeur=nb_valeur+1
    return nb_valeur
"""fonction pour calculer la moyen superieur"""  

def moy_sup(liste:list,e:int)->float:
    moyen_sup=0
    somme_sup=0
    nbr_valeur=0
    for i in liste:
        if i>e:
#on va stocker le nombre superieur puis on calcule la sommme de cette nombre on sort de if et on calcule la moyen superieur             
            nbr_valeur=nbr_valeur+1
            somme_sup=somme_sup+i
    if nbr_valeur!=0:
        moyen_sup=somme_sup/nbr_valeur  

    return moyen_sup

"""fonction pour valeur maximal"""    

def val_max(liste:list)->int:
    max=0
#pour calculer la valeur maximal de element de liste 
    for e in liste :
        if e>max:
            max=e
    return max
"""fonction pour calculer indice de la liste"""
def ind_max(liste:list)->int:
    maxid=0
# pour calculer indice de la liste il faut utiliser range car se mieux on a la taille len et puis on calcule mac index      
    for i in range(len(liste)):
        if i>maxid:
            maxid=i
    return maxid        

def test():
    s=[1,2,7,8,4]
#Quand on une seul parametre il faut donne avec le parametre et si il faut la valeur de la liste [1,2,7,8,4]     
    print("la somme1 est",somme1(s))
    print("la somme2 est",somme2(s))
    print("la somme3 est",somme3(s))
    print("la moyenne est",moyenne(s)) 
#Quand on fait appel a la fonction il faut saisir tout les parametre donner exe;ple nbr_sup(s,4) 
    print("le nombre superieur avec range est",nbr_sup(s,6)) 
    print("le nombre superieur2 avec version simple est",nbr_sup2(s,6)) 
    print("le moyen superieur est",moy_sup(s,6))
    print("la valeur maximal est:",val_max(s))
    print("la valeur indice maximal est:",ind_max(s))


test()    