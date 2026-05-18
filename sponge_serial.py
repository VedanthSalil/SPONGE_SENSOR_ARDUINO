import serial

SERIAL_PORT = "COM4"
BAUD_RATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
print(f"Listening on {SERIAL_PORT}...")

while True:
    line = ser.readline().decode("utf-8", errors="replace").rstrip()
    if line:
        print(line)
    parts = line.split()
    if len(parts) < 3:
        continue

    value = parts[2]
    print(value)

    try:
        with open("storage.py", "w") as storage_file:
            storage_file.write(f"value = {value}\n")
        print(f"  -> Saved {value} to storage.py")
    except Exception as e:
        print(f"  -> Error writing to storage.py: {e}")