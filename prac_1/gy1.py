text = "apple"
for c in text:
    print(f"{c} ", end=" ")

print()
'''
num = int(input("Input a number: "))

if num < 0:
    print("The given number is negative")
elif num > 0:
    print("The give number is positive")
else:
    print("The given number is 0")
'''

text = str(101) + " dalmatians"  # strings are immutable in python: once declared, can't be changed
print(text)

print(len("python"))
text = "python"
for i in range(0, len(text), 1):
    print(f"{text[i]}", end=" ")
print()

for i in range(1, 11):
    print(f"{i}", end=" ")
    for j in range(2, 11):
        print(f"{i * j}", end=" ")
    print()

""" Exercises """

"""1. Írj Python szkriptet, amely beolvas a standard bemenetről két szöveget és rendre összefűzi azokat! Az összefűzés 
eredményeképpen kapott szöveget írasd ki a konzolra!"""

text_1 = input("First word: ")
text_2 = input("Second word: ")
print()
print(f"The concatenated words: {text_1 + text_2}")

"""2. Dávid, a kereskedő számítógép alkatrészeket ad el. Mivel mostanság megnőtt a vásárlói igény az alkatrészekre, 
ezért Dávid úgy dönt, hogy felemeli az árait.

Írj Python szkriptet, amely beolvassa a standard bemenetről egy adott alkatrész jelenlegi árát (egész szám), 
valamint az áremelés mértékét százalékban (valós szám)! Írasd ki a konzolra, hogy mennyi lesz az alkatrész ára, 
miután azt az adott százalékkal megnöveljük! A végeredményt egész számmá alakítva írasd ki!"""

price = int(input("The current price of the product: "))
perc = float(input("Increase price in %: "))

print()
print(f"The new price of the product: {price + (price * perc / 100)}")

"""3. A gimnazista Laci informatikaórán odafigyelés helyett mémeket nézegetett, ezért az informatikatanártól azt a 
régimódi büntetést kapta, hogy le kell írnia a nevét 100-szor. Írj Python szkriptet, amely kiírja a konzolra a Laci 
szöveget 100 alkalommal! Az egyes kiíratások után szerepeljen sortörés is!"""

print("Laci\n" * 100)

"""4 Jónás, a csokigyáros úgy döntött, hogy nyereményjátékot hirdet: néhány legyártott csokoládéba egy aranyszelvényt 
helyez, és a szelvények szerencsés megtalálói egy különleges látogatást tehetnek a csokigyárban. Minden csokihoz 
tartozik egy gyártási sorszám, és Jónás azokba a csokikba tesz aranyszelvényt, amelyek gyártási sorszáma prímszám.

Írj Python szkriptet, amely beolvassa a konzolról egy csoki gyártási sorszámát (egész szám)! Ha a beolvasott szám 
prímszám, akkor írasd ki a Gratulalok, nyertel!, ellenkező esetben pedig a Sajnos nem nyert! szöveget a konzolra!"""

num = int(input("Enter a number: "))
if(num < 2):
    print("The given number is not prime.")
else:
    is_prime = True
    for i in range(2, (num//2) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("The given number is prime.")
    else:
        print("The given number is not prime.")




