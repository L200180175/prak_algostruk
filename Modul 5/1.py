from kegiatan5 import *

class MhsTIF(object):
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', nim ' + str(self.nim)\
            + '. Tinggal di ' + self.kota\
            + '. Uang saku Rp ' + str(self.uangSalu)\
            + '. tiap bulannya.'
        return s

m0 = MhsTIF("Aldy", 175, "jakarta", 240000)
m1 = MhsTIF("Fatwa", 111, "bandung", 230000)
m2 = MhsTIF("Fakhar", 123, "Surakarta", 250000)
m3 = MhsTIF("Erdi", 122, "Surakarta", 235000)
m4 = MhsTIF("Hanan", 133, "papua", 240000)
m5 = MhsTIF("Rizki", 999, "kendari", 250000)
m6 = MhsTIF("iqbal", 908, "Riau", 245000)
m7 = MhsTIF("ijul", 678, "padang", 245000)
m8 = MhsTIF("fikri", 456, "Sorong", 245000)
m9 = MhsTIF("wafiq", 000, "sumba", 270000)
m10 = MhsTIF("kevin", 127, "wonogiri", 265000)

Daftar = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]

def urutNim(list):
    NIM = []
    for i in list:
        NIM.append(i.nim)
    insertionSort(NIM)
    return NIM

print(urutNim(Daftar))
