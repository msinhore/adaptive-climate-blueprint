# Configuração Window Detection para Sonoff TRVZB

## Problema Identificado

Baseado na **documentação oficial do Zigbee2MQTT**, o Sonoff TRVZB não cria uma entidade `binary_sensor### Debug Issues - Opções Práticas

**Se `open_window` não existir no seu TRV:**

1. **SOLUÇÃO MAIS SIMPLES - Desabilitar:**
   ```yaml
   # No blueprint, deixe vazio - funciona perfeitamente
   trv_window_open_sensor: ""
   ```

2. **SOLUÇÃO ALTERNATIVA - Sensor Físico:**
   ```yaml
   # Use um sensor de porta/janela dedicado
   trv_window_open_sensor: binary_sensor.porta_sala_contact
   ```

3. **SOLUÇÃO AVANÇADA - Template de Temperatura:**
   Crie detecção baseada em queda rápida de temperaturaopen_window` separada. Em vez disso, publica `open_window` como uma **propriedade do estado** do `climate` entity.

## Solução: Template Sensor

### 1. Criar Template Sensor (Recomendado)

Adicione no seu `configuration.yaml`:

```yaml
template:
  - binary_sensor:
      - name: "Sala Window Open TRV"
        unique_id: sala_window_open_trv
        state: "{{ state_attr('climate.radiator_sala', 'open_window') == true }}"
        device_class: window
        icon: >
          {% if state_attr('climate.radiator_sala', 'open_window') == true %}
            mdi:window-open
          {% else %}
            mdi:window-closed
          {% endif %}
```

### 2. Reiniciar Home Assistant

Após adicionar o template, reinicie o Home Assistant para criar a nova entidade.

### 3. Verificar a Nova Entidade

Vá em **Developer Tools → States** e confirme que existe:
- `binary_sensor.sala_window_open_trv`

### 4. Configurar no Blueprint

Use a nova entidade no blueprint:

```yaml
# Configuração do blueprint
primary_climate_entity: climate.radiator_sala
enable_trv_efficiency_monitoring: true
trv_valve_opening_sensor: number.radiator_sala_valve_opening_degree
trv_valve_closing_sensor: number.radiator_sala_valve_closing_degree
trv_running_steps_sensor: sensor.radiator_sala_closing_steps
trv_window_open_sensor: binary_sensor.sala_window_open_trv
```

## Alternativa: Sensor Físico

Se você tem um sensor de janela/porta dedicado, pode usar esse em vez do template:

```yaml
# Exemplo com sensor físico
trv_window_open_sensor: binary_sensor.porta_sala_contact
# ou
trv_window_open_sensor: binary_sensor.janela_sala_sensor
```

## Como Funciona o Window Detection do TRV

### Método de Detecção
- **Threshold**: Queda de temperatura > 1.5°C
- **Tempo**: Em 4.5 minutos
- **Automático**: O TRV detecta internamente, sem configuração adicional

### Estados
- `true`: Janela detectada como aberta (temperatura caiu rapidamente)
- `false`: Janela fechada (temperatura estável)

### Uso no Blueprint
Quando `open_window == true`:
1. O blueprint pausa o controle automático
2. O TRV para de aquecer
3. Evita desperdício de energia

## Verificação e Debug

### Testar Template Sensor

No **Developer Tools → Template**, teste:

```jinja2
{{ state_attr('climate.radiator_sala', 'open_window') }}
```

Resultado esperado: `true` ou `false` (ou `None` se não suportado)

### Monitorar em Tempo Real

Crie um card no dashboard:

```yaml
type: entity
entity: binary_sensor.sala_window_open_trv
name: "Window Detection (TRV)"
icon: mdi:window-open-variant
```

## ⚠️ Troubleshooting: Propriedade open_window Não Encontrada

### Se Você Não Encontrar `open_window`

Isso é **comum** e pode ter várias causas:

#### 1. Verificar Todas as Propriedades Disponíveis

