import re


class Idogep:

    def __init__(self, vissza_ido=1000):
        self.vissza_ido = vissza_ido

    def __str__(self):
        return f"Az idogep ennyit fog visszautazni az idoben: {self.vissza_ido}"

idoggep = Idogep(70_000_000)
print(idoggep.__str__())


class Dinoszaurusz:
    def __init__(self, fajta, magassag):
        self._fajta = fajta
        self._magassag = abs(magassag)
        self._veszelyes = self._fajta.endswith('rex') or self._magassag > 500  # Veszélyes-e a dinoszaurusz

    # Getters
    @property
    def fajta(self):
        return self._fajta

    @property
    def magassag(self):
        return self._magassag

    @property
    def veszelyes(self):
        return self._veszelyes

    #Setters
    @fajta.setter
    def fajta(self, fajta):
        self._fajta = fajta

    @magassag.setter
    def magassag(self, magassag):
        if magassag > 0:
            self._magassag = magassag

    @veszelyes.setter
    def veszelyes(self, veszelyes):
        self._veszelyes = veszelyes

    def __iadd__(self, mennyiseg):
        self._magassag += mennyiseg
        return self
    
    def __eq__(self, masik_dinoszaurusz):
        if isinstance(masik_dinoszaurusz, Dinoszaurusz):
            return self._magassag == masik_dinoszaurusz._magassag and self._fajta == masik_dinoszaurusz._fajta and self._veszelyes == masik_dinoszaurusz._veszelyes
        return False
    
dino1 = Dinoszaurusz("T-rex", 330)
dino2 = Dinoszaurusz("T-rex", 330)

print(dino1 == dino2)


