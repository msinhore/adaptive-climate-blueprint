#!/usr/bin/env python3
"""
Debug script para testar a detecção de janela/porta aberta.
Este script simula o que acontece quando uma janela é aberta e mostra
os valores que a automação vê em cada execução.
"""

import time
from datetime import datetime

def simulate_window_detection(initial_temp, final_temp, threshold, detection_time_minutes):
    """
    Simula o processo de detecção de janela aberta
    """
    print(f"=== SIMULAÇÃO DE DETECÇÃO DE JANELA ===")
    print(f"Temperatura inicial: {initial_temp}°C")
    print(f"Temperatura final: {final_temp}°C")
    print(f"Threshold: {threshold}°C")
    print(f"Janela de detecção: {detection_time_minutes} minutos")
    print(f"Mudança esperada: {abs(final_temp - initial_temp)}°C")
    print()
    
    # Simula as execuções da automação
    current_temp = initial_temp
    previous_temp = initial_temp  # Valor armazenado no helper
    
    print("EXECUÇÕES DA AUTOMAÇÃO:")
    print("-" * 60)
    
    # Execução 1: Condições normais (antes da janela abrir)
    execution = 1
    print(f"Execução {execution} - {datetime.now().strftime('%H:%M:%S')} (Antes de abrir janela)")
    print(f"  Previous temp (helper): {previous_temp}°C")
    print(f"  Current temp (sensor):  {current_temp}°C")
    temp_change = abs(previous_temp - current_temp)
    print(f"  Mudança de temperatura: {temp_change}°C")
    print(f"  Detecção triggered? {'SIM' if temp_change >= threshold else 'NÃO'}")
    print(f"  Helper updated to: {current_temp}°C")
    print()
    
    # Atualiza o helper (como a automação faz)
    previous_temp = current_temp
    
    # Simula a abertura da janela (mudança rápida)
    time.sleep(1)  # Pequena pausa para simular
    current_temp = final_temp
    
    # Execução 2: Logo após a janela abrir (triggered por state change)
    execution += 1
    print(f"Execução {execution} - {datetime.now().strftime('%H:%M:%S')} (JANELA ABERTA - Sensor mudou)")
    print(f"  Previous temp (helper): {previous_temp}°C")
    print(f"  Current temp (sensor):  {current_temp}°C")
    temp_change = abs(previous_temp - current_temp)
    temp_drop = previous_temp - current_temp
    temp_rise = current_temp - previous_temp
    print(f"  Mudança de temperatura: {temp_change}°C")
    print(f"  Queda de temperatura: {temp_drop}°C")
    print(f"  Subida de temperatura: {temp_rise}°C")
    print(f"  Detecção triggered? {'SIM' if temp_change >= threshold else 'NÃO'}")
    
    if temp_change >= threshold:
        if temp_drop >= threshold:
            print(f"  TIPO: Queda de temperatura detectada (cenário inverno)")
        elif temp_rise >= threshold:
            print(f"  TIPO: Subida de temperatura detectada (cenário verão)")
        print(f"  AÇÃO: HVAC pausado por {detection_time_minutes} minutos")
    
    print(f"  Helper updated to: {current_temp}°C")
    print()
    
    # Execução 3: Próxima execução programada (10 min depois)
    previous_temp = current_temp
    execution += 1
    print(f"Execução {execution} - {datetime.now().strftime('%H:%M:%S')} (10 min depois - execução programada)")
    print(f"  Previous temp (helper): {previous_temp}°C")
    print(f"  Current temp (sensor):  {current_temp}°C")
    temp_change = abs(previous_temp - current_temp)
    print(f"  Mudança de temperatura: {temp_change}°C")
    print(f"  Detecção triggered? {'SIM' if temp_change >= threshold else 'NÃO'}")
    print(f"  Helper updated to: {current_temp}°C")
    print()

def test_scenarios():
    """
    Testa diferentes cenários de abertura de janela
    """
    print("TESTE DE CENÁRIOS DE DETECÇÃO DE JANELA")
    print("=" * 70)
    print()
    
    # Cenário 1: Inverno - temperatura cai quando janela abre
    print("CENÁRIO 1: INVERNO (Temperatura externa menor)")
    simulate_window_detection(
        initial_temp=22.5,
        final_temp=20.0,  # Cai 2.5°C
        threshold=2.0,
        detection_time_minutes=15
    )
    
    print("\n" + "=" * 70 + "\n")
    
    # Cenário 2: Verão - temperatura sobe quando janela abre
    print("CENÁRIO 2: VERÃO (Temperatura externa maior)")
    simulate_window_detection(
        initial_temp=24.0,
        final_temp=26.5,  # Sobe 2.5°C
        threshold=2.0,
        detection_time_minutes=15
    )
    
    print("\n" + "=" * 70 + "\n")
    
    # Cenário 3: Mudança pequena - não deve detectar
    print("CENÁRIO 3: MUDANÇA PEQUENA (Não deve detectar)")
    simulate_window_detection(
        initial_temp=22.0,
        final_temp=23.0,  # Sobe apenas 1°C
        threshold=2.0,
        detection_time_minutes=15
    )

def check_automation_logic():
    """
    Verifica a lógica específica da automação
    """
    print("\n" + "=" * 70)
    print("ANÁLISE DA LÓGICA DA AUTOMAÇÃO")
    print("=" * 70)
    print()
    
    print("TRIGGERS da automação:")
    print("1. Time pattern: a cada 10 minutos (0, 10, 20, 30, 40, 50)")
    print("2. State change: sensor de temperatura interna")
    print("3. State change: sensor de temperatura externa")
    print()
    
    print("FLUXO DE EXECUÇÃO:")
    print("1. Automation é triggered")
    print("2. Lê temperatura atual do sensor")
    print("3. Lê temperatura anterior do helper")
    print("4. Calcula diferença")
    print("5. Se diferença >= threshold: DETECTA janela aberta")
    print("6. Executa ação (pause HVAC ou controle normal)")
    print("7. SEMPRE atualiza helper com temperatura atual")
    print()
    
    print("PROBLEMA POTENCIAL:")
    print("- Se o sensor muda muito rapidamente, múltiplas execuções")
    print("  podem acontecer antes do helper ser atualizado")
    print("- Timing entre state change trigger e update do helper")
    print("- Helper pode ser atualizado em execução anterior")
    print()
    
    print("SOLUÇÃO RECOMENDADA:")
    print("1. Verificar se o helper está sendo criado corretamente")
    print("2. Verificar se o sensor está reportando mudanças") 
    print("3. Adicionar delay entre leitura e comparação")
    print("4. Verificar logs da automação para ver valores reais")

if __name__ == "__main__":
    test_scenarios()
    check_automation_logic()
