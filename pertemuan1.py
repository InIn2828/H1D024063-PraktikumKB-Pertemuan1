import random
import time

print("PILIH MAKANAN")
print("Sedang memilih makanan...")
time.sleep(1) 

daftar_makan = ["Nasi Goreng", "Ayam Bakar", "Mie Ayam", "Salad"]

for i in range(1):
    pilihan = random.choice(daftar_makan)
    print(f"Rekomendasi hari ini: {pilihan}")
    if pilihan == "Mie Ayam":
        print("Catatan: Inikah my..")
    elif pilihan == "Nasi Goreng":
        print("Catatan: Enak tuh malem-malem")
    else:
        print("Catatan: Bebas aja.")

print("====================================")
