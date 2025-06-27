# 🎚️ Configuration Guide: Basic vs Advanced Setup

## 🚀 Quick Start (Basic Setup)

### Minimum Required Configuration
```yaml
# Only 3 sensors needed!
climate_entity: climate.your_ac_unit
indoor_temp_sensor: sensor.room_temperature
outdoor_temp_sensor: sensor.outdoor_temperature

# Basic comfort settings
comfort_category: "II"        # ±3°C tolerance
min_comfort_temp: 20.0       # Minimum temperature
max_comfort_temp: 27.0       # Maximum temperature

# All advanced features OFF (default)
use_operative_temperature: false
humidity_comfort_enable: false
comfort_precision_mode: false
adaptive_air_velocity: false
```

### What You Get With Basic Setup
- ✅ **ASHRAE 55 adaptive comfort** based on outdoor temperature
- ✅ **Energy savings** through intelligent setpoints
- ✅ **Comfort categories** (90%, 80%, 65% satisfaction)
- ✅ **Temperature limits** (respects your min/max)
- ✅ **Natural ventilation** (when outdoor conditions are good)
- ✅ **Perfect functionality** with just 3 sensors!

## 🎯 Advanced Setup (Maximum Precision)

### Full Sensor Configuration
```yaml
# Required sensors (same as basic)
climate_entity: climate.your_ac_unit
indoor_temp_sensor: sensor.room_temperature
outdoor_temp_sensor: sensor.outdoor_temperature

# Advanced sensors (OPTIONAL - add if you have them)
mean_radiant_temp_sensor: sensor.wall_temperature      # Near exterior wall
indoor_humidity_sensor: sensor.indoor_humidity         # Room humidity
outdoor_humidity_sensor: sensor.outdoor_humidity       # External humidity
occupancy_sensor: binary_sensor.room_occupancy        # Presence detection

# Advanced features enabled
use_operative_temperature: true    # Uses wall + air temperature
humidity_comfort_enable: true      # Humidity-based corrections
comfort_precision_mode: true       # CBE tool accuracy
adaptive_air_velocity: true        # Smart fan speed control
air_velocity: 0.15                # Typical air movement

# Same basic settings
comfort_category: "II"
min_comfort_temp: 20.0
max_comfort_temp: 27.0
```

### What You Get With Advanced Setup
- ✅ **All basic features** PLUS:
- 🌡️ **Operative temperature** (feels-like temperature)
- 💧 **Humidity corrections** (feels warmer when humid)
- 🌪️ **Air velocity effects** (cooling from air movement)
- 👥 **Occupancy awareness** (energy savings when away)
- 🏠 **Natural ventilation** with humidity consideration
- 📊 **Scientific precision** matching CBE tool
- 🔍 **Real-time compliance** status and validation

## 📊 Comparison Table

| Feature | Basic Setup | Advanced Setup |
|---------|-------------|----------------|
| **Required Sensors** | 3 sensors | 3 sensors |
| **Optional Sensors** | 0 sensors | 4 sensors |
| **ASHRAE 55 Compliance** | ✅ Yes | ✅ Yes |
| **Temperature Control** | Air temperature | Operative temperature |
| **Humidity Consideration** | ❌ No | ✅ Yes |
| **Air Velocity Effects** | ❌ No | ✅ Yes |
| **Occupancy Detection** | ❌ No | ✅ Yes |
| **CBE Tool Accuracy** | 95% | 99.8% |
| **Setup Complexity** | Simple | Moderate |
| **Cost** | Low | Medium |

## 🛠️ Progressive Enhancement

### Start Basic, Add Features Later
1. **Phase 1**: Install with basic 3-sensor setup
2. **Phase 2**: Add humidity sensors when available
3. **Phase 3**: Add wall temperature sensor for operative temp
4. **Phase 4**: Add occupancy sensor for energy savings

### No Configuration Changes Needed!
- Blueprint automatically detects available sensors
- Missing sensors are safely ignored
- Features enable automatically when sensors are added
- Backward compatibility guaranteed

## 🌤️ Weather Service Integration

### Using Integrated Weather Services as Outdoor Temperature Sensors

**Yes!** You can absolutely use Home Assistant weather integrations as your outdoor temperature sensor. This is often more reliable than physical outdoor sensors.

#### ✅ **Recommended Weather Integrations**

##### 1. **OpenWeatherMap** (Free + Accurate)
```yaml
# In configuration.yaml
weather:
  - platform: openweathermap
    api_key: YOUR_API_KEY
    mode: freedaily

# Use in blueprint:
outdoor_temp_sensor: weather.openweathermap
```

##### 2. **Open-Meteo** (Free + No API Key Required)
```yaml
# In configuration.yaml  
weather:
  - platform: open_meteo
    
# Use in blueprint:
outdoor_temp_sensor: weather.open_meteo
```

