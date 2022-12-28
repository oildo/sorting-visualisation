# selection
def selection(liste):
  for i in range(len(liste)):
    min = i
    for j in range(i, len(liste)):
     if liste[j] < liste[min]:
       min = j
    liste[i], liste[min] = liste[min], liste[i]
  return liste

def selection_step(liste, min):
    i = min
    for j in range(i, len(liste)):
        if liste[j] < liste[min]:
            min = j
    liste[i], liste[min] = liste[min], liste[i]
    return (liste, i+1)
# insertion

def insertion(liste):
  for i in range(len(liste)):
    n = i
    while n != 0 and liste[n] < liste[n-1]:
      liste[n], liste[n-1] = liste[n-1], liste[n]
      n  -= 1
  return liste


def insertion_step(liste, i):
    n = i
    while n != 0 and liste[n] < liste[n-1]:
        if liste[n] < liste[n-1]:
            liste[n], liste[n-1] = liste[n-1], liste[n]
        n  -= 1
    return liste, i+1

# trie à bulle

def trieABulle(liste):

  max = len(liste) - 1
  while max >0:
    for i in range(max):
      if liste[i]> liste[i+1]:
        liste[i], liste[i+1] = liste[i+1], liste[i]
    max -=1

  return liste

def trieABulle_step(liste, max):

    for i in range(max):
      if liste[i]> liste[i+1]:
        liste[i], liste[i+1] = liste[i+1], liste[i]
    max -=1

    return liste, max
