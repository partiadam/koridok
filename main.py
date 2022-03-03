'''csapat;versenyzo;eletkor;palya;korido;kor
Versenylovak;Fürge Ferenc;29;Gran Prix Circuit;00:01:11;1'''


class Korido:
    def __init__(self, sor):
        csapat, versenyzo, eletkor, palya, korido, kor, = sor.strip().split(';')
        self.csapat = csapat
        self.versenyzo = versenyzo
        self.eletkor = eletkor
        self.palya = palya
        self.korido = korido
        self.kor = int(kor)
        self.ora = int(korido[:2])
        self.perc = int(korido[3:5])
        self.masodperc = int(korido[6:8])

lista = []

with open('autoverseny.txt', 'r', encoding="utf-8")as f:
    f.readline()
    for sorok in f:
        lista.append(Korido(sorok))

#3. feladat

print(f'3. feladat: {len(lista)}')

#4. feladat

meghatarozas = [sor.ora * 3600 + sor.perc* 60 + sor.masodperc for sor in lista if sor.versenyzo == 'Fürge Ferenc' and sor.palya == 'Gran Prix Circuit' and sor.kor == 3]

print(f'4. feladat: {meghatarozas[0]} másodperc')

#5. feladat

beker = input('Minta szerinti név: \n')


#6. feladat

for sor in lista:
    legkisebb = min(lista, key=lambda x:x).kor
    if sor.versenyzo == beker:
       print(legkisebb)