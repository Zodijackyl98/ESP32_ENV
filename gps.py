import machine
import time

# Configure UART2 on GPIO17 (TX2) and GPIO16 (RX2)
uart2 = machine.UART(2, baudrate=9600, tx=17, rx=16)

def read_gps():
    line_buffer = bytearray()  # Buffer to accumulate bytes
    while True:
        if uart2.any():
            byte = uart2.read(1)  # Read one byte from UART
            if byte == b'\n':  # Check for end of line
                try:
                    line_str = line_buffer.decode('ascii', 'ignore').strip()  # Decode accumulated bytes to string
                    print(line_str)
                    line_buffer = bytearray()  # Clear buffer for next line
                    if line_str.startswith('$GNGGA'):
                        parse_gpgga(line_str)
                except UnicodeError:
                    print('Unicode Error Occured')
                    line_buffer = bytearray()
            else:
                line_buffer.extend(byte)  # Accumulate bytes in buffer

def parse_gpgga(gpgga_sentence):
    parts = gpgga_sentence.split(',')
    
    time_utc = parts[1]
    latitude = convert_to_degrees(parts[2])
    latitude_direction = parts[3]
    longitude = convert_to_degrees(parts[4])
    longitude_direction = parts[5]
    fix_quality = parts[6]
    num_satellites = parts[7]
    horizontal_dilution = parts[8]
    altitude = parts[9]
    altitude_units = parts[10]
    
    print(f"Time (UTC): {time_utc}")
    print(f"Latitude: {latitude} {latitude_direction}")
    print(f"Longitude: {longitude} {longitude_direction}")
    print(f"Fix Quality: {fix_quality}")
    print(f"Number of Satellites: {num_satellites}")
    print(f"Horizontal Dilution: {horizontal_dilution}")
    print(f"Altitude: {altitude} {altitude_units}")

def convert_to_degrees(raw_value):
    raw_value = float(raw_value)
    degrees = int(raw_value / 100)
    minutes = raw_value - (degrees * 100)
    return degrees + (minutes / 60)

# Run the GPS reading function
read_gps()