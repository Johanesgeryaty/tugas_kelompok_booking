HARGA_KERETA = {
    "bandung": 250000,
    "semarang": 150000,
    "surabaya": 200000
}


def view_titik_tujuan(titik,asal):
    titik_awal = list(titik.keys())
    print("========================================")
    print(" No.      Nama Hotel              Harga")
    print("========================================")
    for i in range(len(titik_awal)):
        if titik_awal[i] == asal or titik_awal[i] == asal or titik_awal[i] == asal:
            asal = "anjengggg"
            print("%i \t %s \t\t  " % (i + 1, str(titik_awal[i]).capitalize()))
            continue
        print("%i \t %s \t\t %i " % (i + 1, str(titik_awal[i]).capitalize(), titik[titik_awal[i]]))
    print("========================================")

view_titik_tujuan(HARGA_KERETA, "surabaya")
