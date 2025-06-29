# Safe Summer Configuration for TRV Testing

# This configuration allows testing TRV integration without activating heating during summer

## Blueprint Configuration (Summer Safe)
```yaml
# Basic Adaptive Comfort Settings
climate_entity: climate.your_ac_unit  # Your main AC for cooling
indoor_temp_sensor: sensor.your_indoor_temp
outdoor_temp_sensor: sensor.your_outdoor_temp

# Dual Climate Control (Ready for Winter)
dual_climate_control: true
primary_climate_entity: climate.radiator_sala  # TRV ready for winter

# TRV Monitoring (Active Even in Summer)
enable_trv_efficiency_monitoring: true
trv_valve_opening_sensor: number.radiator_sala_valve_opening_degree
trv_valve_closing_sensor: number.radiator_sala_valve_closing_degree
trv_window_open_sensor: switch.radiator_sala_open_window
trv_running_steps_sensor: sensor.radiator_sala_closing_steps

# Thresholds (Safe Values)
secondary_heating_threshold: 2.0  # Won't trigger in summer
trv_priority_temp_difference: 5.0  # Ready for winter logic

# Summer Features (Active Now)
window_open_detection: true
window_open_temp_drop: 2.0
window_open_detection_time: 5
window_open_pause_duration: 15

# Optional Features
natural_ventilation_enable: true
adaptive_air_velocity: true
seasonal_optimization: true  # Will detect summer mode
```

## What This Configuration Does in Summer:

### ✅ Active Features (Working Now):
- **Window Detection**: Both blueprint and TRV detection active
- **Seasonal Logic**: Detects summer, optimizes for cooling/ventilation
- **Smart Rounding**: Optimizes AC cooling temperatures
- **TRV Monitoring**: Collects baseline data without heating
- **Logging**: Records all TRV sensor data for analysis

### 🛡️ Safe Features (Ready for Winter):
- **Dual Climate Control**: Configured but won't heat in summer
- **TRV Efficiency**: Monitors valve but no heating activation
- **Temperature Coordination**: Logic ready but inactive in summer

### 📊 Data Collection (Happening Now):
- TRV valve positions (should be minimal in summer)
- Window detection accuracy from both sources
- Battery levels and motor activity
- Sensor availability and responsiveness

## Verification Steps for Summer:

1. **Check All Entities Available**:
   ```bash
   # In Developer Tools → States, verify these exist:
   climate.radiator_sala
   number.radiator_sala_valve_opening_degree
   number.radiator_sala_valve_closing_degree
   switch.radiator_sala_open_window
   sensor.radiator_sala_closing_steps
   ```

2. **Test Window Detection**:
   - Open a window/door
   - Check if TRV switch.radiator_sala_open_window changes to "on"
   - Verify blueprint also detects temperature drop
   - Monitor logbook for dual detection messages

3. **Monitor TRV Summer Baseline**:
   - Valve opening should be 0-20% (no heating needed)
   - Battery should be stable
   - Motor steps should be minimal
   - Window detection should respond to actual windows

4. **Verify Seasonal Logic**:
   - Blueprint should detect summer season (outdoor temp > 18°C)
   - Should prefer cooling/ventilation over heating
   - TRV coordination should be dormant but ready

## Expected Summer Logs:

```
# Normal summer operation (no heating needed)
Adaptive Comfort Adaptive Climate: Natural ventilation active. HVAC turned off.
Outdoor: 28°C, Indoor: 24°C, Comfort zone: 22-26°C

# Window detection test
Window/door open detected by TRV sensor! HVAC paused for 15 minutes.
TRV window detection: true, Blueprint detection: true.
Indoor: 24°C, Outdoor: 28°C, TRV: 24.1°C.

# TRV monitoring (baseline data)
TRV Summer Test Data: Valve 5%, Window false, Battery 98%, Ready for winter: Yes
```

## Preparation for Winter Testing:

### Current Status (Summer):
- ✅ TRV entities configured and responsive
- ✅ Window detection working from both sources  
- ✅ Blueprint recognizes summer season correctly
- ✅ All sensors providing baseline data

### Ready for Winter:
- 🔄 Switch to heating season automatically when outdoor < 18°C
- 🔄 TRV will become primary heating device
- 🔄 Dual climate coordination will activate
- 🔄 Efficiency monitoring will analyze real heating performance

### When Winter Arrives:
1. **Monitor first cold days** (outdoor < 18°C)
2. **Watch TRV activation** and valve response
3. **Verify dual coordination** between TRV and AC heat mode
4. **Analyze efficiency data** and adjust thresholds
5. **Document energy savings** compared to previous winter

---

*This configuration ensures you're fully prepared for winter testing while safely monitoring TRV integration during summer.*
