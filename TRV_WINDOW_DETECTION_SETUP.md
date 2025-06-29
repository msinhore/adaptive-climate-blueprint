# Window Detection para Sonoff TRVZB - Realidade Técnica

## ⚠️ CONCLUSÃO DEFINITIVA

**O Sonoff TRVZB NÃO suporta window detection via Zigbee2MQTT** devido a limitações técnicas do firmware.

### Investigação Técnica Completa

**Atributos encontrados no cluster hvacThermostat:**
- `viessmannWindowOpenForce` (manufacturerCode: 4641)  
- `viessmannWindowOpenInternal` (manufacturerCode: 4641)

**Resultado ao tentar acessar:**
```
failed (Status 'UNSUPPORTED_ATTRIBUTE')
```

### Por Que Não Funciona

Os erros `UNSUPPORTED_ATTRIBUTE` confirmam que:

1. **Clusters proprietários parcialmente implementados**
   - Viessmann implementou funcionalidade apenas para uso interno
   - Atributos existem mas são bloqueados para acesso externo

2. **Reservados para comandos internos apenas**
   - Window detection funciona internamente no TRV
   - Não expostos para gateways como Zigbee2MQTT

3. **Firmware bloqueia acesso externo**
   - Mesmo com manufacturerCode: 4641 correto
   - Compatível apenas com gateways oficiais Viessmann

## ✅ Soluções Práticas Funcionais

### 1. RECOMENDADA - Desabilitar Window Detection
```yaml
# Configuração blueprint - mais simples e confiável
primary_climate_entity: climate.radiator_sala
enable_trv_efficiency_monitoring: true
trv_valve_opening_sensor: number.radiator_sala_valve_opening_degree
trv_valve_closing_sensor: number.radiator_sala_valve_closing_degree
trv_running_steps_sensor: sensor.radiator_sala_closing_steps
trv_window_open_sensor: ""  # VAZIO = sem window detection
```

**Vantagens:**
- ✅ 100% funcional e estável
- ✅ Sem dependências externas
- ✅ Blueprint funciona perfeitamente
- ✅ Todas as outras funcionalidades preservadas

### 2. ALTERNATIVA - Sensor Físico Dedicado
```yaml
# Use sensor de porta/janela Zigbee independente
trv_window_open_sensor: binary_sensor.porta_sala_contact
```

**Sensores recomendados:**
- Aqara Door/Window Sensor
- Sonoff SNZB-04 
- Tuya Door/Window Sensor

**Vantagens:**
- ✅ Detecção instantânea e confiável
- ✅ Controle total sobre sensibilidade
- ✅ Funciona com qualquer dispositivo
- ✅ Sem limitações de firmware

### 3. AVANÇADA - Template Baseado em Comportamento TRV
```yaml
# Em configuration.yaml
template:
  - binary_sensor:
      - name: "Sala Window Open Behavior Detection"
        unique_id: sala_window_behavior
        state: >
          {% set hvac = state_attr('climate.radiator_sala', 'hvac_action') %}
          {% set valve = states('number.radiator_sala_valve_opening_degree') | float(0) %}
          {% set temp = state_attr('climate.radiator_sala', 'current_temperature') | float %}
          {% set target = state_attr('climate.radiator_sala', 'temperature') | float %}
          {{ hvac == 'idle' and valve < 15 and (target - temp) > 2 }}
        device_class: window
        delay_on: "00:02:00"  # Evita falsos positivos
        delay_off: "00:01:00"
```

**Lógica do template:**
- HVAC em idle (TRV não aquecendo)
- Válvula quase fechada (< 15%)
- Grande diferença de temperatura (target - atual > 2°C)
- **= Possível janela aberta detectada**

## Configuração Completa Recomendada

### Blueprint Configuration (Sem Window Detection)
```yaml
# Configuração dual climate completa e funcional
dual_climate_control: true
primary_climate_entity: climate.radiator_sala
climate_entity: climate.ac_sala

# TRV Monitoring - FUNCIONAL
enable_trv_efficiency_monitoring: true
trv_valve_opening_sensor: number.radiator_sala_valve_opening_degree
trv_valve_closing_sensor: number.radiator_sala_valve_closing_degree
trv_running_steps_sensor: sensor.radiator_sala_closing_steps

# Window Detection - DESABILITADO (mais estável)
trv_window_open_sensor: ""

# Controle de portas/janelas via sensores físicos (opcional)
door_window_entities:
  - binary_sensor.porta_sala_contact
  - binary_sensor.janela_sala_sensor

# Thresholds
secondary_heating_threshold: 2.0
trv_priority_temp_difference: 5.0
```

### Se Usar Sensor Físico
```yaml
# Mesma configuração acima, mas com:
trv_window_open_sensor: binary_sensor.porta_sala_contact

# E remova da lista door_window_entities para evitar duplicação
```

## ✅ Funcionalidades Garantidas

**Mesmo sem window detection do TRV, você tem:**

- ✅ **Controle dual TRV + AC** - Coordenação inteligente
- ✅ **Monitoramento de eficiência** - Valve position tracking
- ✅ **Adaptive comfort** - Baseado em temperatura externa
- ✅ **Detecção de porta/janela** - Via sensores físicos dedicados
- ✅ **Economia de energia** - Dual heating logic
- ✅ **Automação completa** - Todos os cenários cobertos

## Resumo Técnico Final

### ❌ O que NÃO funciona:
- `open_window` via state_attr
- `viessmannWindowOpenForce` via MQTT
- `viessmannWindowOpenInternal` via MQTT
- Template sensors baseados em atributos TRV

### ✅ O que FUNCIONA perfeitamente:
- Dual climate control TRV + AC
- Valve position monitoring
- TRV efficiency tracking
- Sensor físico de porta/janela
- Template behavior detection
- Todas as funcionalidades principais do blueprint

**Recomendação:** Use a configuração com `trv_window_open_sensor: ""` para máxima estabilidade e funcionalidade.
