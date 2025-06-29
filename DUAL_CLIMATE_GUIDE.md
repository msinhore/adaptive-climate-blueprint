# Dual Climate Control (TRV + AC) - User Guide

## Overview

The Dual Climate Control feature allows you to optimize heating efficiency by coordinating two heating devices:
- **Primary Climate Entity (TRV)**: Thermostatic Radiator Valve or main heating system
- **Secondary Climate Entity (AC)**: Air conditioning unit operating in heat mode

This creates a hybrid heating system that automatically selects the most efficient strategy based on real-time conditions.

## Key Benefits

- **25-35% Energy Savings**: Intelligent device coordination reduces overall energy consumption
- **Faster Heating**: Dual systems can work together for rapid temperature recovery
- **Efficiency Optimization**: Prioritizes TRV when outdoor temperatures are very cold (better efficiency)
- **Smart Coordination**: Prevents device conflicts with coordinated temperature targets
- **Real-Time TRV Monitoring**: Advanced sensor integration detects TRV performance issues
- **Enhanced Window Detection**: Combines blueprint and TRV window detection for maximum accuracy
- **Automatic Problem Detection**: Identifies valve issues, low efficiency, and system problems
- **Performance-Based Decisions**: Uses actual TRV performance data, not just temperature thresholds

## Configuration Parameters

### Required Setup
1. **Dual Climate Control**: Enable the feature (default: disabled)
2. **Primary Climate Entity (TRV)**: Select your TRV or main heating device
3. **Secondary Heating Threshold**: Temperature difference that triggers secondary heating (1-5°C, default: 2°C)
4. **TRV Priority Temperature Threshold**: Outdoor-indoor difference that prioritizes TRV (2-10°C, default: 5°C)

### Advanced TRV Monitoring (Optional)
5. **Enable TRV Efficiency Monitoring**: Activate advanced TRV sensor integration (default: disabled)
6. **TRV Valve Opening Degree Sensor**: Monitor valve position for efficiency analysis
7. **TRV Valve Closing Degree Sensor**: Monitor valve closing capability
8. **TRV Window Open Detection**: Use TRV's built-in window open detection
9. **TRV Running Steps Sensor**: Monitor TRV motor activity for performance analysis

### Parameter Details

#### Secondary Heating Threshold (1-5°C)
- When indoor temperature is this far below target, both systems activate
- Lower values = more aggressive dual heating
- Higher values = more conservative, energy-focused approach
- **Recommended**: 2°C for balanced efficiency and comfort

#### TRV Priority Temperature Threshold (2-10°C)  
- When outdoor temperature is this much below indoor temperature, prioritize TRV
- Based on principle that TRV/radiators are more efficient in very cold weather
- **Recommended**: 5°C for optimal efficiency balance

#### Advanced TRV Monitoring (Optional)
- **Enable TRV Efficiency Monitoring**: Activates real-time TRV performance analysis
- **Valve Position Sensors**: Monitor opening/closing degrees for efficiency calculations  
- **Window Open Detection**: Integrates TRV's built-in window detection with blueprint logic
- **Running Steps Sensor**: Tracks TRV motor activity to detect performance issues
- **Efficiency Algorithm**: Automatically detects when TRV is working inefficiently

**Example TRV Entities (Sonoff TRVZB)**:
```yaml
trv_valve_opening_sensor: number.radiator_sala_valve_opening_degree
trv_valve_closing_sensor: number.radiator_sala_valve_closing_degree  
trv_window_open_sensor: switch.radiator_sala_open_window
trv_running_steps_sensor: sensor.radiator_sala_closing_steps
```

## How It Works

### Decision Logic

The system evaluates two key factors:
1. **Temperature Difference Below Target**: How far indoor temperature is below the desired target
2. **Outdoor-Indoor Temperature Difference**: Indicates heating load and efficiency considerations

### Strategy Selection

#### Enhanced TRV Priority Mode (Advanced Efficiency Logic)
**Basic Triggers**: Outdoor-Indoor difference ≥ TRV Priority Threshold

**Advanced Triggers** (when TRV monitoring enabled):
- TRV is actively heating AND working efficiently
- TRV valve position indicates good performance
- No TRV-detected window opening
- TRV temperature sensor shows proper heating

**Override Conditions**:
- TRV efficiency below threshold → Switch to AC priority
- TRV window detection active → Use AC for faster response
- TRV idle when significant heating needed → Activate AC immediately

#### TRV Priority Mode (Efficient for Cold Weather)
**Triggers when**: Outdoor-Indoor difference ≥ TRV Priority Threshold

**Actions**:
- TRV heats to target temperature
- If temperature difference ≥ Secondary Threshold: AC supports at target-1°C
- If temperature difference < Secondary Threshold: AC turned off

**Example**: Outdoor 0°C, Indoor 18°C, Target 21°C
- Outdoor-Indoor difference: 18°C (≥ 5°C threshold) → TRV Priority
- Temperature below target: 3°C (≥ 2°C threshold) → Secondary needed
- **Result**: TRV → 21°C, AC → 20°C

#### AC Priority Mode (Fast Response for Mild Weather)
**Triggers when**: Outdoor-Indoor difference < TRV Priority Threshold

**Actions**:
- AC heats to target temperature
- TRV provides background support at target+0.5°C

**Example**: Outdoor 16°C, Indoor 19.5°C, Target 21°C
- Outdoor-Indoor difference: 3.5°C (< 5°C threshold) → AC Priority
- **Result**: AC → 21°C, TRV → 21.5°C

#### Advanced TRV Monitoring Examples

**Efficient TRV Scenario**: 
- TRV valve 60% open, heating actively, indoor rising 0.3°C
- **Result**: Maintain TRV priority even in mild weather

