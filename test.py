import pandas as pd
# a = {
#     "bandung" : ["lautan api", "bubur"],
#     "jakarta" : ["banjir", "sate"]
# }


# HARGA_KELAS = {
#     "ekonomi" : 0,
#     "vip" : 100000,
#     "executive" : 200000
# }

# HARGA_BUS = {
#     "bandung": 200000,
#     "semarang": 100000,
#     "surabaya": 150000
# }

# # KELAS_BUS = list(HARGA_KELAS.keys())
# KOTA_TERSEDIA = list(HARGA_BUS.keys())
# BUS = list(HARGA_BUS.values())

# data = {
#     "kota tersedia": KOTA_TERSEDIA,
#     "harga ": BUS,
# }


data = {"layanan tersedia" : ["transportasi", "hotel"]}

df = pd.DataFrame(data,index=[1,2])
print(df)