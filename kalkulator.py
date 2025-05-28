# Meminta input dari pengguna dan mengonversinya menjadi integer
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

# Menampilkan pilihan operator
print("tambah(+), kurang(-), kali(*), bagi(/)")

# Memilih operator
operator = input("Pilih salah satu operator: ")

# Mengeksekusi operasi berdasarkan operator yang dipilih
if operator == '+':
    hasil = angka1 + angka2
elif operator == '-':
    hasil = angka1 - angka2
elif operator == '*':
    hasil = angka1 * angka2
elif operator == '/':
    hasil = angka1 / angka2
else:
    hasil = "Operator yang anda gunakan tidak sesuai"

# Menampilkan hasil
print("Hasil: ", hasil)
