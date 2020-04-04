class MhsTIF():
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uang = us

    def __str__(self):
        s = self.nama + " " + str(self.nim) + " " + self.kota + " " + str(self.uang)
        return s

    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.nim
    def ambilUangSaku(self):
        return self.uang

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


def cetak(A):
    for i in A:
        print (i)

def mergeSort2(A, awal, akhir):
    mid = (awal+akhir)//2
    if awal < akhir:
        mergeSort2(A, awal, mid)
        mergeSort2(A, mid+1, akhir)

    a, f, l = 0, awal, mid+1
    tmp = [None] * (akhir - awal + 1)
    while f <= mid and l <= akhir:
        if A[f].ambilUangSaku() < A[l].ambilUangSaku():
            tmp[a] = A[f]
            f += 1
        else:
            tmp[a] = A[l]
            l += 1
        a += 1

    if f <= mid:
        tmp[a:] = A[f:mid+1]

    if l <= akhir:
        tmp[a:] = A[l:akhir+1]

    a = 0
    while awal <= akhir:
        A[awal] = tmp[a]
        awal += 1
        a += 1
        
def mergeSort(A):
    mergeSort2(A, 0, len(A)-1)

print("Sebelum diurutkan")
cetak(Daftar)
mergeSort(Daftar)
print("\nSeletah diurutkan")
cetak(Daftar)