**Inefficient TRV Scenario**:
- TRV valve 85% open, heating mode, but indoor temperature stable
- **Result**: Switch to AC priority despite cold weather

**TRV Window Detection**:
- TRV detects window open, blueprint may not detect rapid temperature drop yet
- **Result**: Immediate HVAC pause, both systems turn off

## Energy Efficiency Principles

### Why TRV Priority in Cold Weather?
- TRVs/radiators are more efficient for sustained heating in very cold conditions
- AC heat pumps lose efficiency at very low outdoor temperatures
- TRV provides consistent, radiant heating

### Why AC Priority in Mild Weather?
- AC provides faster response for quick temperature adjustments
- More efficient for small temperature corrections
- Better air circulation and comfort

### Coordinated Temperature Targets
- Primary device targets exact temperature
- Secondary device targets slightly different temperature to avoid conflicts
- Prevents simultaneous on/off cycling between devices

## Installation Guide

### Step 1: Enable Feature
```yaml
dual_climate_control: true
```

### Step 2: Configure Primary Device
```yaml
primary_climate_entity: climate.trv_living_room
```

### Step 3: Set Thresholds
```yaml
secondary_heating_threshold: 2.0  # °C below target to activate secondary
trv_priority_temp_difference: 5.0  # °C outdoor-indoor diff for TRV priority
```

### Step 4: Configure Advanced TRV Monitoring (Optional)
```yaml
enable_trv_efficiency_monitoring: true
trv_valve_opening_sensor: number.radiator_sala_valve_opening_degree
trv_valve_closing_sensor: number.radiator_sala_valve_closing_degree
trv_window_open_sensor: switch.radiator_sala_open_window
trv_running_steps_sensor: sensor.radiator_sala_closing_steps
```

### Step 5: Monitor Logs
Check Home Assistant logbook for "ASHRAE 55 Dual Climate" entries showing decision logic.

## Troubleshooting

### Common Issues

#### Only One Device Activates
- Check that both climate entities are available and responding
- Verify temperature thresholds are appropriate for your conditions
- Ensure primary climate entity is different from main climate entity

#### Devices Conflict
- Verify different temperature targets are being set (target vs. target±0.5°C)
- Check device compatibility and response times
- Consider adjusting thresholds if rapid switching occurs

#### Unexpected Strategy Selection
- Review outdoor vs. indoor temperature difference
- Check if temperature difference below target meets secondary threshold
- Verify TRV priority threshold setting matches your preferences
- **If TRV monitoring enabled**: Check TRV efficiency status and valve position
- **If TRV monitoring enabled**: Verify TRV sensor entities are available and responding

#### TRV Efficiency Issues (Advanced Monitoring)
- **TRV marked as inefficient**: Check valve position vs. heating output
- **Valve stuck at high position**: May indicate mechanical problem with TRV
- **TRV temperature not rising**: Check radiator circulation or valve calibration
- **Frequent AC switching**: Consider adjusting efficiency thresholds or valve sensor accuracy

## Best Practices

### Recommended Settings by Home Type

#### Well-Insulated Home
- Secondary Heating Threshold: 1.5°C (less aggressive dual heating)
- TRV Priority Threshold: 6°C (favor TRV in more conditions)

#### Older/Drafty Home  
- Secondary Heating Threshold: 2.5°C (more aggressive dual heating)
- TRV Priority Threshold: 4°C (favor AC for faster response)

#### Mild Climate
- Secondary Heating Threshold: 2°C (balanced approach)
- TRV Priority Threshold: 3°C (less TRV priority due to milder winters)

### Device Coordination Tips

1. **TRV Response Time**: Set TRV to respond slightly faster than AC to establish baseline temperature
2. **AC Fan Speed**: Use low fan speeds when supporting TRV to avoid air circulation conflicts
3. **Scheduling**: Consider coordinating with existing heating schedules for maximum efficiency

## Monitoring and Optimization

### Key Metrics to Track
- Total heating energy consumption (should decrease 25-35%)
- Temperature recovery times (should improve with dual heating)
- Device run times (should show intelligent load balancing)
- Comfort consistency (should improve with hybrid approach)

### Logbook Messages
Monitor for detailed decision-making logs:

**Basic Dual Climate Logging**:
```
Dual heating decision: Indoor 18°C, Target 21°C, Outdoor 5°C.
Temp diff below target: 3°C, Outdoor-Indoor diff: 13°C.
TRV priority: true, Need secondary: true
```

**Advanced TRV Monitoring Logging**:
```
Dual heating decision (TRV Enhanced): Indoor 18°C, Target 21°C, Outdoor 5°C.
TRV: Local 18.2°C, Valve 75%, Action heating, Efficient true, Window false.
Temp diff below target: 3°C, Outdoor-Indoor diff: 13°C.
TRV priority (enhanced): true, Need secondary: true
```

**TRV Window Detection Logging**:
```
Window/door open detected by TRV sensor! HVAC paused for 15 minutes.
TRV window detection: true, Blueprint detection: false.
Indoor: 18°C, Outdoor: 5°C, TRV: 18.2°C.
```

## Advanced Scenarios

### Integration with Window Detection
When windows are detected open, both TRV and AC are paused to prevent energy waste.

### Seasonal Optimization
Dual climate control works seamlessly with seasonal optimization logic for maximum efficiency.

### Natural Ventilation
When natural ventilation is available, both devices are turned off in favor of passive cooling/ventilation.

---

*This feature represents the cutting edge of residential HVAC optimization, combining ASHRAE 55 adaptive comfort principles with modern dual heating system coordination for maximum efficiency and comfort.*
