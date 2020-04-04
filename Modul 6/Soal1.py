class MhsTIF:
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kota = kota
        self.uang = us
    def __str__ (self) :
        s = self.nama + " " + str(self.NIM) + " " + self.kota + " " + str(self.uang)
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

def mergeSort(A):
    #print("Membelah      ",A)
    if len(A) > 1:
        mid = len(A) // 2
        separuhkiri = A[:mid]
        separuhkanan = A[mid:]

        mergeSort(separuhkiri)
        mergeSort(separuhkanan)

        i = 0;j=0;k=0
        while i < len(separuhkiri) and j < len(separuhkanan):
            if separuhkiri[i] < separuhkanan[j]:
                A[k] = separuhkiri[i]
                i = i + 1
            else:
                A[k] = separuhkanan[j]
                j = j + 1
            k=k+1

        while i < len(separuhkiri):
            A[k] = separuhkiri[i]
            i = i + 1
            k=k+1

        while j < len(separuhkanan):
            A[k] = separuhkanan[j]
            j = j + 1
            k=k+1
    #print("Menggabungkan",A)


def quickSort(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSort(A, awal, titikBelah-1)
        quickSort(A, titikBelah+1, akhir)

def partisi(A, awal, akhir):
    nilaipivot = A[awal]

    penandakiri = awal + 1
    penandakanan = akhir

    selesai = False
    while not selesai:

        while penandakiri <= penandakanan and A[penandakiri] <= nilaipivot:
            penandakiri = penandakiri + 1

        while penandakanan >= penandakiri and A[penandakanan] >= nilaipivot:
            penandakanan = penandakanan - 1

        if penandakanan < penandakiri:
            selesai = True
        else:
            temp = A[penandakiri]
            A[penandakiri] = A[penandakanan]
            A[penandakanan] = temp

    temp = A[awal]
    A[awal] = A[penandakanan]
    A[penandakanan] = temp

    return penandakanan

      
def convert(arr, obj):
    hasil=[]
    for x in range (len(arr)):
        for i in range (len(arr)):
            if arr[x] == obj[i].NIM:
                hasil.append(obj[i])
    return hasil

def printMerge(arr):
    print("hasil merge sort")
    NIM = []
    for i in arr:
        NIM.append(i.NIM)
    mergeSort(NIM)
    for x in convert(NIM, arr):         
        print(x.NIM) 
        
        

def printQuick(arr):
    print("\nhasil quick sort")
    A = []
    for x in Daftar:
        A.append(x.NIM)

    quickSort(A, 0, len(A)-1)
    for x in convert(A, Daftar):
        print (x.NIM)

printMerge(Daftar)
printQuick(Daftar)
