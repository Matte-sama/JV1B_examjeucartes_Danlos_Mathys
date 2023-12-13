
class mage:
    def __init__(self,nom,pv, mana):
        self.__nom = nom
        self.__pv = pv
        self.__mana = mana
    def getnom(self):
        return self.__nom
    def getpv(self):
        return self.__pv
    def getmana(self):
        return self.__mana    


class carte :
    def __init__(self,mana,nom,description):
        self.__mana = mana
        self.__nom = nom
        self.__description=description
    def getmana(self):
        return self.__mana
    def getnom(self):
        return self.__nom
    def getdesciption(self):
        return self.__description
    

class cristal(carte):
    def __init__(self, valeur):
        self.__valeur = 2
    def getvaleur(self):
        return self.__valeur

class monster(carte):
    def __init__(self, valeur, pv, attack):
        self.__valeur = valeur
        self.__pv = pv
        self.__attack = attack
    def getvaleur(self):
        return self.__valeur
    def getpv(self):
        return self.__pv
    def getattack(self):
        return self.__attack

class blast(carte):
    def __init__(self, valeur, attack):
        self.__valeur = 1
        self.__attack = 2
    def getvaleur (self):
        return self.__valeur
    def getattack (self):
        return self.__attack
    

mage1 = mage("Merlin", 10,5)
mage2 = mage("Harry", 10,5)


