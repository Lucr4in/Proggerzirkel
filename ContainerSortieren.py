import random
try:
    containerAnzahl = int(input("Geben Sie die Anzahl der Container an: "))
except ValueError:
    containerAnzahl = int(input("Geben Sie eine ZAHL ein: "))
        
waggonAnzahl = containerAnzahl

listeContainer = []
listeWaggon = []
for i in range(1,containerAnzahl+1):
    listeContainer.append(i)
for i in range(1,waggonAnzahl+1):
    listeWaggon.append(i)

random.shuffle(listeContainer)
    
print(listeContainer)
print(listeWaggon)    


def fertig():
    fertig_ = True
    for i in range(containerAnzahl):
        if listeContainer[i] != listeWaggon[i]:
            fertig_ = False
    return fertig_

def match():
    ende = fertig()
    pos=0
    while ende == False:
        ende = fertig()
        
        if pos == 0:
                elem = int(listeContainer[pos])
            
        else:
            elem = int(listeContainer[pos])
            listeContainer[pos] = elem2
            
        if elem == listeWaggon[pos]:
            pos += 1
            elem = int(listeContainer[pos])
        else:
          elem2 = int(listeContainer[elem-1])
          listeContainer[elem-1] = elem
          pos = elem2-1
          print("\n")
          print(listeContainer)
          print(listeWaggon)

match()
   