'''
Alfonso Pangaribuan
    122140206
'''
r = float(input("jari-jari: "))

if r < 0:
    print("jari-jari lingkaran tidak boleh negatif")
else:
    luas = 3.14 * r * r
    keliling = 2 * 3.14 * r
    print("Luas\t:", round(luas, 2))
    print("Keliling:", round(keliling, 2))