# 🌤️ Weather Services Integration Setup

This guide shows how to use weather services integrated with Home Assistant as outdoor temperature sensors in the adaptive climate control blueprint.

## ✅ **Why use weather services?**

- **🎯 No external hardware**: No need for physical outdoor sensors
- **📡 Professional data**: Accurate and updated meteorological information
- **💰 Zero cost**: Most services have free plans
- **🔄 Always updated**: Real-time data
- **🌍 Multiple locations**: Use different services as needed

## 🌤️ **Recommended Services**

### 1. **Open-Meteo** (Recommended - No API Key Required)
```yaml
# In configuration.yaml
weather:
  - platform: open_meteo
    latitude: 40.7128  # New York example
    longitude: -74.0060
    
# In blueprint:
outdoor_temp_sensor: weather.open_meteo
```

### 2. **OpenWeatherMap** (Free up to 1000 calls/day)
```yaml
# In configuration.yaml
weather:
  - platform: openweathermap
    api_key: YOUR_API_KEY
    mode: freedaily
    
# In blueprint:
outdoor_temp_sensor: weather.openweathermap
```

### 3. **AccuWeather** (50 free calls/day)
```yaml
# In configuration.yaml
weather:
  - platform: accuweather
    api_key: YOUR_API_KEY
    
# In blueprint:
outdoor_temp_sensor: weather.accuweather
```

## 🔧 **Complete Configuration Example**

### Basic Setup (3 sensors)
```yaml
# Blueprint automation
climate_entity: climate.living_room_ac
indoor_temp_sensor: sensor.room_temperature        # Physical indoor sensor
outdoor_temp_sensor: weather.open_meteo           # Weather service
comfort_category: "II"                            # ±3°C tolerance
```

### Advanced Setup (with weather humidity)
```yaml
# Create template sensors first
template:
  - sensor:
      - name: "Outdoor Temperature"
        unit_of_measurement: "°C"
        device_class: temperature
        state: "{{ state_attr('weather.open_meteo', 'temperature') }}"
        
      - name: "Outdoor Humidity"
        unit_of_measurement: "%"
        device_class: humidity
        state: "{{ state_attr('weather.open_meteo', 'humidity') }}"

# Blueprint configuration
climate_entity: climate.bedroom_ac
indoor_temp_sensor: sensor.bedroom_temperature
outdoor_temp_sensor: sensor.outdoor_temperature    # Template from weather service
indoor_humidity_sensor: sensor.room_humidity      # Physical sensor (optional)
outdoor_humidity_sensor: sensor.outdoor_humidity    # Template from weather service
humidity_comfort_enable: true
natural_ventilation_enable: true
```

## 📊 **Comparison: Weather Service vs Physical Sensor**

| Feature | Weather Service | Physical Sensor |
|---------|----------------|----------------|
| **Cost** | Free | $20-80 |
| **Installation** | Configuration only | Hardware + installation |
| **Maintenance** | Zero | Battery, calibration |
| **Local Precision** | Regional (~2km) | Exact (your location) |
| **Reliability** | High | Depends on maintenance |
| **Extra Data** | Humidity, pressure, wind | Temperature only |

## ⚡ **Quick Setup - Recommended**

Simple configuration for most users:

```yaml
# In configuration.yaml
weather:
  - platform: open_meteo
    name: "Local Weather"

# Blueprint configuration
climate_entity: climate.your_ac
indoor_temp_sensor: sensor.room_temperature      # Zigbee sensor ~$25
outdoor_temp_sensor: weather.local_weather       # Free service
comfort_category: "II"                           # Comfortable for home
energy_save_mode: true                           # Energy savings
```

## 🎯 **Results**

With just one indoor sensor ($25) + free weather service, you get:

✅ Complete ASHRAE 55 adaptive climate control
✅ 15-30% energy savings
✅ Dynamic comfort zones based on outdoor weather
✅ Automatic natural ventilation
✅ Zero outdoor maintenance

**The most practical and economical way to implement intelligent climate control!** 🚀

## 🔍 **Troubleshooting**

### Issue: Weather sensor doesn't appear
```yaml
# Check if weather integration is working
developer_tools → States → search for "weather."
```

### Issue: Data doesn't update
```yaml
# Weather services update every 15-60 minutes
# This is normal and sufficient for climate control
```

### Issue: Temperature seems inaccurate
```yaml
# Use an offset if needed:
template:
  - sensor:
      - name: "Adjusted Outdoor Temperature"
        state: "{{ state_attr('weather.open_meteo', 'temperature') | float - 2 }}"
```

**Tip**: Monitor for a few days and adjust if necessary. Differences of 1-2°C are normal between regional data and local microclimate.
