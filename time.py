import time
import random as rd
from Sorting import *

def newSample(lenght):
    a = []
    for i in range(lenght):
        a.append(i)
    rd.shuffle(a)
    return a
#----------------------------------------------------------------------
deltas = {}
ln = int(input("lenght : "))
print("\n")

# selection
l = newSample(ln)
print("selection sample : done")
seconds = time.time()
l = selection(l)
deltas["selection"] = time.time() - seconds
print("selection : done\n")


# insertion
l = newSample(ln)
print("insertion sample : done")
seconds = time.time()
l = insertion(l)
deltas["insertion"] = time.time() - seconds
print("insertion : done\n")

# bulle
l = newSample(ln)
print("bulle sample : done")
seconds = time.time()
l = trieABulle(l)
deltas["bulle"] = time.time() - seconds
print("bulle : done\n")


m_strings = {"insertion" : f"insertion : {deltas.get('insertion')} sec\n", "selection" : f"selection : {deltas.get('selection')} sec\n", "bulle" : f"bulle : {deltas.get('bulle')} sec\n"}

print(f"--------\nlenght : {ln}\n")
print(f"{m_strings.get('selection')}{m_strings.get('insertion')}{m_strings.get('bulle')}")

rep = input("enregistrer(O/N)?")
if rep == "o" or rep == "O":
    #f = open(f"{input('nom du fichier (sans extension) :')}.txt", "w")
    f = open(f"{ln}.txt", "w")
    f.write(f"list lenght: {ln}\n\ntest d'algorithmes de trie\n------------------------\n{m_strings.get('selection')}{m_strings.get('insertion')}{m_strings.get('bulle')}")
    f.close()
