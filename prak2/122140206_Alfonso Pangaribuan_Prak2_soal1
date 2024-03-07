'''
AlfonsoPangaribuan
122140206
PBO RB
'''

class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.__isMahasiswa = isMahasiswa

    def set_nim(self, nim):
        self.__nim = nim

    def get_nim(self):
        return self.__nim

    def set_nama(self, nama):
        self.__nama = nama

    def get_nama(self):
        return self.__nama

    def set_isMahasiswa(self, isMahasiswa):
        self.__isMahasiswa = isMahasiswa

    def get_isMahasiswa(self):
        return self.__isMahasiswa

    def info_mahasiswa(self):
        return f"NIM: {self.get_nim()}, Nama: {self.get_nama()}, Angkatan: {self.angkatan}, Mahasiswa: {self.get_isMahasiswa()}"

    def belajar(self, jam):
        return f"{self.get_nama()} belajar selama {jam} jam."

    def lulus(self):
        if self.get_isMahasiswa():
            return f"{self.get_nama()} telah lulus."
        else:
            return f"{self.get_nama()} tidak dapat lulus karena bukan mahasiswa."


# Object pertama dengan isMahasiswa = True
mahasiswa1 = Mahasiswa("12214111", "Anjim", 2011)
print(mahasiswa1.info_mahasiswa())
print(mahasiswa1.belajar(5))
print(mahasiswa1.lulus())

print()

# Object kedua dengan isMahasiswa = False
mahasiswa2 = Mahasiswa("122113111", "Budat", 2021, isMahasiswa=False)
print(mahasiswa2.info_mahasiswa())
print(mahasiswa2.belajar(3))
print(mahasiswa2.lulus())

print()

# Ubah mahasiswa1
mahasiswa1.set_nim("122140206")
mahasiswa1.set_nama("Alfonso Pangaribuan")
mahasiswa1.angkatan = 2022
print(mahasiswa1.info_mahasiswa())
