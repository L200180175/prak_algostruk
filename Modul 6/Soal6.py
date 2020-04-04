class MhsTIF():
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uang = us

    def __str__ (self) :
        s = self.nama + " " + str(self.nim) + " " + self.kota + " " + str(self.uang)
        return s

m0 = MhsTIF("Aldy", 17, "jakarta", 240000)
m1 = MhsTIF("Fatwa", 11, "bandung", 230000)
m2 = MhsTIF("Fakhar", 12, "Surakarta", 250000)
m3 = MhsTIF("Erdi", 12, "Surakarta", 235000)
m4 = MhsTIF("Hanan", 13, "papua", 240000)
m5 = MhsTIF("Rizki", 99, "kendari", 250000)
m6 = MhsTIF("iqbal", 90, "Riau", 245000)
m7 = MhsTIF("ijul", 67, "padang", 245000)
m8 = MhsTIF("fikri", 45, "Sorong", 245000)
m9 = MhsTIF("wafiq", 00, "sumba", 270000)
m10 = MhsTIF("kevin", 12, "wonogiri", 265000)

Daftar = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]
A = []
for i in Daftar:
    A.append(i.nama)

def cetak():
    for i in A:
        print(i)

def quickSort(arr):
    kurang = []
    pivotList = []
    lebih = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                kurang.append(i)
            elif i > pivot:
                lebih.append(i)
            else:
                pivotList.append(i)
        kurang = quickSort(kurang)
        lebih = quickSort(lebih)
        return kurang + pivotList + lebih

print("Sebelum diurutkan")
cetak()
print("\nSetelah diurutkan")
quickSort(A)
cetak()
