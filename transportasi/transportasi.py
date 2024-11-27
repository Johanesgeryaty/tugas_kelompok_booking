from transportasi.bus import bus1 as Bus
from transportasi.kereta import kereta as Kereta
from hotel import hotel as Hotel
from utils import validateInput as Validate
from view import view as View

def get_transportasi():
    pilihan_valid = ["bus", "kereta"]
    while True:
        try:
            View.view_trans(pilihan_valid)
            transportasi_input = input("Masukkan pilihan transportasi anda [Bus/Kereta]: ").lower().strip()
            
            if transportasi_input in pilihan_valid:
                match transportasi_input:
                    case "bus":
                        bus = Bus.get_bus()
                        return bus
                    case "kereta":
                        kereta = Kereta.get_train()
                        return kereta
                    case _:
                        break

            else:
                print("Maaf, pilihan tidak valid. Silakan pilih: Bus, atau Kereta")
        except KeyboardInterrupt:
            print("\nProgram dihentikan")
            break




