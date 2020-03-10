#no1
class Pesan(object):
    
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('kalimatku mempunyai', len(self.teks), 'karakter.')
    def perbarui(self, stringBaru):
        self.teks = stringBaru
    def apakahTerkandung(self, a):
        if a in self.teks:
            return True
        else :
            return False
    def hitungKonsonan(self):
        jmlKons = 0
        x = self.teks
        alfaKon = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        for i in x:
            if i in alfaKon:
                jmlKons += 1
        return jmlKons
    def hitungVokal(self):
        jmlVoc = 0
        x = self.teks
        Vocal = "aiueoAIUEO"
        for i in x:
            if i in Vocal:
                jmlVoc += 1
        return jmlVoc


#no2
class Manusia(object):
    
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salam, namaku ",self.nama)
    def makan(self, s):
        print("Saya baru saja makan ", s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print("Saya baru saja latihan ", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n * 2


class Mahasiswa(Manusia):
    def __init__ (self,nama,NIM,kota,us):
        self.nama = nama
        self.NIM = NIM
        self.kota = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM '+ str(self.NIM)\
            +', tinggal di '+ self.kota \
            +', uang saku '+ str(self.uangSaku)\
            +', tiap bylannya'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangS(self):
        return self.uangSaku
    def Makan(self, s):
        print("saya baru saja makan ", s," sambil belajar")
        self.keadaan = 'kenyang'

    #no2 a
    def ambilKota(self):
        return self.kota

    #no2 b
    def perbaruiKota(self, baru):
        self.kota = baru
    
    #no2 c
    def tambahUang(self, a):
        self.uangSaku = self.uangSaku + a


#no3
print("Silahkan melengkapi data berikut")
a = input ('Masukkan nama      : ')
b = input ('Masukkan NIM       : ')
c = input ('Masukkan Kota      : ')
d = int(input ('Masukkan Uang Saku : '))

maha = Mahasiswa(a,b,c,d)


#no4
    listKuliah = []
    def ambilKuliah(self, Matkul):
        self.listKuliah.append(Matkul)


#no5
    def hapusKuliah(self, Hps):
        self.listKuliah.remove(Hps)


#no6
class SiswaSMA(Manusia):
    def __init__(self, nama, NISN, uangSaku, alamat):
        self.nama = nama
        self.nisn = NISN
        self.uangSaku = uangSaku
        self.alamat = alamat
    def __str__(self):
        a = 'Nama      : ' + str(self.nama) + '\n' \
            + 'NISN      : ' + str(self.nisn) + '\n' \
            + 'Alamat    : ' + str(self.alamat) + '\n' \
            + 'Uang Saku : ' + str(self.uangSaku)
        return a


#no7
class MhsTIF(Mahasiswa):    # class induknya : Mahasiswa
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def kataKanPy(self):
        print('Python is cool.')

#makan merupakan metode yg berasal dari class Mahasiswa
#ambilNIM merupakan metode yg berasal dari class Mahasiswa
#ambilNama merupakan metode yg berasal dari class Mahasiswa
#ambilUangS merupakan metode yg berasal dari class Mahasiswa
#keadaan merupakan state yg berasal dari class Mahasiswa
#NIM merupakan state yg berasal dari class Mahasiswa
#nama merupakan state yg berasal dari class Mahasiswa
#kota merupakan state yg berasal dari class Mahasiswa
#katakanPy merupakan metode yg berasal dari class MhsTIF
#mengalikanDenganDua merupakan metode yg berasal dari class Manusia
