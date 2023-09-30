

def bolygo(osszetevok):
    return len(osszetevok)

##osszetevok = [1,2,3]
##print(len(osszetevok))

def kalozok(kaloz_lista):
    for i in range(0 ,len(kaloz_lista)):
        kaloz_lista[i] = kaloz_lista[i] + ", a veszedelmes"

#kaloz_lista = ["Zoltan", "Karoly", "Edit"]
#kalozok(kaloz_lista)
#print(kaloz_lista)


#kaloz_lista = ["Zoltan, a veszedelmes;Viharlovag", "Panni, a veszedelmes;Tengeri sárkány", "David, a veszedelmes;Tengeri sárkány", "Feri, a veszedelmes; Villammano"]
def benepesites(kaloz_lista):
    dictionary = dict()
    for i in range(0, len(kaloz_lista)):
        temp = kaloz_lista[i].split(';')[1]
        if temp not in dictionary.keys():
            dictionary[temp] = 1
        else:
            dictionary[temp] += 1
    return dictionary

#print(benepesit(kaloz_lista))

#kaloz_lista = ["Endre", "Anna", "Etele", "Karoly", "Sanyika"]
#kaloz_lista_1 = ["Endre", "Anna", "Etele", "Karoly", "Sanyika", "Matyi"]
def csata(kaloz_lista):
    lista = []
    lista = kaloz_lista[1::2]
    return lista

#csata(kaloz_lista)
#csata(kaloz_lista_1)

#versenyzok = ["Coral Comet", "Aqua Racer", "Coral Comet", "Coral Comet", "Wave Warrior", "Wave Warrior", "Fin Flash", "Dolphin Dart"]
def verseny(versenyzo_lista:list):
    dictionary = dict()
    for versenyzo in versenyzo_lista:
        if versenyzo not in dictionary.keys():
            dictionary[versenyzo] = 1
        else:
            dictionary[versenyzo] += 1
    osszes = 0
    for kulcs in dictionary.keys():
        if dictionary[kulcs] == 2:
            osszes += 1
    return osszes

dictionary = {
"KX8-3YZ6": [0.17, 0.88, 0.53, 0.63],
"VF3-1XJ7": [0.55, 0.74, 0.23, 0.11],
"SD1-7MV8": [0.54, 0.99, 0.53, 0.51, 0.54]
}

def foci(vonat_dictionary:dict):
    atlag = 0
    kulcs = ""

    for temp_kulcs in vonat_dictionary.keys():
        vonat_dictionary[temp_kulcs].sort()
        vonat_dictionary[temp_kulcs] = vonat_dictionary[temp_kulcs][1:-1]
        temp_atlag = sum(vonat_dictionary[temp_kulcs]) / len(vonat_dictionary[temp_kulcs])
        if temp_atlag > atlag:
            atlag = temp_atlag
            kulcs = temp_kulcs
    return kulcs


print(foci(dictionary))