HARGA_HOTEL = {
    "mercure(bandung)": 300000,
    "novotel(semarang)": 200000,
    "sheraton(surabaya)": 250000
}
nama_hotel = list(HARGA_HOTEL.keys())



x = input(nama_hotel)

for i in nama_hotel:
    if x in i:
        print(i)

