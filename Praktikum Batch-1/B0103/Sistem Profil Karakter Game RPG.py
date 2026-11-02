# --- Sistem Profil Karakter Game RPG

# 1. Variabel profil karakter
nama_hero = "Hayato"                                                     # String
level = 15                                                               # Integer
hp = 200.0                                                               # Float
is_alive = True                                                          # Boolean
inventory = ["Pedang Baja", "Pedang Samurai", "Granat"]                  # List (min. 3 senjata)
atribut = {"kekuatan": 85, "kelincahan": 95, "Ketahanan": 80}            # Dictionary


def tampilkan_profil():
    print("Nama Hero :", nama_hero)
    print("Level     :", level)
    print("HP        :", hp)
    print("Hidup     :", is_alive)
    print("Inventory :", inventory)
    print("Atribut   :", atribut)


# 2. Tampilkan seluruh informasi karakter
print("=== PROFIL KARAKTER ===")
tampilkan_profil()

# 3. Tampilkan tipe data tiap variabel
print("\n=== TIPE DATA ===")
print("nama_hero :", type(nama_hero))
print("level     :", type(level))
print("hp        :", type(hp))
print("is_alive  :", type(is_alive))
print("inventory :", type(inventory))
print("atribut   :", type(atribut))

# 4. Aksi
inventory.append("Ramuan HP")   # item baru
level = float(level) + 0.5      # konversi ke float lalu tambah 0.5

# 5. Cetak kembali informasi terbaru
print("\n=== PROFIL KARAKTER (TERBARU) ===")
tampilkan_profil()
print("Tipe data level sekarang:", type(level))
