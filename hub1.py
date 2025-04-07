class Patsient:
    def __init__(self, nimi, vanus):
        self.nimi = nimi
        self.vanus = vanus
    
class Arst:
    def __init__(self, nimi, vanus, eriala, aeg):
        self.nimi = nimi
        self.vanus = vanus
        self.eriala = eriala
        self.aeg = aeg

class Haigla:
    def __init__(self):
        self.patsiendiList = []
        self.arstilist = []

    def naitaArstid(self):
        for elem in self.arstilist:
            print("Arsti nimi:", elem.nimi, "Vanus:", elem.vanus, "Eriala:", elem.eriala)
            if len(elem.aeg) > 0:
                for time in elem.aeg:
                    print("Aeg:", time)
    
    def naitaArst(self, arst):
        print(f"Arsti {arst.nimi} ajakava:")
        for time in arst.aeg:
            print(time)
            
    def viisitArst(self):
        sisetatudArstNimi = input("Arsti nimi: ")
        for elem in self.arstilist:
            if sisetatudArstNimi == elem.nimi:
                self.naitaArst(elem)
                break
        else:
            print("Arsti ei leitud.")
    
    def naitaPatsientid(self):
        for index, i in enumerate(self.patsiendiList):
            print("id:", index, "Patsiendi nimi:", i.nimi, "Vanus:", i.vanus)

pats1 = Patsient("Thomas", 24)
pats2 = Patsient("Franklin", 45)

arst1 = Arst("Muhamad", 35, "Kiirurg", ['10:00', '10:30', '11:00', '11:30'])
arst2 = Arst("Ahmed", 28, "Kiirurgi-abi", ['09:00', '09:30', '10:00'])

haigla = Haigla()
haigla.arstilist.append(arst1)
haigla.arstilist.append(arst2)

haigla.naitaArstid()
haigla.viisitArst() 
haigla.patsiendiList.append(pats1)
haigla.patsiendiList.append(pats2)

haigla.naitaPatsientid()



