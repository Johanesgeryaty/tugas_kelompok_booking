from hotel import hotel as Hotel
from transportasi import transportasi as Trans
from view import view as View
from utils import validateInput as Validate
import pandas as pd

nama_pembeli = ""

def main():
    while True:
        try:
            View.greeting()
            global nama_pembeli
            nama_pembeli= input("Silahkan masukan nama anda : ")
            data = {"layanan tersedia" : ["transportasi", "hotel"]}
            df = pd.DataFrame(data,index=[1,2])
            print("\n",df)
            pilihan = Validate.validate_input("\nSilahkan anda pilih tiket transportasi atau hotel [1,2] ? ", ["1", "2"])
            if pilihan == "1":
                data = {}
                trans = Trans.get_transportasi()
                x = Validate.validate_input("Apakah anda berminat memesan hotel [ya/tidak]? ", ["ya","tidak"])
                if x == "ya":
                    hotel = Hotel.get_hotel()
                    data.update({
                        "transportasi": trans,
                        "hotel": hotel
                        })
                    return data
                elif x == "tidak":
                    data.update({
                        "transportasi": trans
                    })
                    return data
            elif pilihan == "2":
                hotel = Hotel.get_hotel()
                data = {}
                x = Validate.validate_input("Apakah anda berminat memesan transportasi[ya/tidak]? ", ["ya","tidak"])
                if x == "ya":
                    trans = Trans.get_transportasi()
                    data.update({
                        "transportasi": trans,
                        "hotel": hotel
                        })
                    return data
                elif x == "tidak":
                    data.update({
                        "hotel": hotel
                    })
                    return data

        except:
            print("Maaf, ada yang salah, Coba ulangi lagi")
             
if __name__ == "__main__":
    data = main()
    if len(data) == 1 :
        if "transportasi" in data:
            View.view_bill_trans(data,nama_pembeli)
        elif "hotel" in data:
            View.view_bill_hotel(data,nama_pembeli)
    elif len(data) == 2 :
        View.view_bill2(data,nama_pembeli)