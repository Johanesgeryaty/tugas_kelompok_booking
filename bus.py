bandung_bus = 200000
semarang_bus = 100000
surabaya_bus = 150000
result = {
    "destinasi": [],
    "harga_tiket": [],
    "jumlah_tiket": 0,
    "titik_awal": [],
    "kelas_bus": []
}
def get_bus():


    jumlah_tiket = int(input("Berapa tiket yang ingin anda beli : "))
    result["jumlah_tiket"] = jumlah_tiket
    total_harga_tiket = 0

    for i in range(jumlah_tiket):
        kelas_bus = input(f"Masukan kelas bus yang anda inginkan [Ekonomi, VIP, Executive] (tiket ke {i + 1}): ").lower().strip()
        titik_awal = input(f"Masukan titik awal anda [Bandung,Semarang,Surabaya] (tiket ke {i + 1}): ").lower().strip()
        destinasi = input(f"Masukan tujuan anda [Bandung,Semarang,Surabaya] (tiket ke {i + 1}): ").lower().strip()

        if titik_awal == "bandung":
            result["titik_awal"].append("Bandung")
            harga_tiket = bandung_bus

        elif titik_awal == "semarang":
            result["titik_awal"].append("Semarang")
            harga_tiket = semarang_bus

        elif titik_awal == "surabaya":
            result["titik_awal"].append("Surabaya")
            harga_tiket = surabaya_bus

        else:
            print("error")

        if destinasi == titik_awal:
            print("Anda melakukan perjalanan dalam kota")

        elif destinasi == "bandung":
            harga_tiket += bandung_bus
            total_harga_tiket += harga_tiket
            result["destinasi"].append(destinasi.capitalize())
            result["harga_tiket"].append(harga_tiket)

        elif destinasi == "semarang":
            harga_tiket += semarang_bus
            total_harga_tiket += harga_tiket
            result["destinasi"].append(destinasi.capitalize())
            result["harga_tiket"].append(harga_tiket)
            
        elif destinasi == "surabaya":
            harga_tiket += surabaya_bus
            total_harga_tiket += harga_tiket
            result["destinasi"].append(destinasi.capitalize())
            result["harga_tiket"].append(harga_tiket)

    result["total_harga_tiket"] = total_harga_tiket
    return result



        