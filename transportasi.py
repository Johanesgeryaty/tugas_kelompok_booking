def get_transportasi():
    pilihan_valid = ["bus", "pesawat", "kereta"]
    
    while True:
        try:
            transportasi_input = input("Masukkan pilihan transportasi anda [Bus/Pesawat/Kereta]: ").lower().strip()
            
            if transportasi_input in pilihan_valid:
                return transportasi_input
            else:
                print("Maaf, pilihan tidak valid. Silakan pilih: Bus, Pesawat, atau Kereta")
        except KeyboardInterrupt:
            print("\nProgram dihentikan")
            break

get_transportasi()


