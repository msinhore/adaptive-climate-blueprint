# TRV Testing Templates for Summer Season

## Testing Strategy During Summer

Since TRV heating is not needed during summer, here are ways to validate the dual climate control system:

### 1. Configuration Validation (Do This Now)

#### Check TRV Entity Availability
Go to **Developer Tools → States** and verify these entities exist and are responsive:

```
climate.radiator_sala                           # Principal TRV control
    ↳ state_attr('climate.radiator_sala', 'open_window')  # Window detection property
number.radiator_sala_valve_opening_degree       # Valve position
number.radiator_sala_valve_closing_degree       # Valve closing
sensor.radiator_sala_closing_steps              # Motor activity
sensor.radiator_sala_battery                    # Battery level
```

**IMPORTANTE**: O Sonoff TRVZB não cria `binary_sensor.radiator_sala_open_window` como entidade separada. O window detection é uma **propriedade** do climate entity.

#### Criar Template Sensor para Window Detection
Se quiser usar no blueprint, adicione em `configuration.yaml`:

```yaml
template:
  - binary_sensor:
      - name: "Sala Window Open TRV"
        unique_id: sala_window_open_trv
        state: "{{ state_attr('climate.radiator_sala', 'open_window') == true }}"
        device_class: window
```

#### Blueprint Configuration Test
Create automation with these settings (won't activate heating in summer):

```yaml
# Safe summer configuration - no actual heating will occur
dual_climate_control: true
primary_climate_entity: climate.radiator_sala
secondary_heating_threshold: 2.0
trv_priority_temp_difference: 5.0
enable_trv_efficiency_monitoring: true
trv_window_open_sensor: binary_sensor.sala_window_open_trv  # Template sensor baseado na propriedade Z2M
# Add all TRV sensors...
```

### 2. Summer Features Testing (Available Now)

#### Window Detection Testing
- Open windows/doors and verify detection works
- Check if both blueprint and TRV detection coordinate
- Monitor logbook for window detection messages

#### Seasonal Logic Testing  
- Verify summer mode prevents heating when indoor < target
- Test ventilation mode activation
- Check AC cooling optimization

#### Smart Rounding Testing
- Monitor AC cooling with smart rounding
- Verify energy-optimized temperature setting
- Check logging shows rounding decisions

### 3. Simulation Testing with Input Numbers

Create input numbers to simulate winter conditions:

#### Create Test Input Numbers
```yaml
# Add to configuration.yaml
input_number:
  test_outdoor_temp:
    name: "Test Outdoor Temperature"
    min: -20
    max: 40
    step: 0.5
    unit_of_measurement: "°C"
    initial: 5  # Simulate winter
    
  test_indoor_temp:
    name: "Test Indoor Temperature"  
    min: 10
    max: 30
    step: 0.1
    unit_of_measurement: "°C"
    initial: 18  # Simulate cold indoor
```

#### Create Test Automation
Use test inputs instead of real sensors to simulate winter:

```yaml
# Temporary test automation
outdoor_temp_sensor: input_number.test_outdoor_temp
indoor_temp_sensor: input_number.test_indoor_temp
# Configure TRV settings...
```

#### Test Scenarios
Set different combinations and monitor logs:

**Scenario 1: Very Cold (TRV Priority Expected)**
- Outdoor: 0°C, Indoor: 18°C, Target: 21°C
- Expected: TRV priority, possible secondary heating

**Scenario 2: Mild Weather (AC Priority Expected)**  
- Outdoor: 16°C, Indoor: 19°C, Target: 21°C
- Expected: AC priority, TRV background support

### 4. TRV Sensor Data Collection (Summer Preparation)

Even without heating, collect TRV data for analysis:

#### Monitor TRV Entities Daily
Track these values to understand TRV behavior:

```yaml
# Template sensor to log TRV data
sensor:
  - platform: template
    sensors:
      trv_summer_monitoring:
        friendly_name: "TRV Summer Data"
        value_template: >
          Valve: {{ states('number.radiator_sala_valve_opening_degree') }}%, 
          Window Detected: {{ states('binary_sensor.radiator_sala_open_window') }}, 
          HVAC Action: {{ state_attr('climate.radiator_sala', 'hvac_action') }},
          Battery: {{ states('sensor.radiator_sala_battery') }}%,
          Steps: {{ states('sensor.radiator_sala_closing_steps') }}
```

#### Baseline Data Collection
- Record TRV valve positions during summer (should be minimal)
- Monitor window detection accuracy
- Check battery levels and update status
- Verify all sensors respond correctly

### 5. Pre-Winter Preparation Checklist

#### August/September Tasks:
- [ ] Verify all TRV entities working correctly
- [ ] Test blueprint configuration without heating activation
- [ ] Create dashboard cards for TRV monitoring
- [ ] Document current valve positions as baseline
- [ ] Test window detection integration

#### October Tasks (Pre-Winter):
- [ ] Switch to real temperature sensors
- [ ] Enable heating functions gradually
- [ ] Monitor first heating cycles carefully
- [ ] Adjust thresholds based on real performance
- [ ] Document energy consumption baseline

### 6. Dashboard Creation for TRV Monitoring

Create cards to monitor TRV status during summer:

```yaml
# TRV Monitoring Card
type: entities
title: "TRV Summer Monitoring"
entities:
  - entity: climate.radiator_sala
    name: "TRV Status"
  - entity: number.radiator_sala_valve_opening_degree
    name: "Valve Position"
  - entity: binary_sensor.radiator_sala_open_window
    name: "Window Detected (Auto)"
  - type: attribute
    entity: climate.radiator_sala
    attribute: hvac_action
    name: "HVAC Action (idle/heating)"
  - entity: sensor.radiator_sala_battery
    name: "Battery Level"
  - entity: sensor.radiator_sala_closing_steps
    name: "Motor Activity"
```

### 7. Testing Automation Logic

Create a test automation that logs TRV decisions without actual heating:

```yaml
automation:
  - alias: "TRV Logic Test (Summer Safe)"
    trigger:
      - platform: time_pattern
        minutes: "/30"  # Every 30 minutes
    action:
      - service: logbook.log
        data:
          name: "TRV Summer Test"
          message: >
            TRV Test Data: Valve {{ states('number.radiator_sala_valve_opening_degree') }}%, 
            Window Detected: {{ states('binary_sensor.radiator_sala_open_window') }}, 
            HVAC Action: {{ state_attr('climate.radiator_sala', 'hvac_action') }},
            Battery: {{ states('sensor.radiator_sala_battery') }}%,
            Ready for winter testing: {{ 'Yes' if states('climate.radiator_sala') != 'unavailable' else 'No' }}
```

## Expected Results During Summer

### Normal Summer Behavior:
- **TRV valve position**: 0-20% (minimal opening)
- **Window detection**: Should work normally
- **Battery level**: Should be stable
- **Motor activity**: Minimal steps
- **Blueprint**: Should detect summer season and prefer cooling/ventilation

### Validation Success Criteria:
- [ ] All TRV entities respond correctly
- [ ] Window detection works from both sources
- [ ] Blueprint recognizes summer season
- [ ] No heating activation in summer mode
- [ ] Logging shows correct seasonal logic
- [ ] TRV sensors provide consistent data

## Winter Testing Plan

When winter arrives, follow this progression:

### Week 1 (First Cold Days):
1. Monitor TRV activation and valve response
2. Check dual climate coordination
3. Validate efficiency calculations
4. Document energy consumption changes

### Week 2-3 (Optimization):
1. Adjust thresholds based on real performance
2. Fine-tune efficiency monitoring
3. Optimize temperature coordination
4. Measure actual energy savings

### Month 1+ (Long-term Validation):
1. Document 25-35% energy savings achievement
2. Create performance reports
3. Identify optimization opportunities
4. Plan system improvements

---

*This testing approach ensures system readiness for winter while taking advantage of available summer testing opportunities.*
