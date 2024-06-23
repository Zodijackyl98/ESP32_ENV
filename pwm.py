import machine
import time

pin_pwm = machine.Pin(32)
pwm = machine.PWM(pin_pwm)

pwm.freq(100)
#pwm.duty(512) #out of 1023, it's %50 with 512, %25 with 256

led = machine.Pin(33, machine.Pin.OUT)


while True:
    try:
        led.on()
        for i in range(0, 1024, 10):
            pwm.duty(i)
            time.sleep(0.01)
        led.off()
        for i in range(1023, -1, -10):
            pwm.duty(i)
            time.sleep(0.01)
    except KeyboardInterrupt:
        print('User interuption')
        pwm.duty(0)
        led.off()
        break
