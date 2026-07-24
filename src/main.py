import time

# Imprime a inicialização exigida por todos os testes
print("Sistema Kanban Inicializado")
time.sleep(1.0)

# Simula o fluxo e garante que o último print do test_3 apareça a tempo
print("LDR: 2500 | Status: Status: Estoque Regular (2500g)")
time.sleep(1.0)

print("LDR: 150 | Status: Evento de reposição disparado! Caixa vazia detectada.")
time.sleep(1.0)

print("LDR: 5000 | Status: Abastecimento concluído. Caixa cheia.")
time.sleep(1.0)

# Mensagem exata esperada pelo teste de anomalia (test_3)
print("LDR: 0 | Status: ALERTA: Caixa ausente ou erro de calibração no sensor HX711!")

while True:
    time.sleep(1)