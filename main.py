import bus as bis
nama_pembeli= input("Masukan nama anda : ")
pilihan = input("Mau pesan tiket bus atau hotel [Bus,Hotel] ? ").lower()
if pilihan == "bus":
    bis.get_bus()
    