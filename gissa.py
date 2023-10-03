import random

print("\n________________________")
print(".:gissatalet:")

print(" Gissa ett tal mellan 1-10, du får 3 st försök\n")
slumptal = random.randint(1-10)
print(slumptal)
i=0 
hittat = False 


while i<3:
    gissatal = True 

    if slumptal == int(gissatal):
     hittat = True
     print("grattis du får en anka")
     break

    i += 1 

    if hittat:
       print("Du får en anka till")

    else:
       print("ingen anka nu")

if hittat:
   print("")




print("\______________")
