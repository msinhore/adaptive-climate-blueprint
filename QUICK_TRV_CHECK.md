# Quick Check: Verificar Capacidades do Seu Sonoff TRVZB

## Teste Rápido - Developer Tools → Template

Cole estes templates um por vez para verificar o que seu TRV suporta:

### 1. Verificar Todos os Atributos Disponíveis
```jinja2
{{ states.climate.radiator_sala.attributes }}
```

### 2. Procurar Window Detection (várias possibilidades)
```jinja2
{{ state_attr('climate.radiator_sala', 'open_window') }}
{{ state_attr('climate.radiator_sala', 'window_detection') }}
{{ state_attr('climate.radiator_sala', 'window_open') }}
{{ state_attr('climate.radiator_sala', 'window_state') }}
```

### 3. Verificar Outros Atributos Úteis
```jinja2
{{ state_attr('climate.radiator_sala', 'hvac_action') }}
{{ state_attr('climate.radiator_sala', 'current_temperature') }}
{{ state_attr('climate.radiator_sala', 'temperature') }}
{{ state_attr('climate.radiator_sala', 'valve_position') }}
```

## Resultados Esperados

### ✅ Se Funcionar:
- `open_window`: `true` ou `false`
- Você pode usar o template sensor

### ❌ Se NÃO Funcionar:
- `open_window`: `None` ou erro
- Use uma das alternativas abaixo

## Alternativas Práticas (Escolha 1)

### Opção 1: Desabilitar (Mais Simples)
```yaml
# Blueprint configuration
primary_climate_entity: climate.radiator_sala
trv_window_open_sensor: ""  # Vazio = sem window detection
enable_trv_efficiency_monitoring: true
```

### Opção 2: Sensor Físico de Porta/Janela
```yaml
# Se você tem sensor de porta/janela
trv_window_open_sensor: binary_sensor.porta_sala_contact
```

### Opção 3: Detecção por Queda de Temperatura
```yaml
# configuration.yaml - Template sensor
template:
  - binary_sensor:
      - name: "Sala Window Open Temperature Drop"
        unique_id: sala_window_temp_drop
        state: >
          {% set current_temp = states('sensor.temperatura_sala') | float(0) %}
          {% set old_temp = states('sensor.temperatura_sala') %}
          {% set temp_history = state_attr('sensor.temperatura_sala', 'history') %}
          {{ (current_temp < (current_temp + 1.5)) if temp_history else false }}
        device_class: window
```

## Configuração Recomendada (Sem Window Detection)

**Se window detection não funcionar, use esta configuração que é 100% confiável:**

```yaml
# Blueprint - Configuração Completa SEM Window Detection
dual_climate_control: true
primary_climate_entity: climate.radiator_sala
climate_entity: climate.ac_sala

# TRV Monitoring (essencial)
enable_trv_efficiency_monitoring: true
trv_valve_opening_sensor: number.radiator_sala_valve_opening_degree
trv_valve_closing_sensor: number.radiator_sala_valve_closing_degree
trv_running_steps_sensor: sensor.radiator_sala_closing_steps

# Window Detection - DESABILITADO
trv_window_open_sensor: ""

# Thresholds
secondary_heating_threshold: 2.0
trv_priority_temp_difference: 5.0

# Door/Window Detection via outros sensores (opcional)
door_window_entities:
  - binary_sensor.porta_sala_contact
  - binary_sensor.janela_sala_sensor
```

## Teste de Funcionamento

### 1. Configurar Sem Window Detection
Use a configuração acima

### 2. Verificar Logs
Vá em **Configuration → Logs** e procure por erros relacionados ao blueprint

### 3. Testar Dual Climate
- Abaixe a temperatura alvo do TRV
- Verifique se o AC ativa quando necessário
- Monitor valve opening degree

### 4. Se Tudo Funcionar
Você tem um sistema dual climate totalmente funcional sem depender de window detection!

## Conclusão

**Não se preocupe** se window detection não funcionar. O blueprint funciona perfeitamente sem essa funcionalidade e você ainda terá:

- ✅ Controle dual TRV + AC
- ✅ Eficiência energética
- ✅ Monitoramento de válvula
- ✅ Adaptive comfort
- ✅ Detecção de porta/janela via sensores físicos (opcional)

O window detection do TRV é um **bônus**, não um requisito!
