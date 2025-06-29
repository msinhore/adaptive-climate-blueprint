# Guia de Verificação de Entidades Sonoff TRVZB

## Como Verificar Quais Entidades Você Tem

### 1. Vá em Developer Tools > States

No Home Assistant, navegue para **Developer Tools → States** e procure por entidades que começam com seu TRV:

### 2. Entidades Comuns do Sonoff TRVZB

#### ✅ Entidades que SEMPRE existem:
```
climate.radiator_sala                          # Controle principal
number.radiator_sala_valve_opening_degree      # Posição da válvula
number.radiator_sala_valve_closing_degree      # Fechamento da válvula
switch.radiator_sala_open_window               # Controle detecção janela
sensor.radiator_sala_closing_steps             # Atividade do motor
sensor.radiator_sala_battery                   # Nível da bateria
```

#### ❓ Entidades que PODEM existir (dependem da configuração):
```
binary_sensor.radiator_sala_window_detection   # Estado real da detecção
sensor.radiator_sala_open_window              # Outro formato do sensor
sensor.radiator_sala_window_state             # Variação do nome
```

### 3. Para o Blueprint Adaptive Climate

#### Configuração SEGURA (sempre funciona):
```yaml
# TRV básico - sempre funciona
primary_climate_entity: climate.radiator_sala
enable_trv_efficiency_monitoring: true
trv_valve_opening_sensor: number.radiator_sala_valve_opening_degree
trv_valve_closing_sensor: number.radiator_sala_valve_closing_degree
trv_running_steps_sensor: sensor.radiator_sala_closing_steps

# Window detection - deixe vazio se não tiver sensor específico
trv_window_open_sensor: ""
```

#### Se você ENCONTRAR um sensor de janela:
```yaml
# Use o sensor específico que encontrou
trv_window_open_sensor: binary_sensor.radiator_sala_window_detection
# OU
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
