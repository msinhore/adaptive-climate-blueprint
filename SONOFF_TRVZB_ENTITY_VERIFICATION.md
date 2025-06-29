# Guia de Verificação de Entidades Sonoff TRVZB

## Como Verificar Quais Entidades Você Tem

### 1. Vá em Developer Tools > States

No Home Assistant, navegue para **Developer Tools → States** e procure por entidades que começam com seu TRV:

### 2. Entidades Comuns do Sonoff TRVZB

#### ✅ Entidades que SEMPRE existem (conforme doc oficial Zigbee2MQTT):
```
climate.radiator_sala                           # Controle principal (thermostat)
    ↳ state_attr('climate.radiator_sala', 'open_window')  # Propriedade window detection
number.radiator_sala_valve_opening_degree       # Posição da válvula (0-100%)
number.radiator_sala_valve_closing_degree       # Fechamento da válvula (0-100%)
sensor.radiator_sala_closing_steps              # Passos do motor para fechar
sensor.radiator_sala_idle_steps                 # Passos de calibração
sensor.radiator_sala_battery                    # Nível da bateria
number.radiator_sala_frost_protection_temperature # Proteção anti-congelamento
number.radiator_sala_external_temperature_input # Entrada temp externa
number.radiator_sala_temperature_accuracy       # Precisão do controle (-0.2 a -1°C)
```

#### ❌ Entidades que NÃO existem (confusão de documentação):
```
binary_sensor.radiator_sala_open_window        # NÃO EXISTE - open_window é propriedade, não entidade
switch.radiator_sala_open_window               # NÃO EXISTE - era erro na documentação
sensor.radiator_sala_open_window              # NÃO EXISTE - o correto é state_attr
```

### 3. Para o Blueprint Adaptive Climate

#### Configuração OFICIAL (baseada na doc Zigbee2MQTT):
```yaml
# TRV completo - configuração oficial
primary_climate_entity: climate.radiator_sala
enable_trv_efficiency_monitoring: true
trv_valve_opening_sensor: number.radiator_sala_valve_opening_degree
trv_valve_closing_sensor: number.radiator_sala_valve_closing_degree
trv_running_steps_sensor: sensor.radiator_sala_closing_steps

# Window detection - MÉTODO 1: Criar template sensor (recomendado)
# Primeiro, crie em configuration.yaml:
template:
  - binary_sensor:
      - name: "Sala Window Open TRV"
        unique_id: sala_window_open_trv
        state: "{{ state_attr('climate.radiator_sala', 'open_window') == true }}"
        device_class: window

# Depois use no blueprint:
trv_window_open_sensor: binary_sensor.sala_window_open_trv
```

#### Método Alternativo (sensor físico):
```yaml
# Se você tem um sensor de janela/porta dedicado, use esse
trv_window_open_sensor: binary_sensor.porta_sala_contact
trv_window_open_sensor: sensor.radiator_sala_open_window
```

### 4. Como Testar se a Detecção de Janela Funciona

#### Teste 1: Template no Developer Tools
```yaml
# Cole no Developer Tools > Templates:
TRV Switch Window: {{ states('switch.radiator_sala_open_window') }}
HVAC Action: {{ state_attr('climate.radiator_sala', 'hvac_action') }}

{% if states('binary_sensor.radiator_sala_window_detection') != 'unavailable' %}
Window Sensor: {{ states('binary_sensor.radiator_sala_window_detection') }}
{% else %}
Window Sensor: NÃO EXISTE
{% endif %}
```

#### Teste 2: Monitorar durante janela aberta
1. Abra uma janela no ambiente
2. Monitore por 5-10 minutos
3. Veja se `hvac_action` muda de 'heating' para 'idle'
4. Se mudar, a detecção está funcionando

### 5. Solução para Problema de Cooling

Para resolver o problema do AC não ligar:

```yaml
# Configure temporariamente:
natural_ventilation_enable: false

# E monitore se o AC liga com estas temperaturas:
# Externa: 33.4°C, Interna: 27.5°C, Max conforto: 27°C
```

### 6. Diagnóstico Completo

Execute no Developer Tools > Templates:

```yaml
=== ENTIDADES TRV VERIFICAÇÃO ===
Climate: {{ states('climate.radiator_sala') }}
Valve Opening: {{ states('number.radiator_sala_valve_opening_degree') }}%
Window Switch: {{ states('switch.radiator_sala_open_window') }}

{% if states('binary_sensor.radiator_sala_window_detection') != 'unavailable' %}
Window Binary Sensor: {{ states('binary_sensor.radiator_sala_window_detection') }}
{% endif %}

{% if states('sensor.radiator_sala_open_window') != 'unavailable' %}
Window Sensor: {{ states('sensor.radiator_sala_open_window') }}
{% endif %}

=== COOLING DIAGNOSIS ===
Temp Externa: {{ states('sensor.seu_temp_externa') }}°C
Temp Interna: {{ states('sensor.seu_temp_interna') }}°C
AC Estado: {{ states('climate.seu_ac') }}
AC Modo: {{ state_attr('climate.seu_ac', 'hvac_mode') }}
```

### Conclusão

- **A maioria dos setups Sonoff TRVZB**: Use `trv_window_open_sensor: ""`
- **Se tiver sensor específico**: Configure com a entidade que encontrou
- **Para o problema de cooling**: Desabilite `natural_ventilation_enable: false` temporariamente
