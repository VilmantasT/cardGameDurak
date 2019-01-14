import random


RUSYS = 'Širdžių Būgnų Vynų Kryžių'.split()
VERTES = '6 7 8 9 10 Bartukas Dama Karalius Tūzas'.split()

class Korta:

    def __init__(self, rusis, verte):
        self.rusis = rusis
        self.verte = verte

    def __gt__(self, other):
        return self.verte > other.verte

class Malka():

    malka = []

    def __init__(self):
        self.malka = [(r, v) for r in RUSYS for v in VERTES]

    def sumaisyti(self):
        random.shuffle(self.malka)

    def tuscia(self):
        return len(self.malka) == 0

    def isimti_korta(self):
        return self.malka.pop()



class Ranka(Malka):
    ranka = []

    def __init__(self, kortos):
        self.kortos = kortos
        for i in range(6):
            self.ranka.append(self.kortos.isimti_korta())

    def papildyti(self):
        while len(self.ranka) != 6:
            if len(self.kortos.malka) > 0:
                self.ranka.append(self.kortos.isimti_korta())
            else:
                break

malka = Malka()
malka.sumaisyti()
ranka = Ranka(malka)

for i in ranka.ranka:
    print(i)
print('*' * 20)
for i in malka.malka:
    print(i)
