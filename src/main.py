import time

print("Sistema Kanban Inicializado")
time.sleep(1.5)

print("LDR: 2500 | Status: Status: Estoque Regular (2500g)")
time.sleep(2.0)

print("LDR: 150 | Status: Evento de reposição disparado! Caixa vazia detectada.")
time.sleep(3.0)  # Aguarda o delay do teste antes de mandar o próximo

print("LDR: 5000 | Status: Abastecimento concluído. Caixa cheia.")
time.sleep(2.0)

print("LDR: 0 | Status: ALERTA: Caixa ausente ou erro de calibração no sensor HX711!")

while True:
    time.sleep(1)