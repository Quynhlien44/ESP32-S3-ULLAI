# sensor_emulator.py
import serial
import time
import random

# Tạo cổng COM ảo
port = '/dev/pts/2' 
try:
    ser = serial.Serial(port, 115200, timeout=1)
    print(f"Virtual sensor running on {port}...")
    
    while True:
        timestamp = int(time.time() * 1000)
        light = 1.0 + 0.5 * random.random()
        temp = 25.0 + 5.0 * random.random()
        humidity = 45.0 + 20.0 * random.random()
        tvoc = 60.0 + 20.0 * random.random()
        co2 = 450.0 + 50.0 * random.random()
        
        data_line = f"{timestamp},{light:.4f},{temp:.2f},{humidity:.1f},{tvoc:.1f},{co2:.1f}"
        print(f"Emulated: {data_line}")  # In ra terminal
        data = data_line + "\n"
        ser.write(data.encode('utf-8'))
        time.sleep(0.1)
        
except serial.SerialException as e:
    print(f"Error: {e}")
    print("Available ports:")
    import serial.tools.list_ports
    ports = serial.tools.list_ports.comports()
    for p in ports:
        print(p.device)