from hotel import hotel as Hotel
from transportasi import transportasi as Trans

def main():
    while True:
        try:
            # nama_pembeli= input("Masukan nama anda : ")
            pilihan = input("Mau pesan tiket transportasi atau hotel [Transportasi,Hotel] ? ").lower()
            if pilihan == "transportasi":
                
                return print(Trans.get_transportasi())
            elif pilihan == "hotel":
                return print(Hotel.get_hotel())
        except:
            print("anjengggg")
             
if __name__ == "__main__":
    main()