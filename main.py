import numpy as np

#è un elenco di elementi
a1 = np.array([1,2,3,4,5,6,7])
print ("a1",a1)

#divide da 0 a 100 (primi 2 numeri) in 5 punti (ultimo numero)
a2 = np.linspace(0,100,21)
print ("a2",a2)

#crea un array di 8 (numero) zeri
a3 = np.zeros(8)
print ("a3",a3)

#crea un array di 8 (numero) uni
a4 = np.ones(8)
print ("a4",a4)

#crea un array di numeri cauali da 1 a 0 di 2 (numero) rige e 3 (numero) colonne (la lettura è sempre righe colonne, in ogni cosa)
#il *15 ti permette di moltipricare ogni numero generato per "15" (o qualsiasi altro numero)
r1 = np.random.rand(2,3)*15
print ("r1",r1)

np.random.seed(8)
r2 = np.random.rand(2,3)
print ("r2",r2)


r3 = r1.reshape (3,2)
print ("r3",r3)