# ESP32_ENV
Discovering what options ESP32 offers based on Micropython. Purpose of this project is to learn main functions of ESP32 by practising with different sensor and communication methods.

Any documentation, datasheet about ESP32 specifically for the model I work with can be found inside the folder.

You can find different files for different sensor and processes which can be done with ESP32(D2WD) using only Micropython. Project include so far;
  - Receiving data from NEO-6M GPS sensor via U2TXD and U2RXD pins on ESP32. Users can easily choose pins that are available for UART communication easily by adjusting the code. Be wary that one also needs to change UART peripheral ID(in this case it's 2) to use other pins.
  
  - Changing PWM states of a GPIO pin.

  - Using DHT11 temperature and humidity sensor with ESP32.

  - Reading values from 12-bit Analog to Digital converter which ESP32 supports on designated pins.

  - Setting ESP32 up for an Access Point and connecting it to any network in the area.
