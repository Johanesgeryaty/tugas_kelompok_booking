def greeting():
    txt = "{:^43}"
    print("===================================")
    print(txt.format("\033[1m Bookit \033[0m"))
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
    txt = "{:^70}"
    transportasi = tiket["transportasi"]
    print("=================================================================")
    print(txt.format("\033[1m Tagihan Pembayaran \033[0m"))
    print("=================================================================")
    print("%s \t %s \t %s \t %s \t\t %s" % ("No.", "Titik Awal", "Tujuan", "Kelas","Harga"))
    print("-----------------------------------------------------------------")
    for i in range(transportasi["jumlah_tiket"]):
        if transportasi["kelas"][i] == "Vip":
            print("%i \t %s \t %s \t %s\t\t %i" % (i + 1, transportasi["titik_awal"][i], transportasi["tujuan"][i], transportasi["kelas"][i], transportasi["harga_tiket"][i]))
            print("-----------------------------------------------------------------")
            continue
        print("%i \t %s \t %s\t %s \t %i" % (i + 1, transportasi["titik_awal"][i], transportasi["tujuan"][i], transportasi["kelas"][i], transportasi["harga_tiket"][i]))
        print("-----------------------------------------------------------------")
    print("=================================================================")
    print("\t \t \t \t %s" % (f"Total Harga Rp. {transportasi["total_harga_tiket"]}"))
    while True:
        try:
            bayar = int(input("Masukkan uang bayar anda: "))
            if bayar > transportasi["total_harga_tiket"]:
                print(f"Uang yang anda masukkan adalah {bayar}, kembalian anda {bayar - transportasi["total_harga_tiket"]}")
                print(f"Terimakasih {nama} telah memesan tiket transportasi di agen kami")
                break
            elif bayar == transportasi["total_harga_tiket"]:
                print(f"Uang yang anda masukkan adalah {bayar}, Uang anda Pas")
                print(f"Terimakasih {nama} telah memesan tiket transportasi di agen kami")
                break
            else:
                print("Maaf uang yang anda masukkan kurang, Silahkan coba lagi")
        except:
            print("Maaf ada yang salah")


def view_bill_hotel(tiket, nama):
    txt = "{:^70}"
    hotel = tiket["hotel"]
    print("=========================================================")
    print(txt.format("\033[1m Tagihan Pembayaran \033[0m"))
    print("=========================================================")
    print("%s \t %s \t\t %s \t %s" % ("No.", "Nama Hotel", "Tipe Kamar", "Harga"))
    print("---------------------------------------------------------")
    for i in range(hotel["jumlah_kamar"]):
        if hotel["tipe_kamar"][i] == "Twin":
            print("%i \t %s \t %s \t\t %i" % (i + 1, hotel["nama_hotel"][i], hotel["tipe_kamar"][i], hotel["harga_hotel"][i]))
            print("---------------------------------------------------------")
            continue
        print("%i \t %s \t %s \t %i" % (i + 1, hotel["nama_hotel"][i], hotel["tipe_kamar"][i], hotel["harga_hotel"][i]))
        print("---------------------------------------------------------")
    print("=========================================================")
    print("\t \t \t \t %s" % (f"Total Harga Rp. {hotel["total_harga_hotel"]}"))
    while True:
        try:
            bayar = int(input("Masukkan uang bayar anda: "))
            if bayar > hotel["total_harga_hotel"]:
                print(f"Uang yang anda masukkan adalah {bayar}, kembalian anda {bayar - hotel["total_harga_hotel"]}")
                print(f"Terimakasih {nama} telah memesan hotel di agen kami")
                break
            elif bayar == hotel["total_harga_hotel"]:
                print(f"Uang yang anda masukkan adalah {bayar}, Uang anda Pas")
                print(f"Terimakasih {nama} telah memesan hotel di agen kami")
                break
            else:
                print("Maaf uang yang anda masukkan kurang, Silahkan coba lagi")
        except:
            print("Maaf ada yang salah")

def view_bill2(tiket, nama):
    txt = "{:^70}"
    transportasi = tiket["transportasi"]
    hotel = tiket["hotel"]
    print("=================================================================")
    print(txt.format("\033[1m Tagihan Pembayaran \033[0m"))
    print("=================================================================")
    print("%s \t %s \t %s \t %s \t\t %s" % ("No.", "Titik Awal", "Tujuan", "Kelas","Harga"))
    print("-----------------------------------------------------------------")
    for i in range(transportasi["jumlah_tiket"]):
        if transportasi["kelas"][i] == "Vip":
            print("%i \t %s \t %s \t %s\t\t %i" % (i + 1, transportasi["titik_awal"][i], transportasi["tujuan"][i], transportasi["kelas"][i], transportasi["harga_tiket"][i]))
            print("-----------------------------------------------------------------")
            continue
        print("%i \t %s \t %s \t %s\t %i" % (i + 1, transportasi["titik_awal"][i], transportasi["tujuan"][i], transportasi["kelas"][i], transportasi["harga_tiket"][i]))
        print("-----------------------------------------------------------------")
    print("=================================================================")
    print("\t \t \t %s" % (f"Total Harga Transportasi Rp. {transportasi["total_harga_tiket"]}"))
    print()
    print("=================================================================")
    print("%s \t %s \t\t %s \t %s" % ("No.", "Nama Hotel", "Tipe Kamar", "Harga"))
    print("-----------------------------------------------------------------")
    for i in range(hotel["jumlah_kamar"]):
        if hotel["tipe_kamar"][i] == "Twin":
            print("%i \t %s \t %s \t\t %i" % (i + 1, hotel["nama_hotel"][i], hotel["tipe_kamar"][i], hotel["harga_hotel"][i]))
            print("-----------------------------------------------------------------")
            continue
        print("%i \t %s \t %s \t %i" % (i + 1, hotel["nama_hotel"][i], hotel["tipe_kamar"][i], hotel["harga_hotel"][i]))
        print("-----------------------------------------------------------------")

    print("=================================================================")
    print("\t \t \t \t%s" % (f"Total Harga Kamar Hotel Rp. {hotel["total_harga_hotel"]}"))
    tagihan = hotel["total_harga_hotel"] + transportasi["total_harga_tiket"]
    print(f"Total Harga Pesanan Anda Rp. {tagihan} ")

    while True:
        try:
            bayar = int(input("Masukkan uang bayar anda: "))
            if bayar > tagihan:
                print(f"Uang yang anda masukkan adalah {bayar}, kembalian anda {bayar - tagihan}")
                print(f"Terimakasih {nama} telah memesan tiket transportasi dan hotel di agen kami")
                break
            elif bayar == tagihan:
                print(f"Uang yang anda masukkan adalah {bayar}, Uang anda Pas")
                print(f"Terimakasih {nama} telah memesan tiket transportasi dan hotel di agen kami")
                break
            else:
                print("Maaf uang yang anda masukkan kurang, Silahkan coba lagi")
        except:
            print("Maaf ada yang salah")