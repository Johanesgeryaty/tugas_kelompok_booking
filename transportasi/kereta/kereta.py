from utils import validateInput as Validate
from view import view as View

# Konstanta untuk harga dan pilihan
HARGA_KERETA = {
    "bandung": 250000,
    "semarang": 150000,
    "surabaya": 200000
}

HARGA_KELAS = {
    "ekonomi" : 0,
    "vip" : 100000,
    "executive" : 200000
}

KELAS_KERETA = list(HARGA_KELAS.keys())

KOTA_TERSEDIA = list(HARGA_KERETA.keys())

result = {
    "tujuan": [],
    "harga_tiket": [],
    "jumlah_tiket": 0,
    "titik_awal": [],
    "kelas": [],
    "total_harga_tiket": 0
}

def calculate_ticket_price(asal, tujuan, kelas):
    """Menghitung harga tiket berdasarkan asal dan tujuan"""
    if asal == tujuan:
        return HARGA_KERETA[asal] + HARGA_KELAS[kelas]
    return HARGA_KERETA[asal] + HARGA_KERETA[tujuan] + HARGA_KELAS[kelas]

def get_train():
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
        View.view_titik_awal(HARGA_KERETA)
        asal = Validate.validate_input(
            "Masukkan titik awal [Bandung/Semarang/Surabaya]: ",
            KOTA_TERSEDIA
        )
        
        # Input dan validasi tujuan
        View.view_titik_tujuan(HARGA_KERETA, asal)
        tujuan = Validate.validate_input(
            "Masukkan tujuan [Bandung/Semarang/Surabaya]: ",
            KOTA_TERSEDIA
        )
        
        # Input dan validasi kelas 
        View.view_kelas(HARGA_KELAS)
        kelas = Validate.validate_input(
        "Masukkan kelas kereta [Ekonomi/VIP/Executive]: ",
        KELAS_KERETA
        )
        
        # Menghitung harga tiket
        harga_tiket = calculate_ticket_price(asal, tujuan, kelas)
        
        # Menyimpan data tiket
        result["kelas"].append(kelas.title())
        result["titik_awal"].append(asal.title())
        result["tujuan"].append(tujuan.title())
        result["harga_tiket"].append(harga_tiket)
        result["total_harga_tiket"] += harga_tiket

    return result