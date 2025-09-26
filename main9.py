class Mobil:
    warna = "Yellow"
    ukuran = 1000

class Makanan:
    def __init__(self, nama, harga):
        self.rasa = "Manis"
        self.warna = "Coklat"
        self.nama = nama
        self.harga = harga

class Mobil:
    def __init__(self, merek):
        self.merek = merek
    
    @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobil")
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()

mobil_toyota = Mobil()
mobil_toyota.warna = "Ungu"

mobil_avanza = Mobil()
mobil_avanza.ukuran = 7000

makanan_dapoy = Makanan("Donat",70000)

print(mobil_toyota.warna)
print(mobil_avanza.ukuran)
print(makanan_dapoy.nama)