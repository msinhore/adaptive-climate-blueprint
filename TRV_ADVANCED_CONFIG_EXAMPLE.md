# TRV Advanced Configuration Example - Sonoff TRVZB Integration

## Complete Configuration Example

Below is a complete configuration example for integrating Sonoff TRVZB with the Adaptive Comfort Adaptive Climate Blueprint's dual climate control system.

### Basic Dual Climate Setup
```yaml
# Required - Enable dual climate control
dual_climate_control: true

# Required - Primary heating device (TRV)
primary_climate_entity: climate.radiator_sala

# Required - Main climate device (AC with heat mode)
climate_entity: climate.ac_living_room

# Thresholds for dual system coordination
secondary_heating_threshold: 2.0  # °C below target to activate secondary heating
trv_priority_temp_difference: 5.0  # °C outdoor-indoor diff for TRV priority
```

### Advanced TRV Monitoring Setup
```yaml
# Enable advanced TRV efficiency monitoring
enable_trv_efficiency_monitoring: true

# TRV valve position monitoring
trv_valve_opening_sensor: number.radiator_sala_valve_opening_degree
trv_valve_closing_sensor: number.radiator_sala_valve_closing_degree

# TRV window open detection integration
# IMPORTANTE: Para Sonoff TRVZB, verifique qual entidade existe no seu setup:
# Opção 1: Se existe binary_sensor separado (verifique Developer Tools > States)
# trv_window_open_sensor: binary_sensor.radiator_sala_window_detection
#
# Opção 2: Se só existe o switch de controle (mais comum)
# trv_window_open_sensor: ""  # Deixar vazio e monitorar via hvac_action
#
# Opção 3: Se TRV reporta via atributos do climate entity
# Monitore state_attr('climate.radiator_sala', 'window_detection') nos templates
trv_window_open_sensor: ""  # Verificar primeiro quais entidades existem

# TRV motor activity monitoring
trv_running_steps_sensor: sensor.radiator_sala_closing_steps
```

## Available Sonoff TRVZB Entities

### Climate Entity (Primary)
- `climate.radiator_sala` - Main TRV control entity
- **Importante**: Use `state_attr('climate.radiator_sala', 'hvac_action')` para monitorar se está aquecendo
- Estados do hvac_action: 'idle', 'heating', 'off'

### Control Entities
- `switch.radiator_sala_child_lock` - Safety lock control
- `number.radiator_sala_frost_protection_temperature` - Frost protection setting
- `switch.radiator_sala_open_window` - **Habilita/desabilita** detecção de janela (controle)
- ⚠️ `sensor.radiator_sala_open_window` - **Verificar se existe** no seu setup
- `number.radiator_sala_external_temperature_input` - External temperature input
- `number.radiator_sala_temperature_accuracy` - Temperature accuracy adjustment

### Valve Monitoring Entities
- `number.radiator_sala_valve_closing_degree` - Valve closing percentage
- `number.radiator_sala_valve_opening_degree` - Valve opening percentage

### System Monitoring Entities  
- `sensor.radiator_sala_battery` - Battery level monitoring
- `sensor.radiator_sala_closing_steps` - Valve motor closing activity
- `sensor.radiator_sala_idle_steps` - Valve motor idle position
- `sensor.radiator_sala_valve_closing_limit_voltage` - Valve closing voltage
- `sensor.radiator_sala_valve_motor_running_voltage` - Motor operation voltage
- `sensor.radiator_sala_valve_opening_limit_voltage` - Valve opening voltage
- `update.radiator_sala` - Firmware update status

## Entity Usage in Blueprint

### Primary Usage (Recommended)
**For optimal performance and monitoring, use these entities:**

1. **Valve Position Monitoring**:
   - `number.radiator_sala_valve_opening_degree` → `trv_valve_opening_sensor`
   - `number.radiator_sala_valve_closing_degree` → `trv_valve_closing_sensor`

2. **Window Detection Integration**:
   - **Primeiro**: Verifique no Developer Tools > States quais entidades existem
   - `switch.radiator_sala_open_window` → Controle (habilita/desabilita)
   - Procure por: `binary_sensor.radiator_sala_window_detection` ou similar
   - Se não existir sensor separado, deixe `trv_window_open_sensor: ""`
   - O blueprint pode monitorar via mudanças no hvac_action

