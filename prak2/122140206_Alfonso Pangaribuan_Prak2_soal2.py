'''
Alfonso Pangaribuan
122140206
PBO RB
'''
class Dinosaurus:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

    def __del__(self):
        print(f"{self.nama} telah punah.")

    @staticmethod
    def pelihara(func):
        def wrapper(self):
            print(f"Menjaga {self.nama} dengan baik.")
            func(self)
        return wrapper

    @classmethod
    def tambah_usia(cls, dino, tahun):
        dino.usia += tahun
        print(f"{dino.nama} bertambah usia menjadi {dino.usia} tahun.")


# Object pertama dengan menggunakan decorator
dino1 = Dinosaurus("Tyrannosaurus", 70)

@dino1.pelihara
def makan(self):
    print(f"{self.nama} sedang makan.")

makan(dino1)
Dinosaurus.tambah_usia(dino1, 10)
del dino1

print()

# Object kedua dengan menggunakan constructor dan destructor
class Dinosaurus2:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

    def __del__(self):
        print(f"{self.nama} telah punah.")

    def pelihara(self):
        print(f"Menjaga {self.nama} dengan baik.")

    @classmethod
    def tambah_usia(cls, dino, tahun):
        dino.usia += tahun
        print(f"{dino.nama} bertambah usia menjadi {dino.usia} tahun.")


dino2 = Dinosaurus2("Stegosaurus", 150)
dino2.pelihara()
Dinosaurus2.tambah_usia(dino2, 20)
del Dinosaurus2
