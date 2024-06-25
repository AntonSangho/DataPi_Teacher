from machine import Pin, I2C
from utime import sleep
from neopixel import NeoPixel
from bh1750 import BH1750

# NeoPixel 설정
np0 = NeoPixel(machine.Pin(21), 1)

# NeoPixel 제어 함수
# NeoPixel을 켜는 함수
def np_on():
    for i in range(0, np0.n):
        # Magenta 으로 설정
        np0[i] = (126, 000, 129)
    np0.write()
# NeoPixel을 끄는 함수
def np_off():
    for i in range(0, np0.n):
        np0[i] = (0, 0, 0)
    np0.write()

# I2C 설정
i2c0_sda = Pin(4)
i2c0_scl = Pin(5)
i2c0 = I2C(0, sda=i2c0_sda, scl=i2c0_scl)

# 조도센서 설정
bh1750 = BH1750(0x23, i2c0)

# 메인 루프
try: 
    while True:
        np_on()
        print(bh1750.measurement)
        sleep(1)
finally:
    np_off()
    print('finish')

