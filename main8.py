def luas_persegi_panjang(panjang,lebar):
    luas = panjang*lebar
    return luas

luas_pertama = luas_persegi_panjang(4,5)
luas_kedua = luas_persegi_panjang(6,7)

print(luas_pertama)
print(luas_kedua)


"""
Buatlah sebuah fungsi bernama "minimal" dengan ketentuan berikut.
- Menerima dua buah argumen berupa number, yaitu a dan b.
- Mengembalikan nilai terkecil antara a atau b.
- Bila nilai keduanya sama, kembalikan dengan nilai a.
"""

# akhirnya gw bisa ngerjain koding sendiri tanpa bantuan chatgpt, kode pertama gw yang bisa anjas
def minimal(a,b):
  if a<b:
    return a
  elif b<a:
    return b
  else:
    return a
    
print(minimal(10,10))

# prosedur
def greeting(name):
    print(f"Halo, ini gw {name}!")

greeting("dapoy")
  