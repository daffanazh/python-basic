import numpy

matriks = [[1,2,3],
           [3,4,5],
           [6,7,8]]     # matriks manual, memakan banyak memori

matriks2 = numpy.array([[3,2,1],    # baris index 0
                        [6,5,4],    # baris index 1
                        [9,8,7]])   # baris index 2

                        # kolom index 0, 1, 2

print(matriks)
print(matriks2)
print(matriks2[2][1])