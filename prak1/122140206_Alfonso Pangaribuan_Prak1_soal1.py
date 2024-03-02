'''
Alfonso Pangaribuan
    122140206
'''
def adalah_ganjil(angka):
    return angka % 2 != 0

batas_bawah = int(input("batas bawah: "))
batas_atas = int(input("batas atas: "))

if batas_bawah < 0 or batas_atas < 0:
    print("Batas bawah dan atas yang dimasukkan tidak boleh di bawah Nol")
else:
    angka_ganjil = [num for num in range(batas_bawah, batas_atas) if adalah_ganjil(num)]
    total_ganjil = sum(angka_ganjil)

    print("Angka Ganjil:")
    for angka in angka_ganjil:
        print(angka)

    print("Total :", total_ganjil)