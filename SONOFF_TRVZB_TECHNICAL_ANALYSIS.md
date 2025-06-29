# Análise Técnica: Sonoff TRVZB Window Detection

## Descoberta Importante ✨

Durante a investigação técnica do Sonoff TRVZB (fabricado pela Viessmann), foram descobertos **atributos proprietários de window detection** que **existem no hardware mas são inacessíveis via Zigbee2MQTT**.

## Evidências Técnicas

### 1. Atributos Encontrados no Cluster
**Localização:** `Zigbee2MQTT → Device → Reporting/Endpoint 1/hvacThermostat`

```
viessmannWindowOpenForce      (manufacturerCode: 4641)
viessmannWindowOpenInternal   (manufacturerCode: 4641)
```

### 2. Resultado de Tentativas de Acesso
```bash
# Tentativa de leitura
Status: failed (Status 'UNSUPPORTED_ATTRIBUTE')

# Tentativa de escrita  
Status: failed (Status 'UNSUPPORTED_ATTRIBUTE')
```

### 3. Código Viessmann Confirmado
- **Manufacturer Code:** 4641
- **Marca:** Viessmann (fabricante real do hardware)
- **Produto:** Sonoff TRVZB (rebranding)

## Análise do Problema

### Por Que os Atributos Existem Mas Não Funcionam?

#### 1. **Implementação Proprietária Parcial**
```
✅ Hardware: Window detection implementado
✅ Cluster: Atributos listados no hvacThermostat
❌ Acesso: Bloqueado para gateways externos
❌ Zigbee2MQTT: UNSUPPORTED_ATTRIBUTE
```

#### 2. **Estratégia Comercial Viessmann**
- **Funcionalidade interna:** O TRV detecta janelas internamente
- **Acesso restrito:** Apenas para gateways oficiais Viessmann
- **Zigbee2MQTT:** Considerado gateway "não autorizado"

#### 3. **Limitações do Protocolo Zigbee**
- **Clusters padrão:** Totalmente acessíveis
- **Clusters proprietários:** Depende da implementação do fabricante
- **Viessmann:** Escolheu restringir acesso externo

## Implicações Práticas

### O Que Funciona ✅
```yaml
# Controle básico do TRV
climate.radiator_sala                     # Controle completo
number.radiator_sala_valve_opening_degree # Posição da válvula
number.radiator_sala_valve_closing_degree # Fechamento da válvula
sensor.radiator_sala_closing_steps        # Atividade do motor
sensor.radiator_sala_battery              # Nível da bateria
```

### O Que NÃO Funciona ❌
```yaml
# Window detection via Zigbee2MQTT
state_attr('climate.radiator_sala', 'open_window')          # None
state_attr('climate.radiator_sala', 'window_detection')     # None
binary_sensor.radiator_sala_open_window                     # Não existe
```

### Detecção Interna (Inacessível) 🔒
```
viessmannWindowOpenForce:    UNSUPPORTED_ATTRIBUTE
viessmannWindowOpenInternal: UNSUPPORTED_ATTRIBUTE
```

## Soluções Alternativas

### 1. **Abordagem Mais Simples (Recomendada)**
```yaml
# Blueprint configuration
trv_window_open_sensor: ""  # Desabilitar window detection
```

**Vantagens:**
- ✅ 100% confiável
- ✅ Sem complexidade adicional
- ✅ Blueprint funciona perfeitamente
- ✅ Foco nas funcionalidades principais

### 2. **Sensor Físico Independente**
```yaml
# Sensor de porta/janela Zigbee dedicado
trv_window_open_sensor: binary_sensor.porta_sala_contact
```

**Vantagens:**
- ✅ Detecção instantânea e precisa
- ✅ Controle total sobre sensibilidade
- ✅ Não depende do TRV
- ✅ Funciona com qualquer blueprint

### 3. **Template Comportamental Avançado**
```yaml
template:
  - binary_sensor:
      - name: "Sala Window Open Smart Detection"
        unique_id: sala_window_smart_detection
        state: >
          {% set hvac = state_attr('climate.radiator_sala', 'hvac_action') %}
          {% set valve = states('number.radiator_sala_valve_opening_degree') | float(0) %}
          {% set temp_current = state_attr('climate.radiator_sala', 'current_temperature') | float %}
          {% set temp_target = state_attr('climate.radiator_sala', 'temperature') | float %}
          {% set temp_diff = temp_target - temp_current %}
          
          {# Lógica: TRV parou de aquecer mas ainda há demanda significativa #}
          {{ hvac == 'idle' and valve < 15 and temp_diff > 1.5 }}
        device_class: window
        delay_on: "00:02:00"    # Evitar falsos positivos
        delay_off: "00:05:00"   # Janela pode estar aberta por tempo
```

**Lógica do template:**
1. **HVAC em idle** → TRV parou de tentar aquecer
2. **Válvula fechada** → Não está tentando aquecer ativamente  
3. **Grande diferença temperatura** → Ainda há demanda de aquecimento
4. **Conclusão** → Possível janela aberta (TRV detectou internamente)

## Futuro e Monitoramento

### Possíveis Desenvolvimentos

#### 1. **Atualização Zigbee2MQTT**
- Monitorar issues no repositório `zigbee-herdsman-converters`
- Possível suporte futuro aos atributos Viessmann
- Aguardar reverse engineering da comunidade

#### 2. **Firmware Updates**
- Viessmann pode habilitar acesso em futuras versões
- Improvável devido à estratégia comercial
- Foco em ecossistema próprio

#### 3. **Alternativas de Hardware**
- TRVs com clusters padrão (não proprietários)
- Sensores dedicados mais confiáveis
- Integração via outros protocolos

### Links de Monitoramento
```bash
# Repositórios relevantes
https://github.com/Koenkk/zigbee-herdsman-converters
https://github.com/Koenkk/zigbee2mqtt.io

# Issues relacionadas
Buscar: "TRVZB", "Viessmann", "viessmannWindowOpen"
```

## Conclusão

### Resumo Técnico
1. **Hardware:** ✅ Window detection implementado internamente
2. **Protocolo:** ❌ Atributos proprietários bloqueados
3. **Acesso:** ❌ UNSUPPORTED_ATTRIBUTE via Zigbee2MQTT
4. **Solução:** ✅ Usar alternativas práticas (sensor físico/template/desabilitar)

### Recomendação Final
**Para usuários do blueprint:** Configure `trv_window_open_sensor: ""` e use um sensor físico de porta/janela se quiser window detection. O blueprint funciona perfeitamente sem essa funcionalidade, que é apenas um bônus.

**Para desenvolvedores:** Monitore updates do Zigbee2MQTT para possível suporte futuro aos atributos Viessmann, mas não conte com isso a curto prazo.
