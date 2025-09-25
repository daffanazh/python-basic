x = 1
y = 2
a = 3
b = 5

temp = x
x = y
y = temp

a , b = b , a       # one liner

print("\n")
print(temp)
print(x)
print(y)
print(a,b)

# percabangan
if(x > y):
    print("x lebih besar dari y")
else :
    print("x lebih kecil dari y")

nilai = 98
if(nilai >= 50 and nilai < 60):
    print("Grade C")
elif(nilai >= 60 and nilai < 70):
    print("Grade B")
elif(nilai >= 70 and nilai < 80):
    print("Grade A")
elif(nilai >= 80 and nilai < 90):
    print("Grade A+")
elif(nilai >= 90 and nilai <= 100):
    print("Grade S anjay Grade nya S cok wkwk")

lulus = True       # ternary
print("selamat") if lulus else print("yah gak lulus")

kelulusan = ("belajar lagi dek","anjay lulus")[lulus]
print(kelulusan)

# looping
for i in range(1,10,2):     # range(start,stop,step)
    print(i)

print("\n")
counter = 1
while counter <= 5:
    print(counter)
    counter += 1

print("\n")
for x in range(1,3):
    for y in range(1,3):
        print(x,y)

print("\n")
for q in range(2):
    print("Perulangan tingkat pertama :",q)
    for w in range(10):
        print("Perulangan tingkat kedua :",w)
        for e in range(3):
            print("Perulangan tingkat ketiga :",e)
            if e == 2:
                break

print("\n")
listhuruf = [1,2,3,4,5]

for num in listhuruf:
    if num == 6:
        print("ini angka 6")
    elif num > 2 and num < 4:
        break
    # elif num == 3:
    #     continue
    else:
        print("angka tidak ditemukan")

print("\n")
n = 10

while n > 1:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("iya")

print("\n")
evenNumber = []
for n in range(0, 501, 2):
    evenNumber.append(n)

print(evenNumber)


# error handling
print("\n")
z = 0
try :
    print(1/z)
except ZeroDivisionError:
    print("anda tidak bisa membagi angka dengan nilai nol anjeng awok")


print("\n")
var_dict = {"rata_rata": "1.0"}

try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")
