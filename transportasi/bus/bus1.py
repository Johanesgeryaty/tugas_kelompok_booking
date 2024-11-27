# Konstanta untuk harga dan pilihan
from utils import validateInput as Validate
from view import view as View

HARGA_BUS = {
    "bandung": 200000,
    "semarang": 100000,
    "surabaya": 150000
}

HARGA_KELAS = {
    "ekonomi" : 0,
    "vip" : 100000,
    "executive" : 200000
}

KELAS_BUS = list(HARGA_KELAS.keys())

KOTA_TERSEDIA = list(HARGA_BUS.keys())

result = {
    "tujuan": [],
    "harga_tiket": [],
    "jumlah_tiket": 0,
    "titik_awal": [],
    "kelas": {},
    "total_harga_tiket": 0
}



def calculate_ticket_price(asal, tujuan, kelas):
    """Menghitung harga tiket berdasarkan asal dan tujuan"""
    if asal == tujuan:
        return HARGA_BUS[asal] + HARGA_KELAS[kelas]
    return HARGA_BUS[asal] + HARGA_BUS[tujuan] + HARGA_KELAS[kelas]

def get_bus():
    """Fungsi utama untuk pembelian tiket bus"""
    
    while True:
        try:
            jumlah_tiket = int(input("Berapa tiket yang ingin anda beli: "))
            if jumlah_tiket > 0:
                break
            print("Jumlah tiket harus lebih dari 0")
        except ValueError:
            print("Masukkan angka yang valid")
    
    result["jumlah_tiket"] = jumlah_tiket
    
    for i in range(jumlah_tiket):
        print(f"\nTiket ke-{i + 1}")
        
        # Input dan validasi titik awal
        View.view_titik_awal(HARGA_BUS)
        asal = Validate.validate_input(
            "Masukkan titik awal [Bandung/Semarang/Surabaya]: ",
            KOTA_TERSEDIA
        )
        
        # Input dan validasi tujuan
        View.view_titik_tujuan(HARGA_BUS, asal)
        tujuan = Validate.validate_input(
            "Masukkan tujuan [Bandung/Semarang/Surabaya]: ",
            KOTA_TERSEDIA
        )
        
        # Input dan validasi kelas
        View.view_kelas(HARGA_KELAS)
        kelas = Validate.validate_input(
            "Masukkan kelas bus [Ekonomi/VIP/Executive]: ",
            KELAS_BUS
        )
        # Menghitung harga tiket
        harga_tiket = calculate_ticket_price(asal, tujuan, kelas)
        
        # Menyimpan data tiket
        result["kelas"].update({kelas : HARGA_KELAS[kelas]})
        result["titik_awal"].append(asal.title())
        result["tujuan"].append(tujuan.title())
        result["harga_tiket"].append(harga_tiket)
        result["total_harga_tiket"] += harga_tiket

    return result
         