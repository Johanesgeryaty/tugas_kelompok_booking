from transportasi.bus import bus1 as Bus
from transportasi.kereta import kereta as Kereta
from hotel import hotel as Hotel
from utils import validateInput as Validate

def get_transportasi():
    pilihan_valid = ["bus", "kereta"]
    
    while True:
        try:
            transportasi_input = input("Masukkan pilihan transportasi anda [Bus/Kereta]: ").lower().strip()
            
            if transportasi_input in pilihan_valid:
                match transportasi_input:
                    case "bus":
                        bus = Bus.get_bus()
                        x = Validate.validate_input("Apakah anda ingin memesan kamar hotel? (Ya/Tidak)", ["ya", "tidak"])
                        if x == "ya":
                            # hotel = Hotel.get_hotel()
                            return Hotel.get_hotel
                        elif x == "tidak":
                            return bus
                            
                    case "kereta":
                        Kereta.get_train()
                        x = Validate.validate_input("Apakah anda ingin memesan kamar hotel? (Ya/Tidak)", ["ya", "tidak"])
                        if x == "ya":
                            hotel = Hotel.get_hotel()
                            break
                        elif x == "tidak":
                            break
                    case _:
                        break

            else:
                print("Maaf, pilihan tidak valid. Silakan pilih: Bus, atau Kereta")
        except KeyboardInterrupt:
            print("\nProgram dihentikan")
            break




