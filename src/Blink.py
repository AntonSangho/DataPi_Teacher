"""
LED를 0.5초 간격으로 깜박이는 의사 코드

1. LED 핀 설정
2. 무한 루프
    3. LED 켜기
    4. 0.5초 대기
    5. LED 끄기
    6. 0.5초 대기

"""

from machine import Pin 
import utime # 시간 관련 라이브러리 

# LED 핀 설정
led = Pin("LED", Pin.OUT)  


while True:             # 무한 루프
    led.value(1)        # LED 켜기    
    utime.sleep(0.5)    # 0.5초 대기 
    led.value(0)        # LED 끄기 
    utime.sleep(0.5)    # 0.5초 대기 

