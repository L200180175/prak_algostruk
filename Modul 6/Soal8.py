class Node():
    def __init__(self, data, isi=None):
        self.data = data
        self.isi = isi

def cetak(head):
    curr = head
    while curr is not None:
        try:
            print (curr.data)
            curr = curr.isi
        except:
            pass

a = Node(10)
b = Node(30)
c = Node(50)
d = Node(70)
e = Node(20)
f = Node(40)
g = Node(60)

a.isi = b
b.isi = c
c.isi = d
d.isi = e
e.isi = f
f.isi = g

def mergeSortll(A):
    linked = A
    try:
        daftar = []
        curr = A
        while curr:
            daftar.append(curr.data)
            curr = curr.isi
        A = daftar
    except:
        A = A

    if len(A) > 1:
        mid = len(A) // 2
        separuhkiri = A[:mid]
        separuhkanan = A[mid:]

        mergeSortll(separuhkiri)
        mergeSortll(separuhkanan)

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

    for x in A:
        try:
            linked.data = x
            linked = linked.isi
        except:
            pass

mergeSortll(a)
cetak(a)
