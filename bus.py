bandung_bus = 200000
semarang_bus = 100000
surabaya_bus = 150000
def get_bus():
    result = {}
    result["destinasi"] = []
    result["harga_tiket"] = []
    jumlah_tiket = int(input("Berapa tiket yang ingin anda beli : "))
    result["jumlah_tiket"] = jumlah_tiket
    result["titik_awal"] = []
    total_harga_tiket = 0
    for i in range(jumlah_tiket):
        titik_awal = input("Masukan titik awal anda [Bandung,Semarang,Surabaya] : ").lower()
        destinasi = input("Masukan tujuan anda [Bandung,Semarang,Surabaya] : ").lower()
        if titik_awal == "bandung":
            result["titik_awal"].append("Bandung")
            if destinasi == "bandung":
                harga_tiket = bandung_bus
                total_harga_tiket += harga_tiket
                result["destinasi"].append(destinasi.capitalize())
                result["harga_tiket"].append(harga_tiket)
            elif destinasi == "semarang":
                harga_tiket = semarang_bus + bandung_bus
                total_harga_tiket += harga_tiket
                result["destinasi"].append(destinasi.capitalize())
                result["harga_tiket"].append(harga_tiket)
            elif destinasi == "surabaya":
                harga_tiket = surabaya_bus + bandung_bus
                total_harga_tiket += harga_tiket
                result["destinasi"].append(destinasi.capitalize())
                result["harga_tiket"].append(harga_tiket)

        elif titik_awal == "semarang":
            result["titik_awal"].append("Semarang")
            if destinasi == "bandung":
                harga_tiket = bandung_bus + semarang_bus
                total_harga_tiket += harga_tiket
                result["destinasi"].append(destinasi.capitalize())
                result["harga_tiket"].append(harga_tiket)
            elif destinasi == "semarang":
                harga_tiket = semarang_bus
                total_harga_tiket += harga_tiket
                result["destinasi"].append(destinasi.capitalize())
                result["harga_tiket"].append(harga_tiket)
            elif destinasi == "surabaya":
                harga_tiket = surabaya_bus + semarang_bus
                total_harga_tiket += harga_tiket
                result["destinasi"].append(destinasi.capitalize())
                result["harga_tiket"].append(harga_tiket)

        elif titik_awal == "surabaya":
            result["titik_awal"].append("Surabaya")
            if destinasi == "bandung":
                harga_tiket = bandung_bus + surabaya_bus
                total_harga_tiket += harga_tiket
                result["destinasi"].append(destinasi.capitalize())
                result["harga_tiket"].append(harga_tiket)
            elif destinasi == "semarang":
                harga_tiket = semarang_bus + surabaya_bus
                total_harga_tiket += harga_tiket
                result["destinasi"].append(destinasi.capitalize())
                result["harga_tiket"].append(harga_tiket)
            elif destinasi == "surabaya":
                harga_tiket = surabaya_bus
                total_harga_tiket += harga_tiket
                result["destinasi"].append(destinasi.capitalize())
                result["harga_tiket"].append(harga_tiket)
    result["total_harga_tiket"] = total_harga_tiket
    print(result)



        