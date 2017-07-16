import random
try:
    containerAnzahl = int(input("Geben Sie die Anzahl der Container an: "))
except ValueError:
    containerAnzahl = int(input("Geben Sie eine ZAHL ein: "))
        
waggonAnzahl = containerAnzahl

listeContainer = []
listeWaggon = []
listeGeordnet = []
for i in range(1,containerAnzahl+1):
    listeContainer.append(i)
for i in range(1,waggonAnzahl+1):
    listeWaggon.append(i)

random.shuffle(listeContainer)
    
print(listeContainer)
print(listeWaggon)    

def minimaleBewegungen(liste):
    differenz = 0
    summe = 0
    for i in range(0,containerAnzahl):
        differenz = abs(int(listeContainer[i]) - int(i)-1)
        summe = summe + differenz
    return summe
    


def fertig():
    fertig_ = False
    if len(listeGeordnet) == len(listeContainer):
        fertig_ = True
    return fertig_
    
def pruefenObElementSchonInDritterListe(elem):
    return_ = False
    for i in range(0,len(listeGeordnet)):
        if listeGeordnet[i] == elem:
            return_ = True
    return return_
    
def indexZumHinzufuegen(elem):
    index_ = 0
    for i in range(0,len(listeGeordnet)):
        if elem > listeGeordnet[i]:
            index_ += 1
        else:
            break
            
    return index_
        

def match():
    pos=0
    ende = False
    #SummeBewegungen = 0
    while ende == False:
        ende = fertig()        
        if pruefenObElementSchonInDritterListe(listeContainer[pos]):
            if (pos + 1) <= len(listeContainer) -1:
                pos += 1
                #SummeBewegungen += 1
        else:
            indexVar = indexZumHinzufuegen(listeContainer[pos])
            #if listeContainer[pos] != (pos + 1):
             #   SummeBewegungen += abs(listeContainer[pos] - pos-1)
            
            listeGeordnet.insert(indexVar,listeContainer[pos])
            pos = listeContainer[pos] -1
            print("\n")
            print("*****Liste Geordnet*****")
            print(listeGeordnet)
            print("*****Liste Container*****")
            print(listeContainer)
            print("*****Liste Waggons*****")
            print(listeWaggon)
    #SummeBewegungen += abs(pos-1-1)        
    #print("Die benötigten Bewegungen waren: " + str(SummeBewegungen))
        
                
        
        
        
minimaleZuege = minimaleBewegungen(containerAnzahl)
print("Die Anzahl der minimalen Bewegungen beträgt: " + str(minimaleZuege))
match()
   