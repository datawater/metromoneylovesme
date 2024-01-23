import sys

if len(sys.argv) != 2:
    print("Usage: python script.py input_file.txt")
    sys.exit(1)

input_file = sys.argv[1]

with open(input_file, "r") as file:
    lines = file.readlines()

converted_data = ""

for i, line in enumerate(lines):
    converted_data += f"#ifdef PART_{i}\nbyte knownKeys[NR_KNOWN_KEYS][MFRC522::MF_KEY_SIZE] = {line.strip()};\n#endif\n"

print(converted_data)
