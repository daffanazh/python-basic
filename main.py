name = "daffa"
umur = 17
nilai_koma = 90.2
ini_complex = 1+2j
multi_line = """mang ea slurr
kata gue juge
apaa busyett"""
str_index = name[1]
str_index_slicing = name[2:]
hp = "Xiaomi"
variable_list = [1,"dapoy",2.3,1+1j,True]
sequence = variable_list[0:5:4]

# menampilkan index ke 2 hingga terakhir
sequence2 = variable_list[2:]

# menampilkan index ke 0 sampai ke 2
sequence3 = variable_list[:3]

set_variable = {1,2,3,4,"ini objek"}
set_variable2 = {3,4,"kamu ngopi",5,6,7,"hooh"}

# gabungin
union_set = set_variable.union(set_variable2)

# irisan
intersection_set = set_variable.intersection(set_variable2)

identity = {'name' : 'dapoy', 'age' : 23, 'hobi' : 'fotografi'}
identity['Job'] = 'Software Engineer'
identity['isBerak'] = 'Belon'
del identity['isBerak']
identity['Hero Exp Lane Favorit'] = 'Thamuz'
identity['Hero Exp Lane Favorit'] = 'Grock'




print(type(umur))
print(type(nilai_koma))
print(name)
print(type(ini_complex))
print(multi_line)
print(str_index)
print(str_index_slicing)

# formatted string
print(f"Hp saya adalah {hp}")

# % formatting
print("Hp gue adalah %s" % (hp))

# str format
print("Hp aingg adalah {}".format(hp))

print(type(variable_list))
print(variable_list[1])
print(variable_list[-3])
print(sequence)
print(sequence2)
print(sequence3)
print(set_variable)
print(union_set)
print(intersection_set)
print(type(identity))
print(identity['hobi'])
print(identity)
print(float(umur))
print(int(nilai_koma))

# tipe data primitif
    # integer
    # float
    # complex

# integer, string, dan list bersifat immutable alias tidak bisa diubah datanya

# sequence[start:stop:step]