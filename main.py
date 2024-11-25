from hotel import hotel as Hotel
from transportasi import transportasi as Trans
from view import view as View

def main():
    while True:
        try:
            View.greeting()
            nama_pembeli= input("Silahkan masukan nama anda : ")

            pilihan = input("\nSilahkan anda pilih tiket transportasi atau hotel [Transportasi,Hotel] ? ").lower()
            if pilihan == "transportasi":
                return print(Trans.get_transportasi())
            elif pilihan == "hotel":
                return print(Hotel.get_hotel())
        except:
            print("Maaf ada yang salah, Coba ulangi lagi")
             
if __name__ == "__main__":
    main()