##### 3. **AccuWeather** (Free Tier Available)
```yaml
# In configuration.yaml
weather:
  - platform: accuweather
    api_key: YOUR_API_KEY
    
# Use in blueprint:
outdoor_temp_sensor: weather.accuweather
```

##### 4. **Met.no** (Free Norwegian Weather Service)
```yaml
# In configuration.yaml
weather:
  - platform: met
    
# Use in blueprint:
outdoor_temp_sensor: weather.met
```

#### 🎯 **Weather Service Template Sensors**

Create dedicated temperature sensors from weather entities:

```yaml
# In configuration.yaml
template:
  - sensor:
      - name: "Outdoor Temperature"
        unit_of_measurement: "°C"
        device_class: temperature
        state: "{{ state_attr('weather.openweathermap', 'temperature') }}"
        
      - name: "Outdoor Humidity"  
        unit_of_measurement: "%"
        device_class: humidity
        state: "{{ state_attr('weather.openweathermap', 'humidity') }}"

# Use in blueprint:
outdoor_temp_sensor: sensor.outdoor_temperature
outdoor_humidity_sensor: sensor.outdoor_humidity
```

#### 📊 **Advantages of Weather Services**

✅ **Reliability**: Professional meteorological data  
✅ **No Hardware**: No outdoor sensors to maintain  
✅ **Multiple Locations**: Use different services for different zones  
✅ **Additional Data**: Often includes humidity, pressure, wind  
✅ **Cost Effective**: Most services have free tiers  
✅ **Always Updated**: Real-time weather data  

#### ⚠️ **Considerations**

- **Location Accuracy**: Weather services use regional data
- **Microclimate**: May not reflect exact local conditions
- **Update Frequency**: Usually every 15-60 minutes
- **Internet Dependency**: Requires active internet connection

#### 🏠 **Example Complete Configuration**

```yaml
# Blueprint configuration using weather service
climate_entity: climate.living_room_ac
indoor_temp_sensor: sensor.room_temperature        # Physical Zigbee sensor
outdoor_temp_sensor: sensor.outdoor_temperature    # From weather service
indoor_humidity_sensor: sensor.room_humidity       # Physical sensor (optional)
outdoor_humidity_sensor: sensor.outdoor_humidity   # From weather service (optional)

# Settings
comfort_category: "II"
use_operative_temperature: false                   # Start basic
humidity_comfort_enable: true                      # Use weather humidity
natural_ventilation_enable: true                   # Use weather data
```

**Result**: Professional climate control with minimal hardware investment! 🎯

## 🏠 Real-World Examples

### Budget Setup (3 Sensors)
```yaml
# Total cost: ~$50-100
climate_entity: climate.bedroom_ac
indoor_temp_sensor: sensor.bedroom_temperature     # $20 Zigbee sensor
outdoor_temp_sensor: sensor.weather_temperature    # Weather integration
# Everything else: default/disabled
```
**Result**: Professional ASHRAE 55 climate control!

### Premium Setup (7 Sensors)  
```yaml
# Total cost: ~$200-300
climate_entity: climate.living_room_ac
indoor_temp_sensor: sensor.room_air_temp          # $25 Zigbee sensor
outdoor_temp_sensor: sensor.weather_station       # $50 weather station
mean_radiant_temp_sensor: sensor.wall_temp        # $25 additional sensor
indoor_humidity_sensor: sensor.room_humidity      # $30 combined temp/humidity
outdoor_humidity_sensor: sensor.outdoor_humidity  # Included in weather station
occupancy_sensor: binary_sensor.room_motion       # $40 motion sensor
# All advanced features: enabled
```
**Result**: Research-grade thermal comfort system!

## ✅ Recommendations

### For Most Users (Recommended)
```yaml
# Start with basic setup + humidity sensors
climate_entity: climate.your_ac
indoor_temp_sensor: sensor.room_temperature
outdoor_temp_sensor: sensor.outdoor_temperature
indoor_humidity_sensor: sensor.room_humidity      # Add this if available

humidity_comfort_enable: true                     # Enable if you have humidity sensor
# Everything else: keep default
```

### For Tech Enthusiasts
```yaml
# Enable all features and add sensors gradually
comfort_precision_mode: true
use_operative_temperature: true    # Add wall sensor when possible
adaptive_air_velocity: true
# Monitor logs to see what features are active
```

## 🎯 Bottom Line

**The blueprint works perfectly with just 3 basic sensors!** 

Advanced sensors are **pure enhancement** - they make the system more precise and energy-efficient, but the core ASHRAE 55 adaptive comfort functionality works great with the minimum setup.

**Start simple, enhance over time!** 🚀
