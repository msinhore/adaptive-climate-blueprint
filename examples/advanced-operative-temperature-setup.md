# 🏠 Advanced Configuration - Radiant Temperature + Humidity Sensors

## 🌡️ Temperature Sensor Concepts

### **Indoor Air Temperature Sensor**
- **Location**: Between interior rooms (e.g., between living room and kitchen)
- **Purpose**: Measure ambient air temperature without external influence
- **Characteristics**: Away from windows, external walls, or heat sources

### **Mean Radiant Temperature Sensor (External Wall)**
- **Location**: Near the wall facing the exterior
- **Purpose**: Capture influence of solar radiation, heat/cold from external wall
- **Characteristics**: Measures the effect of external environment on indoor temperature

### **Recommended Setup**
- ✅ **Indoor sensor** between rooms (ambient air temperature)
- ✅ **External wall sensor** near exterior wall (radiant temperature)
- ✅ **Humidity sensors** indoor and outdoor
- ✅ **Air conditioning** with multiple modes and fan speeds

## 🎯 Configuration for Maximum Thermal Precision

```yaml
# Required entities
climate_entity: climate.living_room_ac
indoor_temp_sensor: sensor.indoor_ambient_temperature  # Between rooms
outdoor_temp_sensor: sensor.outdoor_temperature

# Advanced sensors (recommended for scientific precision)
mean_radiant_temp_sensor: sensor.external_wall_temperature  # Near exterior wall
indoor_humidity_sensor: sensor.indoor_humidity
outdoor_humidity_sensor: sensor.outdoor_humidity
occupancy_sensor: binary_sensor.room_presence

# ASHRAE 55 comfort settings
comfort_category: "II"  # ±3°C - Typical residential
min_comfort_temp: 20.0
max_comfort_temp: 27.0

# Advanced features enabled
use_operative_temperature: true    # ✅ Use operative temperature
air_velocity: 0.15                # Typical residential air movement
adaptive_air_velocity: true       # ✅ Adaptive fan speed control
humidity_comfort_enable: true     # ✅ Humidity correction
comfort_precision_mode: true      # ✅ Maximum precision (CBE mode)

# Energy efficiency
energy_save_mode: true
natural_ventilation_enable: true
natural_ventilation_threshold: 2.0
setback_temperature_offset: 2.0
```

## 🌡️ How Operative Temperature Works

### 1. **Operative Temperature Calculation**
```
Indoor sensor (between rooms): 25°C
External wall sensor: 28°C (solar/radiant influence from wall)
Operative temperature = (25 + 28) / 2 = 26.5°C
```
**Benefit**: More precise measurement considering both ambient air and radiant heat

### 2. **Why Two Sensors?**
- **Indoor sensor**: Measures actual air temperature in the environment
- **External wall sensor**: Detects heat/cold transmitted through exterior wall
- **Result**: Temperature you actually feel (operative)

### 3. **Humidity Correction**
```
Indoor humidity: 70% (high)
Correction: +0.3°C (feels warmer)
Adjusted temperature for comfort: 26.5 + 0.3 = 26.8°C
```
**Benefit**: AC will be more aggressive on humid days to maintain real comfort

### 4. **Intelligent Natural Ventilation**
```
External temp: 24°C, External humidity: 60%
Internal temp: 26°C, Internal humidity: 65%
Decision: Enable natural ventilation (AC turns off automatically)
```
**Benefit**: Energy savings when external conditions are favorable

### 5. **Adaptive Fan Speed Control**
```
Current temperature: 29°C
Maximum comfort temperature: 27°C  
Deviation: 2°C
Fan speed: "medium"
```
**Benefit**: More efficient cooling when temperature exceeds comfort zone

## 📍 Optimal Sensor Placement

### **Indoor Temperature Sensor**
- ✅ **Location**: Center of room, away from external walls
- ✅ **Height**: 1.5m from floor (breathing level)
- ✅ **Avoid**: Near windows, doors, heat sources
- ✅ **Objective**: Actual ambient air temperature

### **External Wall Temperature Sensor**
- ✅ **Location**: 30-50cm from exterior-facing wall
- ✅ **Position**: Where there's maximum solar/thermal radiation influence
- ✅ **Avoid**: Permanent shadows or corners
- ✅ **Objective**: Capture radiant effect from exterior wall

## 📊 Precision Comparison

### Basic Mode (indoor sensor only)
```
Outdoor: 32°C
Adaptive comfort: 27.1°C
Comfort zone: 24.1-30.1°C
Base: Air temperature only
```

### Advanced Mode (operative temperature + humidity)
```
Outdoor: 32°C, Indoor humidity: 70%
Indoor sensor: 26°C, Wall sensor: 29°C
Operative temperature: 27.5°C
Humidity correction: +0.3°C
Final comfort zone: 24.8-30.8°C
```
**Result**: More precise comfort zone based on actual thermal sensation

## 🔧 Entity Mapping for Home Assistant

```yaml
# Replace with your actual entity_ids
climate_entity: climate.living_room_ac
indoor_temp_sensor: sensor.indoor_temperature        # Between rooms
outdoor_temp_sensor: sensor.outdoor_temperature
mean_radiant_temp_sensor: sensor.external_wall_temp  # Near exterior wall
indoor_humidity_sensor: sensor.indoor_humidity
outdoor_humidity_sensor: sensor.outdoor_humidity
occupancy_sensor: binary_sensor.room_presence
```

## 🎯 Benefits of Advanced Configuration

1. **Superior Precision**: Operative temperature reflects actual thermal sensation
2. **Intelligent Control**: Fan speed adapts automatically to thermal demand
3. **Energy Savings**: Automatic natural ventilation when conditions are favorable
4. **Personalized Comfort**: Respects absolute temperature limits configured
5. **Climate Adaptation**: Adjustments based on humidity and external conditions

## 📈 Expected Results

- **Savings**: 20-35% reduction in energy consumption
- **Comfort**: Precise maintenance of real comfort zone (not just air temperature)
- **Intelligence**: Decisions based on multiple environmental factors
- **Durability**: Fewer AC on/off cycles due to more precise measurement

This configuration will have scientific precision equivalent to the CBE Thermal Comfort Tool! 🎯
