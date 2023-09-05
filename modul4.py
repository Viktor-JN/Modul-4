import os
import math
import random
os.system('cls')
print("Välkommen till gröna lund")
height=int(input("Hur lång är du i cm?(Endast nummmer)\n"))
if height < 140:
    print("Tyvärr du får inte komma in du är för kort")
elif height >= 140:
    print("Välkommen in!")
while True:
    name=str(input("Vad är ditt namn?\n"))
    x=name.isalpha()
    if x == False:
        print("Endast bokstäver!")
    else:
        break
while True:
    try:
        age=int(input("Hur gammal är du?\n"))
        break
    except:
        print("Endast siffror!")
print("Hej", name, "du är", age, "år gammal")
while True:
    try:
        weight=float(input("Hur mycket väger du i kg?\n"))
        break
    except:
        print("Endast siffror!")
while True:
    try:
        height=float(input("Hur lång är du i cm?\n"))
        break
    except:
        print("Endast siffror!")
height=height/100*2
bmi=weight/height
print("Du har", "%.1f" %bmi, "i bmi\n")
if bmi < 18.5:
    print("Du är underviktig, ät mer\n")
elif 18.5<=bmi<=24.9:
    print("Du är normalvikt\n")
elif 25<=bmi<=29.9:
    print("Du är övervikt, kanske borde äta lite mindre donken\n")
elif bmi>30:
    print("Du är fetma, borde kanske delta i ramadan eller nått\n")
print("Räkna arean av en cirkel med 3 decimaler!")
while True:
    try:
        r=float(input("Vad är radien av din cirkel?\n"))
        break
    except:
        print("Endast siffror!")
x=math.pi
y=x*r*r
print(round(y, 3), "är arean av din cirkel!")
#miniräknare
mini=True
while mini==True:
    print("välkommen till min miniräknare")
    try:
        method=int(input("Välj ett räknesätt genom att skriva nummrena\n1.Addition\n2.Subtraktion\n3.Multiplikation\n4.Division\n:"))
        mini=False
    except:
        print("\nVälj ett av alternativen med siffrorna.\n")
if method == 1:
    print("Välj 2 tal att addera")
    try:
        tal1=float(input("Tal 1\n:"))
    except:
        print("Endast nummer!")
    try:
        tal2=float(input("Tal 2\n:"))
    except:
        print("Endast tal!")
    tal=tal1+tal2
    print(tal1, "+", tal2, "=", tal)
elif method == 2:
    print("Välj 2 tal att subtrahera")
    try:
        tal1=float(input("Tal 1\n:"))
    except:
        print("Endast nummer!")
    try:
        tal2=float(input("Tal 2\n:"))
    except:
        print("Endast nummer!")
    tal=tal1-tal2
    print(tal1, "-", tal2, "=", tal)
elif method == 3:
    print("Välj 2 tal att multiplicera")
    try:
        tal1=float(input("Tal 1\n:"))
    except:
        print("Endast nummer!")
    try:
        tal2=float(input("Tal 2\n:"))
    except:
        print("Endast tal!")
    tal=tal1*tal2
    print(tal1, "*", tal2, "=", tal)
elif method == 4:
    print("Välj 2 tal att dividera")
    try:
        tal1=float(input("Tal 1\n:"))
    except:
        print("Endast nummer!")
    try:
        tal2=float(input("Tal 2\n:"))
    except:
        print("Endast tal!")
    tal=tal1/tal2
    print(tal1, "/", tal2, "=", tal)
dice_start=True
while dice_start==True:
    print("\nVill du slå en tärning")
    choice=input("Ja eller Nej\n").lower()
    if choice == "ja":
        dice=random.randint(1, 6)
        print("Du slog tärningen och fick", dice)
        dice_start=False
    elif choice == "nej":
        print("Okej")
        dice_start=False
    else:
        print("Svara ja eller nej\n")
vantal=True
while vantal==True:
    try:
        antal=int(input("Hur många gånger vill du slå tärningen\n:"))
        vantal=False
    except:
        print("Endast nummer")
for x in range(0, antal):
    dice=random.randint(1, 6)
    print("Du slog tärningen och fick", dice)