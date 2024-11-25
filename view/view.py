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
        print("%i \t %s \t %i " % (i + 1, nama_hotel[i], hotel[nama_hotel[i]]))
    print("========================================")

def view_type(kamar):
    nama_kamar = list(kamar.keys())
    print("========================================")
    print(" No.     Nama Kamar              Harga")
    print("========================================")
    for i in range(len(nama_kamar)):
        if i == 1:
            print("%i \t %s \t\t\t %i " % (i + 1, nama_kamar[i], kamar[nama_kamar[i]]))
            continue
        print("%i \t %s \t\t %i " % (i + 1, nama_kamar[i], kamar[nama_kamar[i]]))
    print("========================================")

