def greeting():
    txt = "{:^41}"
    print("===================================")
    print(txt.format("\033[1m TOKO BANG DICK \033[0m"))
    print("===================================")
    print(f"""Selamat datang di aplikasi booking\n{"{:^35}".format("nomer 1 di indonesia!!")}""")
    print("===================================\n")

def view_hotel(hotel):
    nama_hotel = list(hotel.keys())
    print("========================================")
    print(" No.      Nama Hotel              Harga")
    print("========================================")
    for i in range(len(nama_hotel)):
        print("%i \t %s \t %i " % (i + 1, str(nama_hotel[i]).capitalize(), hotel[nama_hotel[i]]))
    print("========================================")

def view_type(kamar):
    nama_kamar = list(kamar.keys())
    print("Memilih Tipe kamar diatas standart akan dikenakan biaya tambahan sebagai berikut : ")
    print("========================================")
    print(" No.     Tipe Kamar              Harga")
    print("========================================")
    for i in range(len(nama_kamar)):
        if i == 0:
            print("%i \t %s \t\t  " % (i + 1, str(nama_kamar[i]).capitalize()))
            continue
        if i == 1:
            print("%i \t %s \t\t\t %i " % (i + 1, str(nama_kamar[i]).capitalize(), kamar[nama_kamar[i]]))
            continue
        print("%i \t %s \t\t %i " % (i + 1, str(nama_kamar[i]).capitalize(), kamar[nama_kamar[i]]))
    print("========================================")

def view_trans(trans):
    print("Berikut di bawah ini adalah Transportasi Tercepat!!!")
    print("=============================")
    print(" No.     Nama Transportasi  ")
    print("=============================")
    for i in range(len(trans)):
        print("%i \t %s %s" % (i + 1 , str(trans[i]).capitalize(), "Tercepat" ))
    print("=============================")

def view_kelas(kelas):
    tipe_kelas = list(kelas.keys())
    print("Memilih Tipe Kelas diatas ekonomi akan dikenakan biaya tambahan sebagai berikut : ")
    print("========================================")
    print(" No.     Tipe Kelas              Harga")
    print("========================================")
    for i in range(len(kelas)):
        if i == 0:
            print("%i \t %s \t\t  " % (i + 1, str(tipe_kelas[i]).capitalize()))
            continue
        if i == 1:
            print("%i \t %s \t\t\t %i " % (i + 1, str(tipe_kelas[i]).capitalize(), kelas[tipe_kelas[i]]))
            continue
        print("%i \t %s \t\t %i " % (i + 1 , str(tipe_kelas[i]).capitalize(), kelas[tipe_kelas[i]] ))
    print("========================================")

def view_titik_awal(titik):
    titik_awal = list(titik.keys())
    print("========================================")
    print(" No.      Nama Kota              Harga")
    print("========================================")
    for i in range(len(titik_awal)):
        print("%i \t %s \t\t %i " % (i + 1, str(titik_awal[i]).capitalize(), titik[titik_awal[i]]))
    print("========================================")

def view_titik_tujuan(titik,asal):
    titik_awal = list(titik.keys())
    print("Perjalanan ke luar Kota akan dikenakan biaya tambahan sebagai berikut : ")
    print("========================================")
    print(" No.      Nama Kota              Harga")
    print("========================================")
    for i in range(len(titik_awal)):
        if titik_awal[i] == asal or titik_awal[i] == asal or titik_awal[i] == asal:
            asal = " "
            print("%i \t %s \t\t  " % (i + 1, str(titik_awal[i]).capitalize()))
            continue
        print("%i \t %s \t\t %i " % (i + 1, str(titik_awal[i]).capitalize(), titik[titik_awal[i]]))
    print("========================================")

def view_bill_trans(tiket, nama):
    txt = "{:^57}"
    bill = tiket["transportasi"]
    print("==================================================")
    print(txt.format("\033[1m Tagihan Pembayaran \033[0m"))
    print("==================================================")
    print("%s \t %s \t %s \t %s" % ("No.", "Titik Awal", "Tujuan", "Harga"))
    print("==================================================")
    for i in range(bill["jumlah_tiket"]):
        print("%i \t %s \t %s \t %i" % (i + 1, bill["titik_awal"][i], bill["tujuan"][i], bill["harga_tiket"][i]))
    print("==================================================")
    print("\t \t \t %s" % (f"Total Harga Rp. {bill["total_harga_tiket"]}"))
    print(f"Terimakasih sudah membeli produk kami {nama}")

def view_bill_hotel(tiket, nama):
    txt = "{:^57}"
    bill = tiket["hotel"]
    print("==================================================")
    print(txt.format("\033[1m Tagihan Pembayaran \033[0m"))
    print("==================================================")
    print("%s \t %s \t %s \t %s" % ("No.", "Nama Hotel", "Tipe Kamar", "Harga"))
    print("==================================================")
    for i in range(bill["jumlah_kamar"]):
        print("%i \t %s \t %s \t %i" % (i + 1, bill["nama_hotel"][i], bill["tipe_kamar"][i], bill["harga_hotel"][i]))
    print("==================================================")
    print("\t \t \t %s" % (f"Total Harga Rp. {bill["total_harga_hotel"]}"))
    print(f"Terimakasih sudah membeli produk kami {nama}")

def view_bill2(tiket):
    transportasi = tiket["transportasi"]
    hotel = tiket["hotel"]
    for i in range(transportasi["jumlah_tiket"]):
        print(i)
    for i in range(hotel["jumlah_tiket"]):
        print(i)
