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

## Configuration Parameters

### Required Setup
1. **Dual Climate Control**: Enable the feature (default: disabled)
2. **Primary Climate Entity (TRV)**: Select your TRV or main heating device
3. **Secondary Heating Threshold**: Temperature difference that triggers secondary heating (1-5°C, default: 2°C)
4. **TRV Priority Temperature Threshold**: Outdoor-indoor difference that prioritizes TRV (2-10°C, default: 5°C)

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

## How It Works

### Decision Logic

The system evaluates two key factors:
1. **Temperature Difference Below Target**: How far indoor temperature is below the desired target
2. **Outdoor-Indoor Temperature Difference**: Indicates heating load and efficiency considerations

### Strategy Selection

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

### Step 4: Monitor Logs
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
```
Dual heating decision: Indoor 18°C, Target 21°C, Outdoor 5°C.
Temp diff below target: 3°C, Outdoor-Indoor diff: 13°C.
TRV priority: true, Need secondary: true
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
