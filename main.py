from hotel import hotel as Hotel
from transportasi import transportasi as Trans
from view import view as View
from utils import validateInput as Validate

nama_pembeli = ""

def main():
    while True:
        try:
            View.greeting()
            global nama_pembeli
            nama_pembeli= input("Silahkan masukan nama anda : ")
            pilihan = Validate.validate_input("\nSilahkan anda pilih tiket transportasi atau hotel [Transportasi,Hotel] ? ",["transportasi", "hotel"] )
            if pilihan == "transportasi":
                data = {}
                trans = Trans.get_transportasi()
                x = Validate.validate_input("Apakah anda berminat memesan hotel", ["ya","tidak"])
                if x == "ya":
                    hotel = Hotel.get_hotel()
                    data.update({
                        "transportasi": trans,
                        "hotel": hotel
                        })
                    return data
                elif x == "tidak":
                    data.update({
                        "data": trans
                    })
                    return data
            elif pilihan == "hotel":
                hotel = Hotel.get_hotel()
                x = Validate.validate_input("Apakah anda berminat memesan transportasi", ["ya","tidak"])
                if x == "ya":
                    trans = Trans.get_transportasi()
                    return print(hotel, trans)
                elif x == "tidak":
                    return print(hotel)

        except:
            print("Maaf, ada yang salah, Coba ulangi lagi")
             
if __name__ == "__main__":
    data = main()
    print(data)
    View.view_bill_trans(data,nama_pembeli)
    print(nama_pembeli)