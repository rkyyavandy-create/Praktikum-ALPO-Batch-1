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

# --- 5. Tipe data koleksi ---
# List daftar mata kuliah yang diambil
daftar_matkul = ["Algoritma dan Pemrograman", "Sistem Digital", "Kalkulus"]

# Dictionary untuk menyimpan nilai mutu (KRS / KHS)
transkrip_nilai = {
    "Algoritma dan Pemrograman": 4.0,       # nilai (A)
    "Sistem Digital": 3.0,                  # nilai (B)
    "Kalkulus": 4.0                         # nilai (A)
}

# --- 6. Update variabel dinamis ---
# Mahasiswa mengmabil 1 mata kuliah susulan
matkul_baru = "Jaringan Komputer"
nilai_matkul_baru_str = "88.0"
mutu_matkul_baru = 3.5  # Nilai AB

# A. Tambah ke list
daftar_matkul.append(matkul_baru)

# B. Tambah ke dictionary
transkrip_nilai [matkul_baru] = mutu_matkul_baru

# C. Rekalkulasi variabel total & rata-rata
nilai_jk = float(nilai_matkul_baru_str)
total_nilai = total_nilai + nilai_jk    # Memperbarui nilai variabel total_nilai
jumlah_matkul = len(daftar_matkul)      # Memperbarui jumlah matkul menggunakan len()
rata_rata_terbaru = total_nilai / jumlah_matkul

# D. Hitung indeks prestasi kumulatif (IPK) dari dictionary mutu
total_bobot_mutu = sum(transkrip_nilai.values())
ipk_sementara = total_bobot_mutu / jumlah_matkul

print("\n---Hasil rekalkulasi setelah menambahkan matkul ---")
print("Daftar matkul terbaru:", daftar_matkul)
print("Jumlah matkul total:", jumlah_matkul)
print("Rata-rata angka baru:", round(rata_rata_terbaru, 2))
print("IPK sementara:", round(ipk_sementara, 2))