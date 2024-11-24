# Konstanta untuk harga dan pilihan
HARGA_KAMAR = {
    "standard": 0,
    "twin": 100000,
    "double": 150000,
    "family": 300000
}



HARGA_HOTEL = {
    "mercure(bandung)": 300000,
    "novotel(semarang)": 200000,
    "sheraton(surabaya)": 250000
}

NAMA_HOTEL = list(HARGA_HOTEL.keys())

JENIS_KAMAR = list(HARGA_KAMAR.keys())

result = {
    "harga_hotel": [],
    "jumlah_kamar": 0,
    "jenis_kamar": [],
    "total_harga_tiket": 0,
    "nama_hotel": []
}

def validate_input(prompt, valid_options):
    """Memvalidasi input user"""
    while True:
        value = input(prompt).lower().strip()
        for i in valid_options:
            if value in i:
                return i
        print(f"Input tidak valid. Pilihan yang tersedia: {', '.join(valid_options).title()}")

def calculate_hotel_price(jenisKamar, namaHotel):
    """Menghitung harga hotel berdasarkan nama hotel dan jenis kamar"""

    return HARGA_KAMAR[jenisKamar] + HARGA_HOTEL[namaHotel]

def get_hotel():
    """Fungsi utama untuk pembelian tiket bus"""
    
    while True:
        try:
            jumlah_kamar = int(input("Berapa kamar yang ingin anda pesan: "))
            if jumlah_kamar > 0:
                break
            print("Jumlah kamar yang harus dipesan minimal 1")
        except ValueError:
            print("Masukkan angka yang valid")
    
    result["jumlah_kamar"] = jumlah_kamar
    
    for i in range(jumlah_kamar):
        print(f"\nTiket ke-{i + 1}")
        
        # Input dan validasi kelas bus
        kelas = validate_input(
            "Masukkan kelas bus [Ekonomi/VIP/Executive]: ",
            KELAS_BUS
        )
        
        # Input dan validasi titik awal
        asal = validate_input(
            "Masukkan titik awal [Bandung/Semarang/Surabaya]: ",
            KOTA_TERSEDIA
        )
        
        # Input dan validasi tujuan
        tujuan = validate_input(
            "Masukkan tujuan [Bandung/Semarang/Surabaya]: ",
            KOTA_TERSEDIA
        )
        
        # Menghitung harga tiket
        harga_tiket = calculate_ticket_price(asal, tujuan)
        
        # Menyimpan data tiket
        result["kelas_bus"].append(kelas.title())
        result["titik_awal"].append(asal.title())
        result["destinasi"].append(tujuan.title())
        result["harga_tiket"].append(harga_tiket)
        result["total_harga_tiket"] += harga_tiket
        
    return result