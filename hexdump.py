hex_string_metro = open("decrypt.txt", "r").read().replace(" ", "").replace("\n", "")
hex_data_metro = bytearray.fromhex(hex_string_metro)

f_metro = open("data/metromani.dat", "wb")

f_metro.write(hex_data_metro)