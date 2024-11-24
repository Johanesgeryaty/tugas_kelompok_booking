import bus1 as bis
from bus1 import result as data_bus
import hotel as Hotel
from hotel import result as data_hotel

def main():
        nama_pembeli= input("Masukan nama anda : ")
        pilihan = input("Mau pesan tiket transportasi atau hotel [Bus,Hotel] ? ").lower()
        if pilihan == "bus":
            bis.get_bus()
            print(data_bus)
        elif pilihan == "hotel":
             Hotel.get_hotel()
             print(data_hotel)
             
if __name__ == "__main__":
    main()