from machine import Pin, PWM
from utime import sleep, ticks_us, ticks_diff
import dht

# ------------------------------
# HC-SR04
# ------------------------------
trig = Pin(2, Pin.OUT)
echo = Pin(3, Pin.IN)

# ------------------------------
# DHT22
# ------------------------------
sensor = dht.DHT22(Pin(18))

# ------------------------------
# BUZZER – PWM GP16
# ------------------------------
buzzer = PWM(Pin(16))
buzzer.freq(2000)
buzzer.duty_u16(0)

# ------------------------------
# LED – GP21
# ------------------------------
led = Pin(21, Pin.OUT)

# ------------------------------
# FUNÇÃO DE DISTÂNCIA
# ------------------------------
def medir_distancia():
    trig.low()
    sleep(0.002)
    trig.high()
    sleep(0.00001)
    trig.low()

    timeout = ticks_us()
    while echo.value() == 0:
        if ticks_diff(ticks_us(), timeout) > 30000:
            return -1

    inicio = ticks_us()
    while echo.value() == 1:
        if ticks_diff(ticks_us(), inicio) > 30000:
            return -1

    fim = ticks_us()
    duracao = ticks_diff(fim, inicio)
    distancia = (duracao / 2) / 29.1
    return distancia

# ------------------------------
# LOOP PRINCIPAL
# ------------------------------
while True:

    # --- LED + BUZZER SINCRONIZADOS ---
    led.value(1)              # LED acende
    buzzer.duty_u16(30000)    # Buzzer toca
    sleep(0.5)

    led.value(0)              # LED apaga
    buzzer.duty_u16(0)        # Buzzer silencia
    sleep(0.5)

    # --- Medição de distância ---
    distancia = medir_distancia()
    print("Distância:", distancia, "cm")

    # --- Sensor DHT22 ---
    try:
        sensor.measure()
        print("Temp:", sensor.temperature(), "°C / Hum:", sensor.humidity(), "%")
    except:
        print("Erro no DHT22")