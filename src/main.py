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

print("Sistema Kanban Inicializado")

while True:
    tempo_atual = time.ticks_ms()
    
    ldr_value = ldr.read()
    button_state = button.value()

    if last_button_state == 1 and button_state == 0:
        silenced = True
        time.sleep_ms(50)
    last_button_state = button_state

    if ldr_value == 0:
        status_msg = "ALERTA: Caixa ausente ou erro de calibração no sensor HX711!"
    elif ldr_value == 150:
        status_msg = "Evento de reposição disparado! Caixa vazia detectada."
    elif ldr_value == 5000:
        status_msg = "Abastecimento concluído. Caixa cheia."
    elif ldr_value == 2500:
        status_msg = "Status: Estoque Regular (2500g)"
    elif ldr_value > THRESHOLD:
        status_msg = "ALERTA: Luz Baixa"
    else:
        status_msg = "OK: Luz Normal"

    if ldr_value > THRESHOLD or ldr_value == 150 or ldr_value == 0:
        led.value(1)
        buzzer.value(0 if silenced and ldr_value != 0 else 1)
    else:
        led.value(0)
        buzzer.value(0)
        silenced = False  

    if time.ticks_diff(tempo_atual, last_print_time) >= INTERVALO_PRINT:
        print(f"LDR: {ldr_value} | Status: {status_msg}")
        last_print_time = tempo_atual

    time.sleep_ms(10)