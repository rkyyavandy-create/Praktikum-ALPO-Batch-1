#--- 1. Deklarasi data diri mahasiswa ---
nim = "261080200038"
nama_mahasiswa= "Ricky Avandy Saputra"
semester = 1
is_aktif = True     # Status registrasi ulang

#--- 2. Data nilai mentah (Simulasi iput melalui Form Web / Database) ---
#Catatan: Input dari form seringkali terbaca sebagai String
str_nilai_algoritma = "80"
str_nilai_basis_data = "90"
str_nilai_pemrograman_web = "85"
sks_per_matkul = 19  # Integer

#--- 3. Koversi tipe data (TYPE CASTING) ---
nilai_algo = float(str_nilai_algoritma)
nilai_bd = float(str_nilai_basis_data)
nilai_pemrograman_web = float(str_nilai_pemrograman_web)

#--- 4. kalkulasi menggunakan variabel ---
total_nilai = nilai_algo + nilai_bd + nilai_pemrograman_web
jumlah_matkul = 3
rata_rata_nilai= total_nilai / jumlah_matkul
total_sks_diambil = jumlah_matkul * sks_per_matkul

#Penentuan status kelulusan semester (Boolean)
#Lulus jika rata-rata >= 75.0 dan status mahasiswa aktif
is_lulus_semester = (rata_rata_nilai >= 75.0) and is_aktif

print("\n--- Hasil Evaluasi Aval ---")
print("Total Nilai: ", total_nilai)
print("Rata-rata: ", round(rata_rata_nilai, 2))
print("Total SKS: ", total_sks_diambil)
print("Lulus Semester: ", is_lulus_semester)