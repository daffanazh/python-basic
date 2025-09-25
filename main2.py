kata = "daffa"
huruf_besar = kata.upper()
huruf_kecil = kata.lower()

space_end = "iyaaaa       "
del_space_end = space_end.rstrip()
space_beginning = "        iyaaaaa"
del_space_beginning = space_beginning.lstrip()
space_between = "      iyaaaa       "
del_space_between = space_between.strip()
kalimat = "AkuKencingDibawahPohon"
kalimat_normal = "Lorem Ipsum Dolor Sit Amet"
strip_kalimat = kalimat.strip("AkuDibawahPohon")
menemukan_awal_kalimat = kalimat.startswith("AkuKencing")
menemukan_akhir_kalimat = kalimat.endswith("DibawahPohon")
list_item = [1,2,3,4,5,5,5,5,8,2]
data = ['Baju','Putih','30s']
data[1] = 'Jembud'
baju, warna, jenis = data
data.sort(reverse=True)


print(huruf_besar)
print(huruf_kecil)
print(del_space_end)
print(del_space_beginning)
print(del_space_between)
print(strip_kalimat)
print(menemukan_awal_kalimat)
print(menemukan_akhir_kalimat)
print(' '.join(['Daffa','Nazhmi','Hakim']))
print('Ngopi'.join(['Disini ',' Disana ',' juga']))
print(kalimat_normal.split())
print(kalimat_normal.replace("Dolor","Dulur"))
print(kata.isupper())
print(kata.islower())
print(kata.isalpha())
print(kata.isalnum())
print(kata.isdecimal())
print('    '.isspace())
print(kalimat.istitle())
print(kalimat_normal.istitle())
print(kata.zfill(7))
print(kata.rjust(10))
print(kata.ljust(20))
print(kata.center(9,'-'))
print(len(list_item))
print(len(kalimat_normal))
print(min(list_item))
print(max(list_item))
print(list_item.count(5))
print('Lorem' in kalimat_normal)
print('Jemboot' in kalimat_normal)
print('Lorem' not in kalimat_normal)
print('Jemboot' not in kalimat_normal)
print(baju,warna,jenis)
print(data)