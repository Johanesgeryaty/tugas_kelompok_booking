import bus as bis
from bus import result

def main():
        nama_pembeli= input("Masukan nama anda : ")
        pilihan = input("Mau pesan tiket transportasi atau hotel [Bus,Hotel] ? ").lower()
        if pilihan == "bus":
            bis.get_bus()

if __name__ == "__main__":
    main()
    print(result)