from operator import le
import re


def figyelmeztetes():
    print("VIGYAZZ!")


def hangok(hanyszor):
    print(hanyszor * "FORDULJ VISSZA!\n")


def kabat(hatizsak):
    return "kabat" in hatizsak


def vizen_jaras(viz):
    if type(viz) != str:
        return False
    return viz.count("~") >= (len(viz) / 2)


def meow_szobor(szoveg, forditas=False):
    uj_szoveg = szoveg[::-1]
    if forditas:
        return uj_szoveg.lower()
    return uj_szoveg


def tunderek(tunder_lista):
    osszeg = 0
    for tunder in tunder_lista:
        osszeg += int(tunder)
    return osszeg


def csapdak(folyoso, tavolsag):
    return list(range(150, folyoso * 100 + 1, tavolsag))

def templomtanc(targyak: list):
    if targyak is None:
        return []
    eredmeny = []
    for targy in targyak:
        if targy.startswith("szent"):
            eredmeny.append(targy.strip())
            continue
        if len(targy < 5):
            continue
        uj_targy = ""
        maganhangzok = "aeiou"
        for c in targy:
            if c not in maganhangzok:
                uj_targy+=c
        eredmeny.append(uj_targy)
    return sorted(eredmeny)

