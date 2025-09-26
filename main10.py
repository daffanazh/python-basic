# CLEAN CODE :
# Pakai pycodestyle untuk memperbaiki indent dan black untuk merapikan kode

Yes:
def LuasPersegiPanjang(panjang=2, lebar=None):
    luas = panjang*lebar
    return luas
 
No:
def LuasPersegiPanjang(panjang = 2, lebar = None):
    luas = panjang*lebar
    return luas

Yes:
def munge(input: str):  # Menambahkan informasi parameter bertipe string
    pass
def munge() -> str:   # Menambahkan informasi return value bertipe string
    pass
 
No:
def munge(input:str):  # Menambahkan informasi parameter bertipe string
    pass
def munge()->str:   # Menambahkan informasi return value bertipe string
    pass


Yes:
FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )

No:
FILES = ['setup.cfg', 'tox.ini',]
initialize(FILES, error=True,)

Yes:
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()

No:
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()

# Nama yang dilihat oleh user publik sebaiknya merefleksikan penggunaan/fungsinya dan bukan implementasinya. Misalnya nama fungsi berikut.
cariJalan() 

# Itu akan lebih mudah dipahami dibanding berikut.
jalan()