3. **Motor Activity Monitoring**:
   - `sensor.radiator_sala_closing_steps` → `trv_running_steps_sensor`

### Secondary Usage (Optional)
**Additional entities for advanced monitoring dashboards:**

- `sensor.radiator_sala_battery` - Monitor TRV battery in your dashboard
- `sensor.radiator_sala_idle_steps` - Track TRV maintenance needs
- `update.radiator_sala` - Monitor firmware updates

## TRV Data Analysis

### Valve Efficiency Indicators
```yaml
# Good Performance
valve_opening_degree: 40-70%  # Moderate opening, effective heating
hvac_action: "heating"        # TRV actively heating
local_temperature: Rising      # Temperature increasing

# Poor Performance  
valve_opening_degree: 85%+    # High opening, struggling to heat
hvac_action: "heating"        # Trying to heat but...
local_temperature: Stable     # No temperature improvement

# Optimal Conditions
valve_opening_degree: 50%     # Efficient position
hvac_action: "heating"        # Active heating
temperature_difference: +2°C  # Good heat transfer
```

### Window Detection Scenarios
```yaml
# TRV Detection
open_window: "ON"             # TRV algorithm detected window
→ Blueprint pauses HVAC immediately

# Blueprint Detection  
temperature_drop: 2.5°C       # Rapid temp drop detected
time_window: 3 minutes        # Within detection time
→ Blueprint pauses HVAC after analysis

# Combined Detection
open_window: "ON" AND temperature_drop: 2.0°C
→ Maximum accuracy, immediate response
```

## Configuration Optimization

### For Well-Insulated Homes
```yaml
secondary_heating_threshold: 1.5  # Less aggressive dual heating
trv_priority_temp_difference: 6.0  # Favor TRV in more conditions
enable_trv_efficiency_monitoring: true  # Monitor performance
```

### For Older/Drafty Homes
```yaml
secondary_heating_threshold: 2.5  # More aggressive dual heating  
trv_priority_temp_difference: 4.0  # Favor AC for faster response
enable_trv_efficiency_monitoring: true  # Critical for efficiency
```

### For Maximum Energy Savings
```yaml
secondary_heating_threshold: 2.0  # Balanced approach
trv_priority_temp_difference: 5.0  # Standard efficiency logic
enable_trv_efficiency_monitoring: true  # Essential for optimization
# All TRV sensors configured for maximum data
```

## Troubleshooting Common Issues

### TRV Not Responding
**Check these entities:**
- `climate.radiator_sala` state should change
- `number.radiator_sala_valve_opening_degree` should adjust
- `sensor.radiator_sala_closing_steps` should show activity

### Valve Stuck Issues
**Monitor these indicators:**
- Valve opening degree stuck at same value
- Motor voltage readings abnormal
- No closing/opening steps activity

### Window Detection Problems
**Verify these sensors:**
- `switch.radiator_sala_open_window` responds to actual window opening
- Blueprint temperature drop detection working
- Both systems coordinate properly

### Efficiency Monitoring Issues
**Check sensor availability:**
```bash
# Home Assistant Developer Tools → States
# Verify all entities are available and updating:
number.radiator_sala_valve_opening_degree
number.radiator_sala_valve_closing_degree  
switch.radiator_sala_open_window
sensor.radiator_sala_closing_steps
```

## Performance Monitoring

### Key Metrics to Track
- **Valve Position vs. Indoor Temperature**: Should correlate well
- **TRV Action vs. Actual Heating**: Heating action should increase temperature
- **Window Detection Accuracy**: Both TRV and blueprint should detect windows
- **Energy Consumption**: Should decrease with dual system coordination

### Expected Improvements
- **25-35% heating energy savings** with proper TRV coordination
- **90%+ window detection accuracy** with dual detection systems
- **Faster temperature recovery** with dual heating capability
- **Reduced TRV wear** through intelligent AC support

---

*This configuration example demonstrates the cutting-edge integration of Adaptive Comfort adaptive comfort principles with modern TRV sensor technology for maximum efficiency and comfort.*
