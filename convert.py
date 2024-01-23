import sys

def convert_hex_to_list(hex_string):
    return [int(hex_string[i:i+2], 16) for i in range(0, len(hex_string), 2)]

def format_as_dict(hex_list):
    return "{" + ",".join([f"0x{val:02X}" for val in hex_list]) + "}"

if len(sys.argv) != 2:
    print("Usage: python script.py input_file.txt")
    sys.exit(1)

input_file = sys.argv[1]

with open(input_file, "r") as file:
    lines = file.readlines()

converted_data = [format_as_dict(convert_hex_to_list(line.strip())) for line in lines]

output = "{" + ",".join(converted_data) + "}"

print(output)
