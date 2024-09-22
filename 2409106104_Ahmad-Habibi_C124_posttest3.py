# variabel
nama = str(input("Nama anda : "))
hari = str(input("Hari apa anda akan menonton : ")).lower()
harga = int(input("Berapa budget anda? "))

if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis":
    if harga >= 40000:
        print(f"Selamat {nama} anda bisa membeli tiket pada hari {hari}")
    else :
        print(f"Maaf anda tidak bisa membeli tiket pada hari {hari} karena harga tiket Rp.40,000 ")
elif hari == "jumat":
    if harga >= 45000:
        print(f"Selamat {nama} anda bisa membeli tiket pada hari {hari}")
    else :
        print(f"Maaf anda tidak bisa membeli tiket pada hari {hari} karena harga tiket Rp.45,000 ")
elif hari == "sabtu":
    if harga >= 55000:
        print(f"Selamat {nama} anda bisa membeli tiket pada hari {hari}")
    else :
        print(f"Maaf anda tidak bisa membeli tiket pada hari {hari} karena harga tiket Rp.55,000 ")
elif hari == "minggu":
    if harga >= 60000:
        print(f"Selamat {nama} anda bisa membeli tiket pada hari {hari}")
    else :
        print(f"Maaf anda tidak bisa membeli tiket pada hari {hari} karena harga tiket Rp.60,000 ")
else :
    print("Maaf tidak ada tiket")
