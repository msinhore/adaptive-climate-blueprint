# Template Inteligente para Window Detection - Sonoff TRVZB

## Problema Identificado

O Sonoff TRVZB (Viessmann) TEM window detection interno (`viessmannWindowOpenForce`, `viessmannWindowOpenInternal`), mas estes atributos retornam `UNSUPPORTED_ATTRIBUTE` no Zigbee2MQTT.

## Solução: Template Baseado em Comportamento

### Método 1: Detecção via HVAC Action + Temperatura

O TRV internamente para de aquecer quando detecta janela aberta. Podemos detectar isso:

```yaml
# configuration.yaml
template:
  - binary_sensor:
      - name: "Sala Window Open Smart Detection"
        unique_id: sala_window_smart_detection
        state: >
          {% set hvac_action = state_attr('climate.radiator_sala', 'hvac_action') %}
          {% set current_temp = state_attr('climate.radiator_sala', 'current_temperature') | float(20) %}
          {% set target_temp = state_attr('climate.radiator_sala', 'temperature') | float(21) %}
          {% set temp_diff = target_temp - current_temp %}
          
          {# TRV para de aquecer (idle) mesmo com diferença de temperatura significativa #}
          {{ hvac_action == 'idle' and temp_diff > 1.5 }}
        device_class: window
        icon: >
          {% set hvac_action = state_attr('climate.radiator_sala', 'hvac_action') %}
          {% set current_temp = state_attr('climate.radiator_sala', 'current_temperature') | float(20) %}
          {% set target_temp = state_attr('climate.radiator_sala', 'temperature') | float(21) %}
          {% set temp_diff = target_temp - current_temp %}
          {% if hvac_action == 'idle' and temp_diff > 1.5 %}
            mdi:window-open
          {% else %}
            mdi:window-closed
          {% endif %}
        attributes:
          hvac_action: "{{ state_attr('climate.radiator_sala', 'hvac_action') }}"
          temperature_difference: "{{ (state_attr('climate.radiator_sala', 'temperature') | float(21)) - (state_attr('climate.radiator_sala', 'current_temperature') | float(20)) }}"
          detection_reason: >
            {% set hvac_action = state_attr('climate.radiator_sala', 'hvac_action') %}
            {% set temp_diff = (state_attr('climate.radiator_sala', 'temperature') | float(21)) - (state_attr('climate.radiator_sala', 'current_temperature') | float(20)) %}
            {% if hvac_action == 'idle' and temp_diff > 1.5 %}
              TRV stopped heating despite temperature gap
            {% else %}
              Normal operation
            {% endif %}
```

### Método 2: Detecção via Valve Position

Se a válvula fecha rapidamente ou permanece fechada com gap de temperatura:

```yaml
template:
  - binary_sensor:
      - name: "Sala Window Open Valve Detection"
        unique_id: sala_window_valve_detection
        state: >
          {% set valve_opening = states('number.radiator_sala_valve_opening_degree') | float(0) %}
          {% set current_temp = state_attr('climate.radiator_sala', 'current_temperature') | float(20) %}
          {% set target_temp = state_attr('climate.radiator_sala', 'temperature') | float(21) %}
          {% set temp_diff = target_temp - current_temp %}
          
          {# Válvula fechada (< 10%) mas temperatura ainda baixa #}
          {{ valve_opening < 10 and temp_diff > 2.0 }}
        device_class: window
        attributes:
          valve_opening: "{{ states('number.radiator_sala_valve_opening_degree') }}"
          temperature_difference: "{{ (state_attr('climate.radiator_sala', 'temperature') | float(21)) - (state_attr('climate.radiator_sala', 'current_temperature') | float(20)) }}"
```

### Método 3: Combinado (Mais Robusto)

```yaml
template:
  - binary_sensor:
      - name: "Sala Window Open Combined Detection"
        unique_id: sala_window_combined_detection
        state: >
          {% set hvac_action = state_attr('climate.radiator_sala', 'hvac_action') %}
          {% set valve_opening = states('number.radiator_sala_valve_opening_degree') | float(0) %}
          {% set current_temp = state_attr('climate.radiator_sala', 'current_temperature') | float(20) %}
          {% set target_temp = state_attr('climate.radiator_sala', 'temperature') | float(21) %}
          {% set temp_diff = target_temp - current_temp %}
          
          {# Condições para detectar janela aberta: #}
          {# 1. TRV parou de aquecer OU válvula fechou #}
          {# 2. Ainda há diferença de temperatura significativa #}
          {% set stopped_heating = hvac_action == 'idle' or valve_opening < 15 %}
          {% set needs_heating = temp_diff > 1.5 %}
          
          {{ stopped_heating and needs_heating }}
        device_class: window
        delay_off: "00:02:00"  # Evita oscilações
        delay_on: "00:01:00"   # Confirma detecção
```

## Como Usar no Blueprint

### Configuração Recomendada

```yaml
# Blueprint configuration
primary_climate_entity: climate.radiator_sala
enable_trv_efficiency_monitoring: true
trv_valve_opening_sensor: number.radiator_sala_valve_opening_degree
trv_valve_closing_sensor: number.radiator_sala_valve_closing_degree
trv_running_steps_sensor: sensor.radiator_sala_closing_steps

# Window detection via template inteligente
trv_window_open_sensor: binary_sensor.sala_window_combined_detection
```

## Testes e Validação

### Teste Manual

1. **Configure um dos templates** acima
2. **Reinicie o Home Assistant**
3. **Abra uma janela** no ambiente com TRV
4. **Monitore o sensor** no Developer Tools → States
5. **Aguarde 2-5 minutos** para o TRV reagir

### Debug Dashboard

```yaml
type: entities
entities:
  - entity: binary_sensor.sala_window_combined_detection
    name: "Window Detection"
  - entity: climate.radiator_sala
    attribute: hvac_action
    name: "HVAC Action"
  - entity: number.radiator_sala_valve_opening_degree
    name: "Valve Opening"
  - entity: climate.radiator_sala
    attribute: current_temperature
    name: "Current Temp"
  - entity: climate.radiator_sala
    attribute: temperature
    name: "Target Temp"
```

## Vantagens dos Templates

### ✅ Baseado em Comportamento Real
- Detecta quando TRV para de aquecer inadequadamente
- Não depende de atributos não suportados

### ✅ Configurável
- Pode ajustar thresholds (temp_diff, valve_opening)
- Delays para evitar false positives

### ✅ Transparente
- Mostra nos atributos por que detectou janela aberta
- Facilita debug e ajustes

## Alternativa Simples

Se os templates parecerem complexos:

```yaml
# Opção mais simples - desabilitar window detection
trv_window_open_sensor: ""

# Ou usar sensor físico dedicado
trv_window_open_sensor: binary_sensor.porta_sala_contact
```

## Conclusão

Mesmo que os atributos Viessmann não sejam suportados pelo Zigbee2MQTT, podemos criar detecção inteligente baseada no **comportamento observável** do TRV. O template combinado é a melhor opção para aproveitar a detecção interna sem depender de atributos não suportados.
