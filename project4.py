def taken(x:int)->int:
    digit =0
    for a in str(x):
        digit += int(a) # Tant que le nombre a plus d'un chiffre
      # Somme des chiffres du nombre
    return digit

x = 1213 
print(taken(x))
