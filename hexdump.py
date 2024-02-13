import sys

hex_string_metro = open(sys.argv[1], "r").read().replace(" ", "").replace("\n", "")
hex_data_metro = bytearray.fromhex(hex_string_metro)

f_metro = open("data/metromani1.dat", "wb")

f_metro.write(hex_data_metro)
