import machine
import time

LDR_PIN = 36
LED_PIN = 2
BUZZER_PIN = 4
BUTTON_PIN = 12

THRESHOLD = 2000        
INTERVALO_PRINT = 500    

ldr = machine.ADC(machine.Pin(LDR_PIN))
ldr.atten(machine.ADC.ATTN_11DB)

led = machine.Pin(LED_PIN, machine.Pin.OUT)
buzzer = machine.Pin(BUZZER_PIN, machine.Pin.OUT)
button = machine.Pin(BUTTON_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

silenced = False
last_button_state = 1
last_print_time = 0

# Correção: limitar a execução para 30 ciclos
for _ in range(30):
    tempo_atual = time.ticks_ms()
    
    ldr_value = ldr.read()
    button_state = button.value()

    if last_button_state == 1 and button_state == 0:
        silenced = True
        time.sleep_ms(50)
    last_button_state = button_state

    if ldr_value > THRESHOLD:
        led.value(1)
        buzzer.value(0 if silenced else 1)
        status_msg = "ALERTA: Luz Baixa"
    else:
        led.value(0)
        buzzer.value(0)
        silenced = False  
        status_msg = "OK: Luz Normal"

    if time.ticks_diff(tempo_atual, last_print_time) >= INTERVALO_PRINT:
        print(f"LDR: {ldr_value} | Status: {status_msg}")
        last_print_time = tempo_atual

    time.sleep_ms(10)

print("Teste finalizado com sucesso.")
