#--- 1. Deklarasi data diri mahasiswa ---
nim = "261080200038"
nama_mahasiswa = "Ricky Avandy Saputra"
semester = 1
is_aktif = True     # Status registrasi ulang

#--- 2. Data nilai mentah (Simulasi iput melalui Form Web / Database) ---
#Catatan: Input dari form seringkali terbaca sebagai String
str_nilai_algoritma = "80"
str_nilai_basis_data = "90"
str_nilai_pemrograman_web = "85"
sks_per_matkul = 19  # Integer

#Tampilkan data awal
print (f"Data Mahasiswa: {nama_mahasiswa} (NIM: {nim})")
print ("Status Aktif :", is_aktif)