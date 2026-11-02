#1. LIST (Berurutan, bisa diubah / mutable)
hobi = ["Membaca", "Coding", "Badminton"]
print ("List Hobi:", (hobi))
print ("Tipe:", type(hobi))

#2. TUPLE (Berurutan, tidak bisa diubah / immutable)
Koordinat = (-6.1751, 106.8650)
print ("Tuple Koordinat:", Koordinat)
print ("Tipe:", type(Koordinat))

#3. Dictionary (Pasangan Key : Value)
Mahasiswa = {
    "nama": "Ricky Avandy Saputra",
    "nim": 261080200038,
    "ipk": 3.85}
print ("Dic Mahasiswa:", Mahasiswa)
print ("Nama Mahasiswa:", Mahasiswa["nama"])
print ("Tipe:", type(Mahasiswa))

#4. Set (Nilai unik, tidak berurutan, tidak ada duplikat)
angka_unik= {1, 2, 2, 3, 4, 4, 5}
print ("Set Angka Unik (Otomatis Menghapus Duplikat):", angka_unik)
print ("Tipe:", type(angka_unik))

