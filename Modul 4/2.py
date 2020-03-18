class Mhs(object):
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = us

m0 = Mhs("Aldy", 175, "jakarta", 240000)
m1 = Mhs("Fatwa", 111, "bandung", 230000)
m2 = Mhs("Fakhar", 123, "Surakarta", 250000)
m3 = Mhs("Erdi", 122, "Surakarta", 235000)
m4 = Mhs("Hanan", 133, "papua", 240000)
m5 = Mhs("Rizki", 999, "kendari", 250000)
m6 = Mhs("iqbal", 908, "Riau", 245000)
m7 = Mhs("ijul", 678, "padang", 245000)
m8 = Mhs("fikri", 456, "Sorong", 245000)
m9 = Mhs("wafiq", 000, "sumba", 270000)
m10 = Mhs("kevin", 127, "wonogiri", 265000)

Daftar = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]

def cariUangSakuTerkecil(list):
    temp = list[0].uangSaku
    for i in list[1:]:
        if i.uangSaku < temp:
            temp = i.uangSaku
            nama = i.nama
    return nama, temp

a = cariUangSakuTerkecil(Daftar)
print(a)
