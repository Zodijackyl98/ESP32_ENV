import machine
import time
import dht

class DHT:
    DHTLIB_OK = 0
    DHTLIB_ERROR_CHECKSUM = -1
    DHTLIB_ERROR_TIMEOUT = -2
    DHTLIB_INVALID_VALUE = -999
    
    humidity = 0
    temperature = 0
    
    def __init__(self, pin):
        self.pin = pin
        self.sensor = dht.DHT11(machine.Pin(pin))
    
    def readSensor(self):
        try:
            self.sensor.measure()
            self.humidity = self.sensor.humidity()
            self.temperature = self.sensor.temperature()
            return self.DHTLIB_OK
        except OSError as e:
            return self.DHTLIB_ERROR_TIMEOUT

def loop():
    dht_sensor = DHT(32)  # Use GPIO4, adjust as needed
    sumCnt = 0
    okCnt = 0
    while True:
        sumCnt += 1
        chk = dht_sensor.readSensor()
        if chk == dht_sensor.DHTLIB_OK:
            okCnt += 1
        okRate = 100.0 * okCnt / sumCnt
        print(f"sumCnt : {sumCnt}, \t okRate : {okRate:.2f}% ")
        print(f"chk : {chk}, \t Humidity : {dht_sensor.humidity:.2f}, \t Temperature : {dht_sensor.temperature:.2f} ")
        time.sleep(3)

if __name__ == '__main__':
    print('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        pass