No **Developer Tools → Template**, teste:

```jinja2
{{ state_attr('climate.radiator_sala', '') }}
```

Ou liste todos os atributos:

```jinja2
{% for attr in state_attr('climate.radiator_sala', '') %}
  {{ attr }}: {{ state_attr('climate.radiator_sala', attr) }}
{% endfor %}
```

#### 2. Verificar no Zigbee2MQTT

Se você usar Zigbee2MQTT, vá em:
- **Zigbee2MQTT → Devices → Seu TRV**
- Procure por configurações como:
  - `window_detection`
  - `open_window_temperature`
  - `window_open`

#### 3. Habilitar Window Detection

Algumas opções para habilitar:

**Via MQTT (se usando Zigbee2MQTT):**
```bash
# Publicar comando para habilitar
mosquitto_pub -h localhost -t "zigbee2mqtt/radiator_sala/set" -m '{"window_detection": "ON"}'
```

**Via Home Assistant Developer Tools → Services:**
```yaml
service: mqtt.publish
data:
  topic: "zigbee2mqtt/radiator_sala/set"
  payload: '{"window_detection": "ON"}'
```

#### 4. Alternativas Práticas

Se o TRV não suporta window detection automático, use estas alternativas:

**Opção A - Sensor de Janela/Porta Físico:**
```yaml
# Use um sensor Zigbee dedicado
trv_window_open_sensor: binary_sensor.porta_sala_contact
```

**Opção B - Template Baseado em Temperatura:**
```yaml
template:
  - binary_sensor:
      - name: "Sala Window Open Detection"
        unique_id: sala_window_detection_temp
        state: >
          {% set temp_now = states('sensor.temperatura_sala') | float %}
          {% set temp_5min = state_attr('sensor.temperatura_sala', 'temperature_5min_ago') | float %}
          {{ (temp_now - temp_5min) < -1.5 }}
        device_class: window
```

**Opção C - Desabilitar Window Detection:**
```yaml
# No blueprint, deixe vazio
trv_window_open_sensor: ""
# O blueprint funciona normalmente sem window detection
```

### Verificação e Debug

Se o template não funcionar:

1. **Verifique se o TRV suporta window detection**:
   ```jinja2
   {{ state_attr('climate.radiator_sala', 'open_window') }}
   ```
   Se retornar `None`, o TRV pode não ter essa funcionalidade ativada.

2. **Use sensor físico alternativo**:
   Configure um sensor de janela/porta dedicado como backup.

3. **Desative window detection**:
   Deixe `trv_window_open_sensor` vazio no blueprint se não tiver sensor confiável.

## Exemplo Completo

### configuration.yaml
```yaml
template:
  - binary_sensor:
      - name: "Sala Window Open TRV"
        unique_id: sala_window_open_trv
        state: "{{ state_attr('climate.radiator_sala', 'open_window') == true }}"
        device_class: window
        icon: >
          {% if state_attr('climate.radiator_sala', 'open_window') == true %}
            mdi:window-open
          {% else %}
            mdi:window-closed
          {% endif %}
      
      - name: "Quarto Window Open TRV"
        unique_id: quarto_window_open_trv
        state: "{{ state_attr('climate.radiator_quarto', 'open_window') == true }}"
        device_class: window
```

### Blueprint Configuration
```yaml
# Sala
primary_climate_entity: climate.radiator_sala
trv_window_open_sensor: binary_sensor.sala_window_open_trv
trv_valve_opening_sensor: number.radiator_sala_valve_opening_degree
trv_valve_closing_sensor: number.radiator_sala_valve_closing_degree
trv_running_steps_sensor: sensor.radiator_sala_closing_steps

# AC de apoio
secondary_climate_entity: climate.ac_sala
enable_ac_dual_mode: true
ac_heat_mode: "heat"
ac_cool_mode: "cool"
```

Essa configuração garante que o window detection funcione corretamente com base na documentação oficial do Zigbee2MQTT.
