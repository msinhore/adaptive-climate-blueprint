# 🌤️ Configuração com Serviços Meteorológicos

Este guia mostra como usar serviços meteorológicos integrados ao Home Assistant como sensor de temperatura externa no blueprint de controle climático adaptativo.

## ✅ **Por que usar serviços meteorológicos?**

- **🎯 Sem hardware externo**: Não precisa de sensores físicos do lado de fora
- **📡 Dados profissionais**: Informações meteorológicas precisas e atualizadas
- **💰 Custo zero**: Maioria dos serviços tem planos gratuitos
- **🔄 Sempre atualizado**: Dados em tempo real
- **🌍 Múltiplas localizações**: Use diferentes serviços conforme necessário

## 🌤️ **Serviços Recomendados**

### 1. **Open-Meteo** (Recomendado - Sem API Key)
```yaml
# Em configuration.yaml
weather:
  - platform: open_meteo
    latitude: -23.5505  # São Paulo exemplo
    longitude: -46.6333
    
# No blueprint:
outdoor_temp_sensor: weather.open_meteo
```

### 2. **OpenWeatherMap** (Gratuito até 1000 calls/dia)
```yaml
# Em configuration.yaml
weather:
  - platform: openweathermap
    api_key: SUA_CHAVE_API
    mode: freedaily
    
# No blueprint:
outdoor_temp_sensor: weather.openweathermap
```

### 3. **AccuWeather** (50 calls/dia gratuitas)
```yaml
# Em configuration.yaml
weather:
  - platform: accuweather
    api_key: SUA_CHAVE_API
    
# No blueprint:
outdoor_temp_sensor: weather.accuweather
```

## 🔧 **Configuração Completa de Exemplo**

### Configuração Básica (3 sensores)
```yaml
# Automação do blueprint
climate_entity: climate.sala_ar_condicionado
indoor_temp_sensor: sensor.temperatura_sala        # Sensor físico interno
outdoor_temp_sensor: weather.open_meteo           # Serviço meteorológico
comfort_category: "II"                            # ±3°C tolerância
```

### Configuração Avançada (com umidade do tempo)
```yaml
# Criar sensores de template primeiro
template:
  - sensor:
      - name: "Temperatura Externa"
        unit_of_measurement: "°C"
        device_class: temperature
        state: "{{ state_attr('weather.open_meteo', 'temperature') }}"
        
      - name: "Umidade Externa"
        unit_of_measurement: "%"
        device_class: humidity
        state: "{{ state_attr('weather.open_meteo', 'humidity') }}"

# Configuração do blueprint
climate_entity: climate.quarto_ar_condicionado
indoor_temp_sensor: sensor.temperatura_quarto
outdoor_temp_sensor: sensor.temperatura_externa    # Template do serviço meteorológico
indoor_humidity_sensor: sensor.umidade_quarto      # Sensor físico (opcional)
outdoor_humidity_sensor: sensor.umidade_externa    # Template do serviço meteorológico
humidity_comfort_enable: true
natural_ventilation_enable: true
```

## 📊 **Comparação: Serviço vs Sensor Físico**

| Característica | Serviço Meteorológico | Sensor Físico |
|----------------|----------------------|---------------|
| **Custo** | Gratuito | R$ 50-200 |
| **Instalação** | Configuração | Hardware + instalação |
| **Manutenção** | Zero | Bateria, calibração |
| **Precisão Local** | Regional (~2km) | Exata (sua casa) |
| **Confiabilidade** | Alta | Depende da manutenção |
| **Dados Extras** | Umidade, pressão, vento | Apenas temperatura |

## ⚡ **Configuração Rápida - Recomendada**

Para brasileiros, recomendamos esta configuração simples:

```yaml
# Em configuration.yaml
weather:
  - platform: open_meteo
    name: "Tempo Local"

# Configuração do blueprint
climate_entity: climate.seu_ar_condicionado
indoor_temp_sensor: sensor.temperatura_ambiente  # Sensor Zigbee ~R$ 30
outdoor_temp_sensor: weather.tempo_local         # Serviço gratuito
comfort_category: "II"                           # Confortável para casa
energy_save_mode: true                           # Economia de energia
```

## 🎯 **Resultado**

Com apenas um sensor interno (R$ 30) + serviço meteorológico gratuito, você terá:

✅ Controle climático adaptativo ASHRAE 55 completo
✅ 15-30% economia de energia
✅ Comfort zones dinâmicas baseadas no tempo externo
✅ Ventilação natural automática
✅ Zero manutenção externa

**É a forma mais prática e econômica de implementar controle climático inteligente!** 🚀

## 🔍 **Troubleshooting**

### Problema: Sensor weather não aparece
```yaml
# Verifique se a integração weather está funcionando
developer_tools → States → procure por "weather."
```

### Problema: Dados não atualizam
```yaml
# Serviços meteorológicos atualizam a cada 15-60 minutos
# Isso é normal e suficiente para controle climático
```

### Problema: Temperatura parece imprecisa
```yaml
# Use um offset se necessário:
template:
  - sensor:
      - name: "Temperatura Externa Ajustada"
        state: "{{ state_attr('weather.open_meteo', 'temperature') | float - 2 }}"
```

**Dica**: Monitore por alguns dias e ajuste se necessário. Diferenças de 1-2°C são normais entre dados regionais e microclima local.
